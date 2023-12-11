from rest_framework import serializers
from watchlist_app.models import Movie

#Convert database model objects to python native data type.
class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()
    
    #Create method is responsible for creating new instance of the associated  model
    def create(self, validated_data):
        # print(f"create:: validated_data:: {validated_data}")
        """
        validated_data = {'name': 'Movie4', 'description': 'Description3', 'active': True}
        Movie.objects.create(name='Movie4', description='Description3', active=True)
        """
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance