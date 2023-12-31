from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from Cafe_feeling_happy.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("dish/", include("dish.urls", namespace="dish")),
    path("order/", include("order.urls", namespace="order")),
    path("user/", include("user.urls", namespace="user")),
    path("accounts/", include("django.contrib.auth.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
