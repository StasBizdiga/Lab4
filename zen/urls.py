from django.conf.urls import url

from . import views

app_name = 'zen'

urlpatterns = [
    # ex: /zen/
    url(r'^$', views.index, name='index'),
    # ex: /zen/#num/   where #num is a number
    url(r'^(\d+)/$', views.detail, name='detail'),
    # ex: /zen/fun
    url(r'^fun/', views.fun, name='fun'),
    url(r'^ajax/show_tip/$', views.show_tip, name='show_tip'),

]


