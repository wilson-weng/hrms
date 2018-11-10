# coding=utf-8
import json
import time

from commons.utils import to_dict
from data.manager import CrewMgr, DwBillboardPointsMgr, DwChartPointsMgr, DatasetMgr, WageMgr


def sample_all():
    sets = DatasetMgr.query({'is_del': 0})
    for set in to_dict(sets):
        sample(set)


def sample(dataset):
    func = eval(dataset['sampler'])
    result, timestamp = func(dataset['org_id'], dataset['proj_id'])
    if dataset['data_type'] == 'billboard':
        DwBillboardPointsMgr.create(dataset_id=dataset['id'], rank_table=result, rank_time=timestamp)
    elif dataset['data_type'] == 'chart':
        DwChartPointsMgr.create(dataset_id=dataset['id'], y_value=result, x_time=timestamp)


def org_total_crew_num(org_id, proj_id):
    total_crew_num = CrewMgr.count({'org_id': org_id, 'is_del': 0})
    return total_crew_num, time.time()


def proj_crew_income_billboard(org_id, proj_id):
    last_record = WageMgr.query_first({'proj_id': proj_id, 'is_del': 0}, order_list=[WageMgr.model.amount.desc()])
    records = WageMgr.query({'proj_id': proj_id, 'wage_time': last_record.wage_time, 'is_del': 0}, limit=10, order_list=[WageMgr.model.amount.desc()])
    billboard = []
    for record in records:
        crew = CrewMgr.get(record.crew_id)
        billboard.append({'员工': crew.crew_name + crew.crew_account, '收入': float(record.amount)})
    return json.dumps(billboard), last_record.wage_time

