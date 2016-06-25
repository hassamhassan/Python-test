from rest_framework import serializers
from models import Provider, ServiceArea


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ('name', 'email', 'phone_number', 'language', 'currency')

    def to_representation(self, instance):
        return_dict = {
            "name": instance.name,
            'email': instance.email,
            'phone_number': instance.phone_number,
            'language': instance.language,
            'currency': instance.currency,
        }
        return return_dict

    def create(self, validated_data):
        """
            Create and return a new Provider instance, given the validated data.
        """
        return Provider.objects.create(**validated_data)


class ServiceAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceArea
        fields = ('name', 'price', 'polygon', 'provider')

    def to_representation(self, instance):
        return_dict = {
            "name": instance.name,
            'price': instance.price,
            'polygon': instance.polygon,
            'provider': instance.provider.name,
        }
        return return_dict

    def create(self, validated_data):
        """
            Create and return a new ServiceArea instance, given the validated data.
        """
        return ServiceArea.objects.create(**validated_data)