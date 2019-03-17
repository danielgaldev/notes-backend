from rest_framework import viewsets
from knox.models import AuthToken
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response

from . import models
from . import serializers


class SemesterAPI(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return self.request.user.semesters.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if (hasattr(self, 'action')):
            if self.action == 'retrieve':
                return serializers.SemesterDetailSerializer
        return serializers.SemesterSerializer
    

class ClassAPI(viewsets.ModelViewSet):
    queryset = models.Class.objects.all()
    serializer_class = serializers.ClassSerializer


class RequirementAPI(viewsets.ModelViewSet):
    queryset = models.Requirement.objects.all()
    serializer_class = serializers.RequirementSerializer


#########################
#         AUTH          #
#########################


class RegistrationAPI(generics.GenericAPIView):
    serializer_class = serializers.CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": serializers.UserSerializer(
                user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)
        })


class LoginAPI(generics.GenericAPIView):
    serializer_class = serializers.LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": serializers.UserSerializer(
                user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)
        })


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.UserSerializer

    def get_object(self):
        return self.request.user
