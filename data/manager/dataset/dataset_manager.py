# -*- encoding: utf8 -*-
from commons.helper.db_manager import DBManager
from data.models.dataset.dataset import Dataset


class DatasetManager(DBManager):

    def __init__(self):
        super(DBManager, self).__init__()
        self.model = Dataset
        self.params = self.get_editable_fields()
