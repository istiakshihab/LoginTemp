
from django.contrib import admin
from django.urls import path, include
from others import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('profile/', views.profile, name='profile'),
]
