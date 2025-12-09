from django.urls import path
from .views import RegisterView, UserListView, UpdateUserRoleView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/',RegisterView.as_view(),name="home"),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('users/', UserListView.as_view(), name="list_users"),
    path('users/update-role/<int:pk>/', UpdateUserRoleView.as_view(), name="update_role"),
]
