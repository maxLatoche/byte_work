from django.conf.urls import url
import blog.views
from blog.views import UserLogin


urlpatterns = [
    url(r'^$', blog.views.index, name='index'),
    url(r'^add$', blog.views.add, name='add'),
    url(r'^edit/(?P<id>[0-9]+)$', blog.views.edit, name='edit'),
    url(r'^delete/(?P<id>[0-9]+)$', blog.views.delete, name='delete'),
    url(r'^register$', blog.views.register, name='register'),
    url(r'^login$', UserLogin.as_view(), name='login'),
    url(r'^logout$', blog.views.user_logout, name='logout'),
]
