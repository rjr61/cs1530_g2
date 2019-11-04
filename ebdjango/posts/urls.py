from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'posts'
urlpatterns = [
    path('', login_required(views.IndexView.as_view(), login_url='login/'), name='index'),
    path('trending/', views.TrendingView.as_view(), name='trends'),
    path('location/', views.location, name='location'),
    path('form/', views.form, name='form'),
    path('upload/', views.upload, name='upload'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:post_id>/vote/', views.vote, name='vote'),
    path('<int:post_id>/down-vote/', views.down_vote, name='down_vote'),
]