from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from users.models import PassUser
from .models import Coords, Level, Images, Pereval
from users.serializers import PassUserSerializer

class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ('latitude', 'longitude', 'height',)

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('winter', 'summer', 'autumn', 'spring',)

class ImagesSerializer(serializers.ModelSerializer):
    data = serializers.URLField()
    
    class Meta:
        model = Images
        fields = ('data', 'title')

class PerevalSerializer(WritableNestedModelSerializer):
    add_time = serializers.DateTimeField(format="&d-&m-&Y &H:&M:&S", read_only=True)
    status = serializers.CharField(read_only=True)
    level = LevelSerializer(allow_null=True)
    user = PassUserSerializer()
    coords = CoordsSerializer()
    images = ImagesSerializer(many=True)

    class Meta:
        model = Pereval
        fields = (
            'user', 'beauty_title', 'title', 'other_titles', 'connect', 'coords', 'level', 'images', 'add_time', 'status')

    def validate_beauty_title(self, value):
        if Pereval.objects.filter(beauty_title=value).exists():
            raise serializers.ValidationError("Название препятствия должно быть уникальным.")
        return value

    def validate_title(self, value):
        if Pereval.objects.filter(title=value).exists():
            raise serializers.ValidationError("Название вершины должно быть уникальным.")
        return value