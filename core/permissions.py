from rest_framework.permissions import BasePermission, SAFE_METHODS
from core.models import TeachingAssignment, Course, Syllabus, CourseLearningOutcome, LOToPOMap


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and (user.is_superuser or user.role == "ADMIN")
    

class IsStudentReadOnly(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.role != "STUDENT":
            return True
        return request.method in SAFE_METHODS


class IsProgramManager(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        
        if user.role == "ADMIN" or user.is_superuser:
            return True
        
        if user.role != "FACULTY":
            return False
        
        return obj.faculty_manager_id == user.id


class IsLecturerOfCourse(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user

        if user.role == "ADMIN" or user.is_superuser:
            return True
        
        if user.role != "LECTURER":
            return False

        if isinstance(obj, Course):
            course = obj
        elif isinstance(obj, Syllabus):
            course = obj.course
        elif isinstance(obj, CourseLearningOutcome):
            course = obj.course
        elif isinstance(obj, LOToPOMap):
            course = obj.lo.course
        else:
            return False

        return TeachingAssignment.objects.filter(course=course, lecturer=user).exists()
