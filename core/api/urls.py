from rest_framework import routers
from django.urls import path, include
from .views import Index, IndexDetails


# router = routers.DefaultRouter()
# router.register('', views.Index)


urlpatterns = [
    # path('products/', include(router.urls)),
    path('products/', Index.as_view()),
    path('products/<int:pk>/', IndexDetails.as_view()),

]
