from rest_framework import generics
from ..models import Repo
from .serializers import RepoSerializer, RepoListSerializer


class RepoListView(generics.ListAPIView):
    queryset = Repo.objects.all()
    serializer_class = RepoListSerializer


class RepoDetailView(generics.RetrieveAPIView):
    queryset = Repo.objects.all()
    serializer_class = RepoSerializer
