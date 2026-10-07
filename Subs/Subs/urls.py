from django.contrib import admin
from django.urls import path
from subscribers import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("subscribe/", views.subscribe, name="subscribe"),
]