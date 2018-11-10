# -*- coding: utf8 -*-
from core import db


class Wage(db.Model):

    __tablename__ = 'wage'
    __bind_key__   = 'hrms'
    __table_args__ = {"mysql_engine":"InnoDB", "mysql_charset":"utf8"}

    id = db.Column(db.BigInteger, primary_key=True, nullable=False, autoincrement=True)
    proj_id = db.Column(db.Integer, default=0)  # 项目编号
    crew_id = db.Column(db.Integer, default=0)  # 项目编号
    supplier_id = db.Column(db.Integer, default=0)  # 项目编号
    offer_type = db.Column(db.SmallInteger, default=0) #是否删除：0-员工应收；1-供应商应付
    bill_id = db.Column(db.String(128), default='', nullable=False)  # 业务id
    amount  = db.Column(db.DECIMAL(precision=10, scale=2), default=0.00)     #返现
    work_rate = db.Column(db.Integer, default=0)  # 项目编号
    wage_status = db.Column(db.SmallInteger, default=0) #奖励状态 0-初始 2-已确认 4-可提现 -1-已取消 -2-异常
    meta = db.Column(db.String(512, collation='utf8_unicode_ci'), default='')  # 收入备注

    wage_time        = db.Column(db.Integer, default=0) #收入时间
    confirm_time        = db.Column(db.Integer, default=0) #收入确认时间
    is_del = db.Column(db.SmallInteger, default=0) #是否删除：0-未删除；1-删除
    create_time = db.Column(db.Integer, default=0) #创建时间


