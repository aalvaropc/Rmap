from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'confirm_password', 'first_name', 'last_name', 'age', 'gender')
        extra_kwargs = {
            'password': {'write_only': True},
            'confirm_password': {'write_only': True},
            'age': {'required': True},
            'gender': {'required': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        confirm_password = validated_data.pop('confirm_password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password and confirm_password and password == confirm_password:
            instance.set_password(password)
        instance.save()
        return instance