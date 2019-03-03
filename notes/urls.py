from rest_framework import routers
from django.urls import path, include

from .views import NoteViewSet, RegistrationAPI, UserAPI, LoginAPI

router = routers.SimpleRouter()

router.register(r'', NoteViewSet, 'notes')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', RegistrationAPI.as_view()),
    path('auth/login/', LoginAPI.as_view()),
    path('auth/user/', UserAPI.as_view())
]
