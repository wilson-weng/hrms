# coding=utf-8
import json

from commons.exception import BatchUploadError
from data.manager import CrewMgr, CrewLevelMgr, SupplierMgr


def create_crew_record(org_id, proj_id, lines):
    line_index = 0
    errors = []
    supplier_map = SupplierMgr.get_supplier_name_id_map(org_id)
    for line in lines:
        line_index += 1
        record = {'org_id': org_id, 'proj_id': proj_id, 'meta': {}}
        for key, value in line.items():
            line[key] = value.strip()
            if key in CrewMgr.params:
                record[key] = value
            else:
                record['meta'][key] = value
        if line['supplier_name'] in supplier_map:
            record['supplier_id'] = supplier_map[line['supplier_name']]
        else:
            errors.append(BatchUploadError(line_index, '供应商不存在').to_dict())
            continue
        record['id_card_num'] = record['id_card_num'].lower()
        record['meta'] = json.dumps(record['meta'])
        crew = CrewMgr.create_override_if_exist(record)
        level = CrewLevelMgr.query_first({'crew_id': crew.id, 'is_del': 0})
        if not level:
            CrewLevelMgr.create(crew_id=crew.id, crew_name=record['crew_name'], level_name='青铜')
    return {'errors': errors, 'lines': lines}


def update_crew_records(crew_id, content):
    crew = CrewMgr.get(crew_id)
    if crew:
        CrewMgr.update(crew, **content)


def delete_crew_record(crew_id):
    record = CrewMgr.get(crew_id)
    if record:
        CrewMgr.delete(record)
