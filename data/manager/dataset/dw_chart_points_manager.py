# -*- encoding: utf8 -*-
from commons.helper.db_manager import DBManager
from data.models.dataset.dw_chart_points import DwChartPoints


class DwChartPointsManager(DBManager):

    def __init__(self):
        super(DBManager, self).__init__()
        self.model = DwChartPoints
        self.params = self.get_editable_fields()
