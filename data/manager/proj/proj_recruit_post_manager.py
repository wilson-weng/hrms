# -*- encoding: utf8 -*-
import time

from commons.helper.db_manager import DBManager
from data.models.proj.proj_recruit_post import ProjRecruitPost


class ProjRecruitPostManager(DBManager):

    def __init__(self):
        super(DBManager, self).__init__()
        self.model = ProjRecruitPost
        self.params = self.get_editable_fields()

    def modified(self, id):
        post = self.get(id)
        if post:
            self.update(post, modify_time=time.time())