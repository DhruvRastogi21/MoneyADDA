from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^transaction/$',views.new_transaction,name='new_transaction')

]