# coding=utf-8
import traceback

from flask import jsonify, request

from core import app
from service import supplier_service


@app.route("/supplier", methods=['POST'])
def create_supplier():
    """
    创建项目
    :return:
    """
    try:
        data = supplier_service.create_supplier(request.form)
        return jsonify(data)
    except Exception, ex:
        traceback.print_exc()
        return jsonify(status='error', msg=ex.message)


@app.route("/supplier/<int:supplier_id>", methods=['PUT'])
def update_supplier(supplier_id):
    """
    更改项目
    :return:
    """
    try:
        data = supplier_service.update_supplier(supplier_id, request.form)
        return jsonify(data)
    except Exception, ex:
        traceback.print_exc()
        return jsonify(status='error', msg=ex.message)


@app.route("/supplier/<int:supplier_id>", methods=['DELETE'])
def delete_supplier(supplier_id):
    try:
        data = supplier_service.delete_supplier(supplier_id)
        return jsonify(data)
    except Exception, ex:
        return jsonify(status='error', msg=ex.message)
