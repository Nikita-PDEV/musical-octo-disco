from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Coords, Level, Images, Pereval
from .serializers import CoordsSerializer, LevelSerializer, ImagesSerializer, PerevalSerializer

class CoordsViewSet(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer

class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer

class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer

def retrieve(self, request, pk=None):
        try:
            pereval_instance = self.get_object()
            serializer = self.get_serializer(pereval_instance)
            return Response(serializer.data)
        except Pereval.DoesNotExist:
            return Response({'message': 'Объект не найден.'}, status=status.HTTP_404_NOT_FOUND)

def partial_update(self, request, pk=None):
        try:
            pereval_instance = self.get_object()
            if pereval_instance.status != Pereval.new:  # Проверка статуса
                return Response({'state': 0, 'message': 'Редактирование возможно только для объектов со статусом "новый".'}, 
                                status=status.HTTP_400_BAD_REQUEST)

            # Проверка запрещенных полей для редактирования
            for field in ['user', 'coords', 'images']:
                if field in request.data:
                    return Response({'state': 0, 'message': f'Редактирование поля "{field}" запрещено.'}, 
                                    status=status.HTTP_400_BAD_REQUEST)

            serializer = self.get_serializer(pereval_instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'state': 1, 'message': 'Запись успешно обновлена.'})
            return Response({'state': 0, 'message': 'Ошибка валидации.'}, 
                            status=status.HTTP_400_BAD_REQUEST)
        except Pereval.DoesNotExist:
            return Response({'state': 0, 'message': 'Объект не найден.'}, status=status.HTTP_404_NOT_FOUND)

def list(self, request):
        email = request.query_params.get('user__email', None)
        if email is not None:
            user_objects = self.queryset.filter(user__email=email)
            serializer = self.get_serializer(user_objects, many=True)
            return Response(serializer.data)
        return Response({'message': 'Email не задан.'}, status=status.HTTP_400_BAD_REQUEST)