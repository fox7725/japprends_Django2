from django.contrib import admin
from django.contrib.auth.views import (
    LoginView, PasswordChangeView, PasswordChangeDoneView)
from django.urls import path

import authentification.views
import blog.views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
        template_name='authentification/login.html',
        redirect_authenticated_user=True),
         name='login'),
    path('logout/', authentification.views.logout_user, name='logout'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='authentification/password_change_form.html'),
         name='password_change'
    ),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='authentification/password_change_done.html'),
    ),
    path('signup', authentification.views.signup_page, name='signup'),
    path('profile-photo/upload', authentification.views.upload_profile_photo,
         name='upload_profile_photo'),
    path('home/', blog.views.home, name='home'),
    path('photo/upload/', blog.views.photo_upload, name='photo_upload')
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
