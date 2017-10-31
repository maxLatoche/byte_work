from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'todos.views.index', name='index'),
]