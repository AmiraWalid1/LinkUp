#!/usr/bin/python3 
import models
from models.base_model import BaseModel
from models.user import User
from models.post import Post
from models.comment import Comment
from models.like import Like

# amira = User(name='amira', password='123', email='amira@email.com')
# esraa = User(name='esraa', password='1234', email='esraa@email.com')

# post0 = Post(content='Hi! My name is amira.', user_id = amira.id)
# amira.posts.append(post0)

# comment0 = Comment(content=f'Hi Amira!!\nMy name is esraa.', user_id= esraa.id, post_id=post0.id)
# esraa.comments.append(comment0)
# post0.comments.append(comment0)

# # print(post0.user.name)
# # print(post0.comments[0].content)
# # print(post0.comments[0].user.name)

# like0 = Like(user_id=esraa.id, post_id = post0.id)

# post0.likes.append(like0)
# esraa.likes.append(like0)

# print(post0.likes[0].user)

# amira.save()
print(models.storage.all())
# print(models.storage.all(Like))
# print (models.storage.count())