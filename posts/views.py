from django.db.models import Count, Case, When, IntegerField
from django.db.models.functions import Coalesce
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from creature_feature_api.permissions import IsOwnerOrReadOnly
from posts.models import Post
from posts.serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    # ADD DOCSTRING
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
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
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    ordering_fields = [
        'reactions_count',
        'comments_count',
        'crown_count',
        'good_count',
        'love_count',
        'reactions__created_on',
    ]
    search_fields = [
        'owner__username',
        'title',
        'category',
    ]
    filterset_fields = [
        'owner__profile',
        'owner__followed__owner__profile',
        'reactions__owner__profile',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # ADD DOCSTRING
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        reactions_count=Count('reactions', distinct=True),
        comments_count=Count('comment', distinct=True),
    ).order_by('-created_on')


class CategoryList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
