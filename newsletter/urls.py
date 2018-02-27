from django.conf.urls import url
from . import views


urlpatterns = [
    url(regex=r'^$', view=views.home, name='home'),
    url(regex=r'^about/$', view=views.about, name='about'),
    url(regex=r'^newsletters/$', view=views.newsletter_list, name='news_list'),
    url(regex=r'^newsletters/(?P<id>[-\w]+)/$', view=views.newsletter_detail, name='news_detail'),
]
