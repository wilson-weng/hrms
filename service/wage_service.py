# coding=utf-8
import json

from commons.exception import BatchUploadError
from commons.utils import time_util, to_dict
from core.framework.plugin import execute_plugin
from data.manager import WageMgr, WageRawDataMgr, CrewMgr
from data.manager.proj import ProjOfferMgr


def create_wage_raw_data(proj_id, lines):
    line_index = 0
    data = {'errors': []}
    for line in lines:
        line_index += 1
        crew_id = CrewMgr.get_crew_id_by_account(line['crew_account'])
        if not crew_id:
            data['errors'].append(BatchUploadError(line_index, '该员工没有录入系统').to_dict())
            continue
        wage_time = time_util.dateString2timestampCommon(line['wage_time'])
        record = {
            'proj_id': proj_id,
            'crew_id': crew_id,
            'bill_id': '%d%d%d' % (proj_id, wage_time, crew_id),
            'wage_time': wage_time
        }
        records = []
        for key, value in line.items():
            if key.endswith('量') and float(value) > 0:
                record['position'] = key.replace('量', '')
                record['work_amount'] = value
                records.append(record.copy())
        for record in records:
            record['work_hours'] = float(line['work_hours']) / len(records)
            WageRawDataMgr.create_override_if_exist(record)
    return data


def calculate(proj_id, date):
    offers = ProjOfferMgr.query({'proj_id': proj_id, 'is_del': 0})
    date_timestamp = time_util.dateString2timestampCommon(date)
    raw_datas = WageRawDataMgr.query({'proj_id': proj_id, 'wage_time': date_timestamp, 'is_del': 0})
    calculated_datas = []
    for offer in offers:
        if offer.position != '所有':
            data = {'offer': to_dict(offer), 'raw_datas': to_dict(raw_datas), 'calculated_datas': []}
            result = execute_plugin('offer', offer.id, 'on_position_calculate', {}, data)
            calculated_datas.extend(result['data']['calculated_datas'])

    wage_maps = {}
    for data in calculated_datas:
        key = '%s_%s_%s' % (data['supplier_id'], data['offer_type'], data['crew_id'])
        if key in wage_maps:
            wage_maps[key]['amount'] += data['amount']
            wage_maps[key]['work_rate'] += data['work_rate']
        else:
            wage_maps[key] = data
    for offer in offers:
        if offer.position == '所有':
            data = {'offer': to_dict(offer), 'wage_datas': wage_maps.values()}
            result = execute_plugin('offer', offer.id, 'on_position_agregate_calculate', {}, data)
            for item in result['data']['wage_datas']:
                WageMgr.create_override_if_exist(item)
