from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import generic
from django import forms 
from .models import Post
from django.views.decorators.http import require_http_methods

class IndexView(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the last five published posts."""
        return Post.objects.order_by('-pub_date')[:5]

class TrendingView(generic.ListView,):
    template_name = 'posts/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the last five published posts."""
        return Post.objects.order_by('-post_score')[:5]

@require_http_methods(["GET", "POST"])
class LocationView(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'latest_post_list'
    
    def get_queryset(self,request):
        location = request.POST['location']
        """Return the last five published posts."""
        return Post.objects.filter(post_location=location)

##Well come back to dis guy 
#def location(request):
#    def get_queryset(self,request):
 #       location = request.POST['location']
 #       """Return the last five published posts."""
 #       return HttpResponseRedirect(reverse('posts:view_location'),args=location)
        


class DetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'


class ResultsView(generic.DetailView):
    model = Post
    template_name = 'posts/results.html'

def vote(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.post_score += 1
    post.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('posts:index'))

def down_vote(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.post_score -= 1
    post.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('posts:index'))