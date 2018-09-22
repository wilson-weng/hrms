# -*- encoding: utf8 -*-
from commons.helper.db_manager import DBManager
from dao.models.wage import Wage


class WageManager(DBManager):

    def __init__(self):
        super(DBManager, self).__init__()
        self.model = Wage
        self.params = self.get_editable_fields()

    def create_override_if_exist(self, record):
        history_record = self.query_first({'bus_id': record['bus_id'], 'is_del': 0})
        if history_record:
            self.update(history_record, **record)
        else:
            self.create(**record)