from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('trending/', views.TrendingView.as_view(), name='trends'),
    path('location/', views.LocationView.as_view(), name='location'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:post_id>/vote/', views.vote, name='vote'),
    path('<int:post_id>/down-vote/', views.down_vote, name='down_vote'),
]