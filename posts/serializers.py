from rest_framework import serializers
from posts.models import Post
from reactions.models import Reaction


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    current_user_reaction = serializers.SerializerMethodField()
    reactions_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    crown_count = serializers.ReadOnlyField()
    good_count = serializers.ReadOnlyField()
    love_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image exceeds maximum file size (2MB)'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image exceeds maximum width (4096px)'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image exceeds maximum height (4096px)'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_current_user_reaction(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            reaction = Reaction.objects.filter(
                owner=user, post=obj
            ).first()

            if not reaction:
                return None

            return {
                "reaction_id": reaction.id,
                "reaction type": reaction.reaction
            }
            # return reaction.id if reaction else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'title', 'excerpt', 'content', 'image', 'image_filter',
            'category', 'status', 'current_user_reaction', 'reactions_count',
            'comments_count', 'crown_count', 'good_count', 'love_count',
            'created_on', 'updated_on',
        ]
