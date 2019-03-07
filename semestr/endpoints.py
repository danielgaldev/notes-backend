from django.urls import include, path
from rest_framework import routers

from . import api

router = routers.DefaultRouter()
router.register(r'semester', api.SemesterAPI)
router.register(r'class', api.ClassAPI)
router.register(r'requirement', api.RequirementAPI)

urlpatterns = [
    path('', include(router.urls))
]