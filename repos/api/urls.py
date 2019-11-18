from django.urls import path
from . import views

app_name = 'repos'
urlpatterns = [
    path('repos/', views.RepoListView.as_view(), name='repo_list'),
    path('repos/<pk>/', views.RepoDetailView().as_view(), name='repo_detail'),
]
