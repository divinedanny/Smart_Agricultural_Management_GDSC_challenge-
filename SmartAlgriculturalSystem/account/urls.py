from django.urls import path
from .views import RegisterationView



urlpatterns = [
    path('register/', RegisterationView.as_view(), name='registration'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
]