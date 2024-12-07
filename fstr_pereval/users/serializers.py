from rest_framework import serializers
from .models import PassUser

class PassUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassUser
        fields = ('email', 'phone_number', 'firstname', 'lastname', 'surname', 'status')

    def update(self, instance, validated_data):
        # Запрет редактирования, если статус не 'new'
        if instance.status != 'new':
            raise serializers.ValidationError("Редактирование доступно только для объектов со статусом 'new'.")

        # Поля, которые нельзя редактировать
        for field in ['email', 'phone_number']:
            if field in validated_data:
                raise serializers.ValidationError(f"Редактирование поля '{field}' запрещено.")

        # Обновление остальных полей
        instance.firstname = validated_data.get('firstname', instance.firstname)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.save()
        return instance