from django.db.models import Count, Case, When, IntegerField
from django.db.models.functions import Coalesce
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from creature_feature_api.permissions import IsOwnerOrReadOnly
from posts.models import Post
from posts.serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """
    Lists all posts, enables logged in users to create new posts.
    Also enables filtering posts and handles the post reactions.
    The 'perform_create' method associates a post with a logged in User.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        reactions_count=Count('reactions', distinct=True),
        comments_count=Count('comment', distinct=True),
        crown_count=Coalesce(Count(Case(
            When(reactions__reaction='CROWN', then=1),
            output_field=IntegerField(),
        ), distinct=True), 0),
        good_count=Coalesce(Count(Case(
            When(reactions__reaction='GOOD', then=1),
            output_field=IntegerField(),
        ), distinct=True), 0),
        love_count=Coalesce(Count(Case(
            When(reactions__reaction='LOVE', then=1),
            output_field=IntegerField(),
        ), distinct=True), 0),
    ).order_by('-created_on')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    ordering_fields = [
        'reactions_count',
        'comments_count',
        'reactions__created_on',
    ]
    search_fields = [
        'owner__username',
        'title',
        'category',
    ]
    filterset_fields = [
        'category',
        'owner__profile',
        'owner__followed__owner__profile',
        'reactions__owner__profile',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves an individual post by ID, enables post
    owners to edit or delete the post.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        reactions_count=Count('reactions', distinct=True),
        comments_count=Count('comment', distinct=True),
        crown_count=Coalesce(Count(Case(
            When(reactions__reaction='CROWN', then=1),
            output_field=IntegerField(),
        )), 0),
        good_count=Coalesce(Count(Case(
            When(reactions__reaction='GOOD', then=1),
            output_field=IntegerField(),
        )), 0),
        love_count=Coalesce(Count(Case(
            When(reactions__reaction='LOVE', then=1),
            output_field=IntegerField(),
        )), 0),
    ).order_by('-created_on')
