from rest_framework import serializers
from core.models import (
    Program, Course, ProgramOutcome,
    CourseLearningOutcome, LOToPOMap,
    Syllabus, TeachingAssignment, Enrollment
)


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class ProgramOutcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramOutcome
        fields = "__all__"


class CourseLearningOutcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseLearningOutcome
        fields = "__all__"


class LOToPOMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = LOToPOMap
        fields = "__all__"


class SyllabusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Syllabus
        fields = "__all__"


class TeachingAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachingAssignment
        fields = "__all__"


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = "__all__"
