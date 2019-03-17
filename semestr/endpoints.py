from django.urls import include, path
from rest_framework_nested import routers

from . import api

router = routers.SimpleRouter()
router.register(r'semesters', api.SemesterAPI, base_name='semesters')
semesters_router = routers.NestedSimpleRouter(router, r'semesters', lookup='semester')
semesters_router.register(r'classes', api.ClassAPI, base_name='semester-classes')
classes_router = routers.NestedSimpleRouter(semesters_router, r'classes', lookup='class')
classes_router.register(r'requirements', api.RequirementAPI, base_name='class-requirements')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(semesters_router.urls)),
    path('', include(classes_router.urls)),
    path('auth/register/', api.RegistrationAPI.as_view(), name='register'),
    path('auth/login/', api.LoginAPI.as_view(), name='login'),
    path('auth/user/', api.UserAPI.as_view(), name='user')
]