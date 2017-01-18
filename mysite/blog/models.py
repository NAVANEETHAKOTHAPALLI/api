from django.db import models

# Create your models here.
#from django.contrib.auth.models import AbstactUser
'''
class User(AbstractUser):
	followers = models.ManyToManyField('self',name='followers',symmetrical=False)
'''

class Post(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=120)
    #author = models.ForeignKey(User,name='posts')
    content = models.TextField()
    
class Tag(models.Model):
	tag_name = models.CharField(max_length=150)
	tag_description = models.TextField()

class Author(models.Model):
	author_name =models.CharField(max_length=200)
	author_email = models.EmailField(max_length=150)
