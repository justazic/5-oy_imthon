from django.urls import path 
from .views import RegisterView,LoginView,LogoutView,ProfileView,ChangePaswordView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('pasword/change/', ChangePaswordView.as_view(), name='change_password'),
]