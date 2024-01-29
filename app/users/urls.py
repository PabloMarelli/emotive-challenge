from django.urls import path
from . import views 

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('test_token/', views.test_token, name='test-token'),
    path('profile/', views.get_profile, name='get-profile'),
]
