from django.contrib import admin
from django.urls import path, include
from hotdeal.views import index
from rest_framework import routers
import hotdeal.views

router = routers.DefaultRouter()
router.register("deals", hotdeal.views.DealViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('api/', include(router.urls))
]
