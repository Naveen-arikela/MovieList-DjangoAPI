from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform

#Convert database model objects to python native data type.

#  ╔══════════════════════════════════╗
# ║        ⚙ Model Serializer ⚙       ║
#  ╚══════════════════════════════════╝

class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = "__all__"


    """
    len_name = serializers.SerializerMethodField()
    #new field added in the response
    class Meta:
        model = WatchList
        fields  = '__all__'
        # fields = ['id', 'name', 'description']
        # exclude = ['active']
        # NOTE:: We should not use both at a time exclude and fields
    
    def get_len_name(self, object):
        return len(object.name)

    #Field level validation
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short!")
        return value
    
    #Object level validation
    def validate(self, data):
        if data['title'] == data['storyline']:
            raise serializers.ValidationError("Title and Description should be different!")
        return data
    """

#  ╔══════════════════════════════════╗
# ║        ⚙ Serializer ⚙             ║
#  ╚══════════════════════════════════╝

"""
#Validators function
def description_length(value):
    if len(value) < 2:
        raise serializers.ValidationError("Description is too short!")
class WatchListSerializer_Serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField(validators=[description_length])
    active = serializers.BooleanField()
    
    #Create method is responsible for creating new instance of the associated  model
    def create(self, validated_data):
        # print(f"create:: validated_data:: {validated_data}")
        
        #validated_data = {'name': 'WatchList4', 'description': 'Description3', 'active': True}
        # WatchList.objects.create(name='WatchList4', description='Description3', active=True)
        
        return WatchList.objects.create(**validated_data)

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
"""