from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views import generic
from django import forms 
from .models import Post
from django.views.decorators.http import require_http_methods
from django.template import loader

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

#returns list of post based on location  
def location(request):
    location = request.POST['location']
    print("This is the location: "+ location)
    loc_post_list = Post.objects.filter(post_location=location)    
    print("This is post list: "+ str(loc_post_list))
    """Return the posts filtered by location"""
    template = loader.get_template('posts/index.html')
    context = {
        'latest_post_list': loc_post_list,
    }
    return HttpResponse(template.render(context, request))
    
def form(request):
    template = loader.get_template('posts/form.html')
    context = {}
    return HttpResponse(template.render(context,request))

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

def upload(request):
    post_dict = request.POST
    post = Post(post_author=post_dict['post_author'],post_drink=post_dict['post_drink'],post_location = post_dict['post_location'], post_text = post_dict['post_text'])
    result = post.save()
    print (str(result))
    return HttpResponseRedirect(reverse('posts:index'))