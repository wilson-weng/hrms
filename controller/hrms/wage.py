# coding=utf-8
import json
import traceback

from flask import jsonify, request

from controller import get_request_proj_id
from core import app
from service import wage_service


@app.route("/wage/raw", methods=['POST'])
def create_wage_record():
    """
    创建收入记录
    :return:
    """
    try:
        proj_id = get_request_proj_id()
        lines = request.form.get("lines", None)
        result = wage_service.create_wage_raw_data(proj_id, json.loads(lines))
        return jsonify(status='ok', data=result)
    except Exception, ex:
        traceback.print_exc()
        return jsonify(status='error', msg=ex.message)


@app.route("/wage/calculate", methods=['GET'])
def calculate_wage():
    """
    创建收入记录
    :return:
    """
    try:
        date = request.args.get('date')
        proj_id = request.args.get('proj_id')
        result = wage_service.calculate(proj_id, date)
        return jsonify(status='ok', data=result)
    except Exception, ex:
        traceback.print_exc()
        return jsonify(status='error', msg=ex.message)
