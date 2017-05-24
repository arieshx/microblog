#test_db.py
# -*- coding: utf-8 -*-
from app import models
import datetime

session = models.DBSession()
#增加几个生产部件信息进去

# u=models.factorycompo_table(factoryId=1,compoType="手机壳",compoMaxCount=5)
# session.add(u)
# session.commit()

