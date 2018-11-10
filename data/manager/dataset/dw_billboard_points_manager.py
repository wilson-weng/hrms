# -*- encoding: utf8 -*-
from commons.helper.db_manager import DBManager
from data.models.dataset.dw_billboard_points import DwBillboardPoints


class DwBillboardPointsManager(DBManager):

    def __init__(self):
        super(DBManager, self).__init__()
        self.model = DwBillboardPoints
        self.params = self.get_editable_fields()
