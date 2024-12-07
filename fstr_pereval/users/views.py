from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import PassUser
from .serializers import PassUserSerializer

class PassUserViewSet(viewsets.ModelViewSet):
    queryset = PassUser.objects.all()
    serializer_class = PassUserSerializer

    @action(detail=False, methods=['get'])
    def my_objects(self, request):
        user_email = request.user.email
        user_objects = self.queryset.filter(email=user_email)
        serializer = self.get_serializer(user_objects, many=True)
        return Response(serializer.data)
