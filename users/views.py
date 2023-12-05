from rest_framework import generics

from users.models import User
from users.serializers import UserSerializer, FullUserSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = FullUserSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user_id = self.kwargs.get('id')
        if user_id:
            return User.objects.filter(id=user_id)
        else:
            return User.objects.all()
