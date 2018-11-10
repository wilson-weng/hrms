# coding=utf-8
import json
import traceback

from flask import jsonify, request

from controller import get_request_proj_id, get_request_org_id
from core import app
from service import crew_service


@app.route("/crew", methods=['POST'])
def create_crew_record():
    """
    创建赔付记录
    :return:
    """
    try:
        proj_id = get_request_proj_id()
        org_id = get_request_org_id()
        lines = request.form.get("lines", None)
        result = crew_service.create_crew_record(org_id, proj_id, json.loads(lines))
        return jsonify(status='ok', data=result)
    except Exception, ex:
        traceback.print_exc()
        return jsonify(status='error', msg=ex.message)


@app.route("/crew/<int:crew_id>", methods=['DELETE'])
def delete_crew_record(crew_id):
    """
    查找赔付记录
    :return:
    """
    try:
        data = crew_service.delete_crew_record(crew_id)
        return jsonify(status='ok', content=data)
    except Exception, ex:
        return jsonify(status='error', msg=ex.message)


@app.route("/crew/<int:crew_id>", methods=['PUT'])
def update_crew_record(crew_id):
    """
    查找赔付记录
    :return:
    """
    try:
        content = json.loads(request.form.get('content'))
        crew_service.update_crew_records(crew_id, content)
        return jsonify(status='ok')
    except Exception, ex:
        return jsonify(status='error', msg=ex.message)