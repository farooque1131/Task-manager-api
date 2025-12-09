from django.urls import path, include
from .views import TaskLC, TaskRUD
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path("add/",TaskLC.as_view(),name="add"),
    path("retrive/<int:pk>",TaskRUD.as_view(),name="retrive")
]
