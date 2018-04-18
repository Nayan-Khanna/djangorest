from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    '''A custom permission to only only the owners of n=an object to edit it.'''

    def has_object_permission(self, request, view, obj):
        '''
        As read permissions are allowed to any request,
        So we will always allow GET, HEAD or OPTIONS requests. '''
        if request.method in permissions.SAFE_METHODS:
            return True

        ''' Write permissions only to owner of snippet. '''
        return obj.owner == request.user
