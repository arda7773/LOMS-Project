from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

from core.models import *
from core.serializers import *
from core.permissions import (
    IsStudentReadOnly,
    IsProgramManager,
    IsLecturerOfCourse
)


class ProgramViewSet(ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [IsAuthenticated, IsStudentReadOnly]

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsProgramManager()]
        return super().get_permissions()


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsStudentReadOnly]

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsProgramManager()]
        return super().get_permissions()


class ProgramOutcomeViewSet(ModelViewSet):
    queryset = ProgramOutcome.objects.all()
    serializer_class = ProgramOutcomeSerializer
    permission_classes = [IsAuthenticated, IsStudentReadOnly]

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsProgramManager()]
        return super().get_permissions()


class CourseLearningOutcomeViewSet(ModelViewSet):
    queryset = CourseLearningOutcome.objects.all()
    serializer_class = CourseLearningOutcomeSerializer
    permission_classes = [IsAuthenticated, IsStudentReadOnly]

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsLecturerOfCourse()]
        return super().get_permissions()


class SyllabusViewSet(ModelViewSet):
    queryset = Syllabus.objects.all()
    serializer_class = SyllabusSerializer
    permission_classes = [IsAuthenticated, IsStudentReadOnly]
    parser_classes = [MultiPartParser, FormParser]

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsLecturerOfCourse()]
        return super().get_permissions()


class LOToPOMapViewSet(ModelViewSet):
    queryset = LOToPOMap.objects.all()
    serializer_class = LOToPOMapSerializer
    permission_classes = [IsAuthenticated, IsStudentReadOnly]

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsLecturerOfCourse()]
        return super().get_permissions()
