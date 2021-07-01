from django.conf.urls import include, url
from django.urls import path
from . import views
#from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView
from flmate.views import user_login,edit,register,index,dialog,messages

urlpatterns = [
    url(r'^login/$', user_login, name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),
    url(r'^edit/$', edit, name='edit'),
    url(r'^password-change/$', PasswordChangeView.as_view(), name='password_change'),
    url(r'^password-change/done/$', PasswordChangeDoneView.as_view(), name='password_change_done'),
    url(r'^password-reset/$', PasswordResetView.as_view(), name='password_reset'),
    url(r'^password-reset/done/$', PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^password-reset/complete/$',PasswordResetCompleteView.as_view() , name='password_reset_complete'),
    url(r'^register/$', register, name='register'),
    url(r'^index/$', index, name='index'),
    url(r'^dialogs/$', dialog, name='dialogs'),
    url(r'^messages/(?P<chat_id>\d+)/$', messages, name='messages'),
    path("select2/", include("django_select2.urls")),
]   