from django.conf.urls import url,include
from accounts.views import view_list,search,view_home,profile,register,edit_profile
from django.contrib.auth.views import login,logout

urlpatterns = [
    url(r'list/$',view_list,name='list'),
    url(r'home/$',view_home),
    url(r'profile/$',profile,name='profile'),
    url(r'home/result/$',search,name='result'),
    url(r'login/$',login,{'template_name': 'accounts/login.html'},name='login'),
    url(r'logout/$',logout, {'template_name': 'accounts/home.html'},name='logout'),
    url(r'edit/$',edit_profile,name='edit'),
    url(r'signup/$',register,name='signup'),
]
