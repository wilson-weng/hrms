# -*- encoding: utf8 -*-
from commons.helper.db_manager import DBManager
from data.models.supplier import Supplier


class SupplierManager(DBManager):

    def __init__(self):
        super(DBManager, self).__init__()
        self.model = Supplier
        self.params = self.get_editable_fields()

    def get_supplier_name_id_map(self, org_id):
        result = self.query({'org_id': org_id, 'is_del': 0})
        return {item.supplier_name: item.id for item in result}