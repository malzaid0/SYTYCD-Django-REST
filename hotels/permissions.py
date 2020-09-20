from datetime import date

from rest_framework.permissions import BasePermission


class IsBookedByUser(BasePermission):
    message = "This isn't your booking....."

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        else:
            return False


class IsNotInPast(BasePermission):
    message = "Can't cancel or modify past bookings"

    def has_object_permission(self, request, view, obj):
        if obj.check_in > date.today():
            return True
        else:
            return False
