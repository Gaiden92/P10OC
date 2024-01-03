from rest_framework import permissions


class isOwner(permissions.BasePermission):
    """A class represent a User himself

    Arguments:
        permissions -- class BasePermission
    """

    def has_object_permission(
            self,
            request: str,
            view: str,
            obj: object
    ) -> bool:
        """Method check if the user is the object's owner

        Arguments:
            request -- the request
            view -- the view
            obj -- the instance

        Returns:
            bool
        """
        return request.user == obj
