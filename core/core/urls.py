from django.contrib import admin
from django.urls import path, include

from user.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/', include('api.urls')),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('accounts/', include('allauth.urls')),

    path('auth/', include('rest_auth.urls'))
]
