from rest_framework import viewsets
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


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.UserSerializer

    def get_object(self):
        return self.request.user
