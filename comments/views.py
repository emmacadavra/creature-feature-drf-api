from rest_framework import generics, permissions
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from creature_feature_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer
from rest_framework.pagination import PageNumberPagination


class CommentsSetPagination(PageNumberPagination):
    """
    Custom pagination class for comments, overriding the global default of 10.
    """
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000


class CommentList(generics.ListCreateAPIView):
    """
    Lists all comments, enables logged in users to create comments.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = CommentsSetPagination
    queryset = Comment.objects.annotate(
        likes_count=Count('likes', distinct=True)
    ).order_by('-created_on')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves an individual comment by id,
    enables comment owners to edit or delete.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.annotate(
        likes_count=Count('likes', distinct=True)
    ).order_by('-created_on')
