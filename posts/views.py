from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from creature_feature_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    # ADD DOCSTRING
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        reactions_count=Count('reactions', distinct=True),
        comments_count=Count('comment', distinct=True),
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
