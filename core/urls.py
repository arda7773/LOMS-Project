from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views import (
    ProgramViewSet, CourseViewSet, ProgramOutcomeViewSet,
    CourseLearningOutcomeViewSet, SyllabusViewSet, LOToPOMapViewSet
)

router = DefaultRouter()
router.register("programs", ProgramViewSet)
router.register("courses", CourseViewSet)
router.register("po", ProgramOutcomeViewSet)
router.register("lo", CourseLearningOutcomeViewSet)
router.register("syllabus", SyllabusViewSet)
router.register("mapping", LOToPOMapViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
