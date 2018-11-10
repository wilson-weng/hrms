# coding=utf-8
import json

from commons.utils import to_dict, time_util
from data.manager import DwBillboardPointsMgr, DwChartPointsMgr, DatasetMgr


class DatasetDao:

    @staticmethod
    def add_newest_points(scale, data):
        """
        赔付发生日期yyyy-mm-dd
        """
        if 'id' in data:
            dataset_id = data['id']
            data_type = data['data_type']
            if data_type == 'billboard':
                points = DwBillboardPointsMgr.query({'dataset_id': dataset_id, 'is_del': 0}, limit=scale,
                                                    order_list=[DwBillboardPointsMgr.model.rank_time.desc()])
            elif data_type == 'chart':
                points = DwChartPointsMgr.query({'dataset_id': dataset_id, 'is_del': 0}, limit=scale,
                                                order_list=[DwChartPointsMgr.model.x_time.desc()])
            else:
                points = []
            data['points'] = to_dict(points)

    @staticmethod
    def get_dataset_by_title(org_id, proj_id, sampler):
        """通过项目id获取单个项目"""
        dataset = DatasetMgr.query_first({'org_id': org_id, 'proj_id': proj_id, 'sampler': sampler})
        return to_dict(dataset)