from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from comments.models import Comment
from like_comments.models import LikeComment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model. Adds additional fields when returning
    a list of Comment instances and links Comments to LikeComment.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    created_on = serializers.SerializerMethodField()
    updated_on = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = LikeComment.objects.filter(
                owner=user, comment=obj
            ).first()
            return like.id if like else None
        return None

    def get_created_on(self, obj):
        return naturaltime(obj.created_on)

    def get_updated_on(self, obj):
        return naturaltime(obj.updated_on)

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'post', 'content', 'profile_id',
            'profile_image', 'like_id', 'likes_count', 'created_on',
            'updated_on',
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model's detail view. Post is set as a
    read only field so that it doesn't have to be set on each update.
    """
    post = serializers.ReadOnlyField(source='post.id')
