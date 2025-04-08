from rest_framework import serializers

from .models import Company, Vacancy

class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description  = serializers.CharField()
    city = serializers.CharField()
    address = serializers.CharField()

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.city = validated_data.get('city', instance.city)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance
    
    def create(self, validated_data):
        return Company.objects.create(**validated_data)


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'description', 'salary', 'company', 'position')

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'description')
