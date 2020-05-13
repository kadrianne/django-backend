from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', views.UserView) # This is the url route /users
router.register('restaurants', views.RestaurantView)

urlpatterns = [
    path('', include(router.urls))
]