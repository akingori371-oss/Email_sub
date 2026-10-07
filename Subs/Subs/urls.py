from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from subscribers import views

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="subscribe"), name="home"),
    # path("admin/", admin.site.urls),
    path("subscribe/", views.subscribe, name="subscribe"),
]