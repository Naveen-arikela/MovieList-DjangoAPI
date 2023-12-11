from rest_framework import serializers
from watchlist_app.models import Movie

#Validators function
def description_length(value):
    if len(value) < 2:
        raise serializers.ValidationError("Description is too short!")
    
#Convert database model objects to python native data type.
class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField(validators=[description_length])
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
    
    #Field level validation
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short!")
        return value
    
    #Object level validation
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and Description should be different!")
        return data