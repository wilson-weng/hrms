# -*- coding: utf8 -*-

from core import db


class Dataset(db.Model):
    __tablename__ = 'dataset'
    __bind_key__ = 'hrms'
    __table_args__ = {"mysql_engine": "InnoDB", "mysql_charset": "utf8"}

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    org_id = db.Column(db.Integer, default=0)  # 所属公司编号
    proj_id = db.Column(db.Integer, default=0)  # 所属公司编号
    title = db.Column(db.String(64), default='', nullable=False)  # 项目名称
    desc = db.Column(db.String(128), default='', nullable=False)  # 项目名称
    data_type = db.Column(db.String(64), default='', nullable=False)  # 项目名称
    sampler = db.Column(db.String(128), default='', nullable=False)  # 项目名称
    sample_frequency = db.Column(db.Integer, default=0)  # 所属公司编号
    is_del = db.Column(db.SmallInteger, default=0)  # 是否删除：0-未删除；1-删除
    create_time = db.Column(db.Integer, default=0)  # 创建时间
