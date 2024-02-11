from rest_framework import serializers
from comments.models import Comment
from like_comments.models import LikeComment


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()

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

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'post', 'content', 'profile_id',
            'profile_image', 'like_id', 'created_on', 'updated_on',
        ]


class CommentDetailSerializer(CommentSerializer):
    post = serializers.ReadOnlyField(source='post.id')
