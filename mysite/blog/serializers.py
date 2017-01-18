from rest_framework import serializers
from blog.models import  Post, Tag, Author
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.HyperlinkedIdentityField('posts', view_name='userpost-list', lookup_field='username')

    class Meta:
        model = User
		fields = ('id','username','posts')

class PostSerializer(serializers.ModelSerializer):
    #author = UserSerializer(required=False)

    class Meta:
        model = Post
        fields =('title','created_date','tags','content')
    
class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        fields =('tag_name','tag_description')

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('author_name','author_email')