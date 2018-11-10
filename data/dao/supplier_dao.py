# coding=utf-8
import json

from commons.utils import to_dict, time_util
from data.manager import SupplierMgr, CrewMgr


class SupplierDao:

    @staticmethod
    def list_supplier(org_id, page, page_size=10):
        """获取供应商列表并分页,"""
        filter_condition = {'is_del': 0, 'org_id': org_id}
        count = SupplierMgr.count(filter_conditions=filter_condition)
        if page_size > 5000:
            page_size = 5000
        records = SupplierMgr.query(filter_conditions=filter_condition, limit=page_size,
                                    offset=(page - 1) * 10)
        return {'total_count': count, 'datas': to_dict(records)}

    @staticmethod
    def add_total_crew_num(org_id, data):
        """
        获取项目员工数量
        """
        if 'id' in data:
            crew_num = CrewMgr.count({'org_id': org_id, 'supplier_id': data['id'], 'is_del': 0})
            data['total_crew_num'] = crew_num

    @staticmethod
    def add_current_crew_num(org_id, data):
        """
        获取项目员工数量
        """
        if 'id' in data:
            crew_num = CrewMgr.count({'org_id': org_id, 'supplier_id': data['id'], 'work_status': 1, 'is_del': 0})
            data['current_crew_num'] = crew_num