from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.book),
    url(r'^books/(?P<num>\d+)$', views.bookInfo),
    url(r'^linkAuth/(?P<num>\d+)$', views.linkAuth),
    url(r'^addBook$', views.addBook),
    url(r'^authors$', views.author),
    url(r'^authors/(?P<num>\d+)$', views.authInfo),
    url(r'^linkBook/(?P<num>\d+)$', views.linkBook),
    url(r'^addAuth$', views.addAuth),
]