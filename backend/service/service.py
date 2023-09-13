import uuid
from model.data_store.mysql_driver import MySQLDriver
from model.objects.item import Item

class Service():

    def __init__(self, dbDriver=None):
        if not dbDriver:
            dbDriver = MySQLDriver()
            dbDriver.init_connection("app_template")
        self.dbDriver = dbDriver

    def upsert_item(self, itemDict):
        item = Item()
        item.from_dictionary(itemDict)
        if not item.id:
            item.id = str(uuid.uuid4())
        executionResponse = None
        try:
            item, response = self.dbDriver.upsert(item)
            executionResponse = self.dbDriver.commit()
        except Exception as e:
            executionResponse = self.dbDriver.rollback()
            #print(e)
            #print(executionResponse)
        return item, executionResponse

    def filter_items(self, filters):
        item = Item()
        items, response = self.dbDriver.filter_multiple(item, filters)
        return items, response
