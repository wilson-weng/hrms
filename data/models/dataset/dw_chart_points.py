# -*- coding: utf8 -*-

from core import db


class DwChartPoints(db.Model):
    __tablename__ = 'dw_chart_points'
    __bind_key__ = 'hrms'
    __table_args__ = {"mysql_engine": "InnoDB", "mysql_charset": "utf8"}

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    dataset_id = db.Column(db.Integer, default=0)  # 所属公司编号
    x_time = db.Column(db.Integer, default=0)  # 所属公司编号
    y_value = db.Column(db.DECIMAL(precision=10, scale=2), default=0.00)  # 所属公司编号
    is_del = db.Column(db.SmallInteger, default=0)  # 是否删除：0-未删除；1-删除
    create_time = db.Column(db.Integer, default=0)  # 创建时间
