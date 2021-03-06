# -*- coding: utf8 -*-

from core import db


class UserProjRightsMap(db.Model):
    __tablename__ = 'user_proj_rights_map'
    __bind_key__ = 'hrms'
    __table_args__ = {"mysql_engine": "InnoDB", "mysql_charset": "utf8"}

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    manager_id = db.Column(db.Integer, default=0, nullable=False) # 管理员编号
    company_id = db.Column(db.Integer, default=0, nullable=False) # 公司编号
    proj_id = db.Column(db.Integer, default=0, nullable=False) # 项目编号
    is_del = db.Column(db.SmallInteger, default=0)  # 是否删除：0-未删除；1-删除
    create_time = db.Column(db.Integer, default=0)  # 创建时间

