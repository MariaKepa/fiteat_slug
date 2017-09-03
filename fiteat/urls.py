from django.conf.urls import url
from .import views
from django.contrib.auth.views import login, logout_then_login, password_change, password_change_done, password_reset, password_reset_done, password_reset_complete, password_reset_confirm

urlpatterns = [
    
url(r'^$', views.first_page, name='first_page'),
   
    url(r'^contact/$', views.aboutme, name= 'aboutme'),
    url(r'^statute/$', views.statute, name = 'statute'),
    url(r'^tips/', views.tips, name='tips'),
    url(r'^aboutme/$', views.contact , name = 'contact'),
    url(r'^diary/$', views.diary , name = 'diary'),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^login/$', login , name ='login'),
    url(r'^profile/$', views.profile, name = 'profile'),
    url(r'^calories/$', views.calories, name = 'calories'),
    url(r'^logout_then_login/$', logout_then_login, name = 'logout_then_login'), 
    url(r'^body_weight/$', views.body_weight, name = 'body_weight'),
    url(r'^edit_panel/$', views.edit_panel, name = 'edit_panel'),
    url(r'^password_change/$', password_change, name = 'password_change'),
    url(r'^password_change/done/$', password_change_done ,name= 'password_change_done'),
    # url(r'^product/$', views.product, name='product'),
    url(r'^product_list/$', views.product_list, name='product_list'),
    url(r'^product/(?P<id>[0-9]+)$', views.product_detail, name='product_detail'),
    url(r'^password_reset/$', password_reset, name = 'password_reset'),
    url(r'^password_reset/done/$', password_reset_done, name = 'password_reset_done'),
    url(r'^password_reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', password_reset_confirm, name = 'password_reset_confirm'),
    url(r'^password_reset/complete/$', password_reset_complete, name = 'password_reset_complete'),

    url(r'^remove_diary_entry/(?P<id>[0-9]+)/$', views.remove_diary_entry, name='remove_diary_entry'),
    
    # url(r'^search/$', views.product_search, name = 'product_search'),
    url(r'^search/$', views.search, name = 'search'),



 ]
