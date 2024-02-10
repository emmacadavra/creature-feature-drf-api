from rest_framework import generics, permissions
from creature_feature_api.permissions import IsOwnerOrReadOnly
from .models import Reaction, Reactions
from .serializers import ReactionSerializer


class ReactionList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ReactionSerializer
    queryset = Reaction.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReactionDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReactionSerializer
    queryset = Reaction.objects.all()
