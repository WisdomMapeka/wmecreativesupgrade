from rest_framework import serializers
from . models import Photos_collections


class Photos_collectionsSerializers (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photos_collections
        fields = ["name", "uploded", "description", "photographer", "photo"]

