from django.conf.urls import include,url
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.log_in, name='login'),
    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^analysis/$', views.analysis, name='analysis'),
    url(r'^analysisBBS/$', views.analysisBBS, name='BBS'),
    url(r'^published/', views.published, name='Published'),
    url(r'^postlist/$',views.postlist, name='postlist'),
    url(r'^(?P<position_id>[0-9]+)/$', views.item, name='item'),
    url(r'^analysisBBS/(?P<article_id>[0-9]+)/$', views.analysis, name='analysis'),
    url(r'^analysisBBS/(?P<article_id>[0-9]+)/comment/$', views.comment, name='comment'),
    url(r'^analysisBBS/(?P<article_id>[0-9]+)/keep/$', views.get_keep, name='keep'),
    url(r'^analysisBBS/(?P<article_id>[0-9]+)/poll/$', views.get_poll_article, name='poll'),
    url(r'^postlist/(?P<article_id>[0-9]+)/delete/$', views.aricle_delete, name='delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)