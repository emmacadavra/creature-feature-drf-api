from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    # ADD DOCSTRING
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    created_on = serializers.SerializerMethodField()
    updated_on = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_on(self, obj):
        return naturaltime(obj.created_on)

    def get_updated_on(self, obj):
        return naturaltime(obj.updated_on)

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'post', 'content', 'profile_id',
            'profile_image', 'like_id', 'created_on', 'updated_on',
        ]


class CommentDetailSerializer(CommentSerializer):
    # ADD DOCSTRING
    post = serializers.ReadOnlyField(source='post.id')
