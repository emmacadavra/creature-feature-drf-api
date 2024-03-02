from rest_framework import generics, permissions
from creature_feature_api.permissions import IsOwnerOrReadOnly
from like_comments.models import LikeComment
from like_comments.serializers import LikeCommentSerializer


class LikeList(generics.ListCreateAPIView):
    # ADD DOCSTRING
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeCommentSerializer
    queryset = LikeComment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    # ADD DOCSTRING
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeCommentSerializer
    queryset = LikeComment.objects.all()
