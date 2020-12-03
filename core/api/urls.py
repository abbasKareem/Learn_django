from rest_framework import routers
from django.urls import path, include
from .views import Index, IndexDetails, IndexListGenerics


# router = routers.DefaultRouter()
# router.register('', views.Index)


urlpatterns = [
    # path('products/', include(router.urls)),
    path('products/', Index.as_view()),
    path('products/<int:pk>/', IndexDetails.as_view()),
    path('generics/list/', IndexListGenerics.as_view()),
    path('generics/list/<int:id>', IndexListGenerics.as_view()),

    

]
