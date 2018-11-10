# -*- encoding: utf8 -*-

from controller import get_request_org_id
from data.manager import SupplierMgr
from commons.utils import to_dict, web_util


def create_supplier(form):

    org_id = get_request_org_id()
    name = form['supplier_name']
    supplier = SupplierMgr.query_first({'supplier_name': name})
    if supplier:
        if supplier.is_del == 1:
            SupplierMgr.restore(supplier)
    else:
        supplier = SupplierMgr.create(org_id=org_id, supplier_name=name)
    return dict(status='ok', data=to_dict(supplier))


def update_supplier(supplier_id, form):
    supplier = SupplierMgr.get(supplier_id)
    if supplier is None:
        return dict(status='error', msg='无效的供应商编号')
    SupplierMgr.update(supplier, **form)
    return dict(status='ok', data=to_dict(supplier))


def delete_supplier(supplier_id):
    supplier = SupplierMgr.get(supplier_id)
    if supplier is None:
        return dict(status='error', msg='要删除的供应商不存在')
    SupplierMgr.delete(supplier)
    return dict(status='ok')
