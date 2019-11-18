from rest_framework import serializers
from ..models import Repo


class RepoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repo
        fields = ['id', 'name', 'html_url', 'description', 'private', 'created_at', 'watchers']


class RepoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repo
        fields = ['id', 'name']
