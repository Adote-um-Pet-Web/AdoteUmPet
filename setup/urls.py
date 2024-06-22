from allauth.socialaccount.providers.google.urls import (
    urlpatterns as google_urlpatterns,
)
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path, re_path

from userauth import views as userauth_views

social_urlpatterns = [
    path("", include(google_urlpatterns)),
]
from django.views.static import serve

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("", include("pet.urls")),
    path("user/", include("userauth.urls")),
    path("adoption/", include("adoption.urls")),
    path("accounts/", include(social_urlpatterns)),
    path(
        "accounts/social/login/cancelled/",
        userauth_views.SocialaccountLoginCancelled.as_view(),
    ),
    # CHANGE PASSWORD
    path(
        "password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]
