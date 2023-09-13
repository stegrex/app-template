import json
from abc import ABC, abstractmethod

class BaseObject(ABC):

    STATUS_INACTIVE = 0
    STATUS_ACTIVE = 1

    # TODO: Use standard docstring.
    """
    Return dict of attribute: values:
    {
        "attribute0": "value0",
        "attribute1": "value1"
    }
    """
    @abstractmethod
    def get_default_attributes(self):
        pass

    # TODO: Use standard docstring.
    """
    Return name of DB table in string form.
    """
    @abstractmethod
    def get_table(self):
        pass

    # TODO: Use standard docstring.
    """
    Return name of primary key in string form.
    """
    @abstractmethod
    def get_primary_key_name(self):
        pass

    # TODO: Use standard docstring.
    """
    Return a new instance of overriding child class.
    """
    @abstractmethod
    def get_instance(self):
        pass

    def __init__(self):
        default_attributes = self.get_default_attributes()
        for key in default_attributes:
            setattr(self, key, default_attributes[key])

    def from_dictionary(self, itemDict):
        default_attributes = self.get_default_attributes()
        for key in default_attributes:
            if key in itemDict:
                setattr(self, key, itemDict[key])

    def to_dictionary(self):
        outputDict = {}
        default_attributes = self.get_default_attributes()
        for key in default_attributes:
            outputDict[key] = getattr(self, key)
        return outputDict

    def from_db_dictionary(self, itemDict):
        self.from_dictionary(itemDict)
        self.properties = json.loads(itemDict.get("properties"))

    def to_db_dictionary(self):
        dbDict = self.to_dictionary()
        dbDict["properties"] = json.dumps(dbDict["properties"])
        return dbDict
