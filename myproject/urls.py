from django.urls import path, re_path
from django.contrib import admin
from boards import views
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.BoardListView.as_view(), name = 'home'),
    path('boards/<int:pk>/', views.TopicListView.as_view(), name='board_topics'),
    path('boards/<int:pk>/new/',views.new_topic, name = 'new_topic'),
    path("admin/", admin.site.urls),
    path('signup/', accounts_views.signup, name ='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html',email_template_name='password_reset_email.html',subject_template_name='password_reset_subject.txt'),name='password_reset'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    re_path(r"reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$",auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    path('settings/password/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name = 'password_change'),
    path('settings/password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name = 'password_change_done'),
    re_path('boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.PostListView.as_view(), name='topic_posts'),
    re_path('boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', views.reply_topic, name='reply_topic'),
    re_path('boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='edit_post'),
    path('settings/account/', accounts_views.UserUpdateView.as_view(), name = 'my_account'),
]
