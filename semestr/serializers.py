from rest_framework import serializers

from .models import Semester, Class, Requirement


class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = '__all__'


class ClassSerializer(serializers.ModelSerializer):
    requirements = RequirementSerializer(many=True)
    
    class Meta:
        model = Class
        fields = '__all__'


class SemesterSerializer(serializers.ModelSerializer):
    classes = ClassSerializer(many=True)

    class Meta:
        model = Semester
        fields = '__all__'
