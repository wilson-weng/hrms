# -*- coding: utf8 -*-

from core import db


class DwBillboardPoints(db.Model):
    __tablename__ = 'dw_billboard_points'
    __bind_key__ = 'hrms'
    __table_args__ = {"mysql_engine": "InnoDB", "mysql_charset": "utf8"}

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    dataset_id = db.Column(db.Integer, default=0)  # 所属公司编号
    rank_table = db.Column(db.TEXT)  # 项目名称
    rank_time = db.Column(db.Integer, default=0)  # 所属公司编号
    is_del = db.Column(db.SmallInteger, default=0)  # 是否删除：0-未删除；1-删除
    create_time = db.Column(db.Integer, default=0)  # 创建时间
