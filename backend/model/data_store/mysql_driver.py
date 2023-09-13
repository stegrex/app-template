import mysql.connector
import time
import pprint
from model.data_store.base_driver import BaseDriver

# TODO: Move to mysqlclient if need faster connections.
# https://github.com/PyMySQL/mysqlclient

class MySQLDriver(BaseDriver):

    def init_connection(self, dbName):
        self.connection = mysql.connector.connect(
            user="root",
            password="test",
            host="db",
            database=dbName
        )
        self.cursor = self.connection.cursor()

    def commit(self):
        return self.connection.commit()

    def rollback(self):
        return self.connection.rollback()

    def destruct(self):
        self.cursor.close()
        self.connection.close()

    # NOTE: This only prepares updates ready for atomic transactional commit.
    # Use MySQLDriver.commit() to persist data in the DB.
    def upsert(self, object=None, createdTime=None, expirationTime=None):
        '''
        if createdTime:
            object.createdTime = createdTime
        else:
            object.createdTime = int(time.time())
        '''
        operation, params = self._construct_upsert_operation(object)
        pprint.pprint([operation, params])
        if operation == None or operation == "" or params == None:
            return objects, False
        response = self.cursor.execute(operation, params)
        return object, response

    def filter_multiple(self, object, filter):
        operation, params = self._construct_filter_operation(object, filter)
        pprint.pprint([operation, params])
        objects = []
        if (
            operation == None or operation == "" or
            params == None or len(params) == 0
        ):
            return objects, False
        response = self.cursor.execute(operation, params)
        for itemTuple in self.cursor:
            item = dict(zip(self.cursor.column_names, itemTuple))
            itemObject = object.get_instance()
            itemObject.from_db_dictionary(item)
            objects.append(itemObject)
        return objects, response

    def _construct_upsert_operation(
        self,
        object,
        filterCriteria={}
    ):
        table = object.get_table()
        values = object.to_db_dictionary()
        placeholders = []
        duplicateKeyPlaceholders = []
        operation = ""
        params = {}
        if not self._validate_table_string(object, table):
            return operation, params
        for x in values:
            if not self._validate_col_string(object, x):
                return operation, params
            placeholders.append("%(" + str(x) + ")s")
            if str(x) != object.get_primary_key_name():
                duplicateKeyPlaceholders.append(
                    str(x) + " = %(" + str(x) + ")s"
                )
            params[str(x)] = values[x]
        operation = (
            "insert into " + table + " " +
            "(" + ", ".join(list(values)) + ") values " 
            "(" + ", ".join(placeholders) + ") " +
            "on duplicate key update " +
            ", ".join(duplicateKeyPlaceholders)
        )
        return operation, params

    def _construct_filter_operation(
        self,
        object,
        filterCriteria={}
    ):
        table = object.get_table()
        values = object.to_db_dictionary()
        placeholders = []
        duplicateKeyPlaceholders = []
        operation = ""
        params = {}
        if not self._validate_table_string(object, table):
            return operation, params
        whereCriteriaStrings = []
        for col in filterCriteria:
            if not self._validate_col_string(object, col):
                return operation, params
            values = filterCriteria[col]
            if not values or len(values) == 0:
                continue
            currentPlaceholders = []
            for x in range(len(values)):
                placeholder = col + "_" + str(x)
                currentPlaceholders.append("%(" + placeholder + ")s")
                params[placeholder] = values[x]
            whereCriteriaStrings.append(
                col + " in (" + ", ".join(currentPlaceholders) + ")"
            )
        if len(params) == 0:
            return operation, params
        operation = (
            "select * from " + table + " where " +
            " and ".join(whereCriteriaStrings)
        );
        return operation, params

    def _validate_table_string(self, object, string):
        table = object.get_table()
        if table == string:
            return True
        return False

    def _validate_col_string(self, object, string):
        objectDict = object.to_dictionary()
        if string in objectDict:
            return True
        return False

    def _delete(self, documentID):
        return self.connection

    def _delete_all(self):
        return self.connection

    def _drop_collection(self):
        return self.connection

    def _drop_db(self):
        return self.connection
