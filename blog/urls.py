from . import views
from django.urls import path

urlpatterns = [
    path("", views.post_index, name="post_index"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
]