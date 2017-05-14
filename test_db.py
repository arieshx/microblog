#test_db.py
# -*- coding: utf-8 -*-
from app import db, models
import datetime


#增加几个user进数据库
# u = models.User(nickname='john', email='john@email.com')
# db.session.add(u)
# u = models.User(nickname='susan', email='susan@email.com')
# db.session.add(u)
# db.session.commit()

#查询所有的user出来
users = models.User.query.all()
print users

#增加一个blog进数据库
# u = models.User.query.get(1)
# p = models.Post(body='my first post!', timestamp=datetime.datetime.utcnow(), author=u)
# db.session.add(p)
# db.session.commit()

#多做一些查询
u = models.User.query.get(1)#u是一个user，查他的blog
posts = u.posts.all()
print posts

#obtain author of each post
for p in posts:
	print p.id,p.author.nickname,p.body

# get all users in reverse alphabetical order
print models.User.query.order_by('nickname desc').all()
