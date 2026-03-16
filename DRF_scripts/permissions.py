# DRF Permission Scripts

from rest_framework import permissions
from datetime import datetime

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Use Case: Social Media Posts, Comments, Reviews.
    Logic: Anyone can read, but only the creator can edit/delete.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Use Case: Configuration Settings, Admin Logs.
    Logic: Anyone can read, but only Admins can write.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class IsVerifiedUser(permissions.BasePermission):
    """
    Use Case: Posting Comments, Making Transactions.
    Logic: Only users with verified emails can perform actions.
    Note: Requires a 'is_verified' field on your User model.
    """
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            # Check if user has a specific attribute
            return getattr(request.user, 'is_verified', False)
        return False

class BusinessHoursOnly(permissions.BasePermission):
    """
    Use Case: Trading APIs, Support Tickets.
    Logic: Actions only allowed during specific hours (e.g., 9 AM - 5 PM).
    Note: This is a Permission, not Authentication. User must still be logged in.
    """
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            current_hour = datetime.now().hour
            # Allow between 9 AM (9) and 5 PM (17)
            return 9 <= current_hour < 17
        return False

class IsStaffOrTargetUser(permissions.BasePermission):
    """
    Use Case: User Profiles.
    Logic: Users can edit their own profile, Staff can edit anyone's.
    """
    def has_object_permission(self, request, view, obj):
        # Staff can do anything
        if request.user and request.user.is_staff:
            return True
        # Users can only edit themselves
        return obj == request.user

class HasPaidSubscription(permissions.BasePermission):
    """
    Use Case: Premium Content, Advanced Features.
    Logic: Only users with an active subscription can access.
    Note: Requires a related Profile or Subscription model.
    """
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            # Example check: request.user.profile.has_subscription
            return getattr(request.user, 'has_paid_subscription', False)
        return False