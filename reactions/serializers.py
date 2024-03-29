from django.db import IntegrityError
from rest_framework import serializers
from .models import Reaction


class ReactionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Reaction model. The 'create' method
    handles the unique constraint on 'owner' and 'comment'.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Reaction
        fields = [
            'id', 'owner', 'post', 'reaction', 'created_on',
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
