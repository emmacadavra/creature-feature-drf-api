from django.db import IntegrityError
from rest_framework import serializers
from .models import Reaction, Reactions


class ReactionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Reaction
        fields = [
            'id', 'owner', 'created_on', 'post'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
