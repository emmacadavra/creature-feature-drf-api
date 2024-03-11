from rest_framework import generics, permissions
from creature_feature_api.permissions import IsOwnerOrReadOnly
from like_comments.models import LikeComment
from like_comments.serializers import LikeCommentSerializer


class LikeList(generics.ListCreateAPIView):
    """
    Lists all comments likes, enables logged
    in users to create a new comment like.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeCommentSerializer
    queryset = LikeComment.objects.annotate()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieves an individual comment like, enables
    comment like owners to delete it (ie, unlike).
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeCommentSerializer
    queryset = LikeComment.objects.all()
