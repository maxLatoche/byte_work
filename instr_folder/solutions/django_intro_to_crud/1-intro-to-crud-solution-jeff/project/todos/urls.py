from django.conf.urls import include, url
from todos import views

urlpatterns = [
    url(r'^$', 'todos.views.index', name='index'),
    url(r'^create/$', 'todos.views.create', name='create'),
    url(r'^(?P<todo_id>[0-9]+)/$', 'todos.views.read', name='read'),
    url(r'^update/(?P<todo_id>[0-9]+)/$', 'todos.views.update', name='update'),
    url(r'^delete/(?P<todo_id>[0-9]+)/$', 'todos.views.delete', name='delete'),
]