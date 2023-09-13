import json
from model.objects.base_object import BaseObject

class Item(BaseObject):

    def get_default_attributes(self):
        return {
            "id": None,
            "title": "",
            "properties": {}
        }

    def get_table(self):
        return "item"

    def get_primary_key_name(self):
        return "id"

    def get_instance(self):
        return Item()
