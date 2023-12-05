from django.contrib import admin
from django.urls import include, path, re_path

from users.views import UserListAPIView, UserRetrieveAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", UserListAPIView.as_view()),
    path('users/<int:id>/', UserRetrieveAPIView.as_view()),
    path("auth/", include("djoser.urls")),
    re_path(r"auth/", include("djoser.urls.authtoken")),
]
