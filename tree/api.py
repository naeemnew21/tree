from rest_framework.generics import UpdateAPIView, CreateAPIView
from rest_framework.permissions import BasePermission
from .serializers import BranchUpdateSerializer, BranchCreateSerializer, FamilyBranchCreateSerializer, FamilyBranchUpdateSerializer
from .models import Person


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False


class CreateBranch(CreateAPIView):
    serializer_class   = BranchCreateSerializer
    permission_classes = [IsAdmin]


class BranchUpdate(UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class   = BranchUpdateSerializer
    permission_classes = [IsAdmin]


class CreateFamilyBranch(CreateAPIView):
    serializer_class   = FamilyBranchCreateSerializer
    permission_classes = [IsAdmin]


class FamilyBranchUpdate(UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class   = FamilyBranchUpdateSerializer
    permission_classes = [IsAdmin]
