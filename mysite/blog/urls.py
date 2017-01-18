from django.conf.urls import patterns, url, include

from blog.views import PostList, PostDetail
from blog.views import TagList, TagDetail
from blog.views import AuthorList,AuthorDetail 

post_urls = patterns('',
	url(r'^myname/(?P<pk>\d+)/$', PostDetail.as_view(), name='post-detail'),
    url(r'^$', PostList.as_view(), name='post-list')
)

tag_urls = patterns('',
	url(r'^myname/(?P<pk>\d+)/$',TagDetail.as_view(), name='tag-detail'),
    url(r'^$', TagList.as_view(), name='tag-list')
)

author_urls = patterns('',
    url(r'^myname/(?P<pk>\d+)/$', AuthorDetail.as_view(), name='author-detail'),
    url(r'^$', AuthorList.as_view(), name='author-list')
)

user_urls = patterns(''
	url(r'^users/(?P<pk>)[0-9]+)/$', UserDetail.as_view(), name='user-detail')
	url(r'^users/$', UserList.as_view(), name='user-list'),




urlpatterns = patterns('',
	url(r'^s',include(post_urls)),
	url(r'^',include(tag_urls)),
	url(r'^',include(author_urls)),
)
	