# -*- encoding: utf8 -*-
from commons.helper.db_manager import DBManager
from data.models.wage_raw_data import WageRawData


class WageRawDataManager(DBManager):

    def __init__(self):
        super(DBManager, self).__init__()
        self.model = WageRawData
        self.params = self.get_editable_fields()

    def create_override_if_exist(self, record):
        history_record = self.query_first({'bill_id': record['bill_id'], 'position': record['position'], 'is_del': 0})
        if history_record:
            self.update(history_record, **record)
        else:
            self.create(**record)

