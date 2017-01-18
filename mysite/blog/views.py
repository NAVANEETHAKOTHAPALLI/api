#from django.shortcuts import render

# Create your views here.
from blog.models import Post, Tag, Author
from .serializers import PostSerializer, TagSerializer, AuthorSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from blog.serializers import UserSerializer

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class PostList(generics.ListCreateAPIView):
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class TagList(generics.ListCreateAPIView):
    model = Tag
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Tag
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class AuthorList(generics.ListCreateAPIView):
    model = Author
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Author
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

