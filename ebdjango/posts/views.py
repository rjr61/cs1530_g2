from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.views import generic
from django import forms 
from .models import Post, Likers
from django.views.decorators.http import require_http_methods
from django.template import loader
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Post.objects.filter(pub_date__lte=timezone.now()).prefetch_related('likes').order_by('-pub_date')[:5]

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
    like = Likers.objects.filter(post=post,like_author=request.POST['username'])
    vals = like.values_list('val',flat=True)
    #print(vals[0])
    if not like :
        post.post_score += 1
        post.save()
        like = Likers(
            post = post,
            like_author = request.POST['username'],
            val = True
        )
        like.save()
    elif not vals[0]:
        like = get_object_or_404(like)
        print(like)
        post.post_score += 1
        post.save()
        like.val = True
        like.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('posts:index'))

def down_vote(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    like = Likers.objects.filter(post=post,like_author=request.POST['username'])
    vals = like.values_list('val',flat=True)
    #print(vals[0])
    if not like :
        post.post_score -= 1
        post.save()
        like = Likers(
            post = post,
            like_author = request.POST['username'],
            val = False
        )
        like.save()
    elif vals[0]:
        like = get_object_or_404(like)
        print(like)
        post.post_score -= 1
        post.save()
        like.val = False
        like.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('posts:index'))

def upload(request):
    post_dict = request.POST
    post = Post(
        post_author=post_dict['post_author'],
        post_drink=post_dict['post_drink'],
        post_location = post_dict['post_location'],
        post_text = post_dict['post_text'],
        drink_type = post_dict['drink_type'],
        post_url = 'posts/' + post_dict['drink_type'] + '.png'
    )
    result = post.save()
    print (str(result))
    return HttpResponseRedirect(reverse('posts:index'))

def locations(request):
            if request.GET.get('q'):
                q = request.GET['q']
                data = Post.objects.filter(post_location__startswith=q).values_list('post_location',flat=True)
                json = list(data)
                return JsonResponse(json, safe=False)
            else:
                HttpResponse("Did not work")

def drink_type(request):
    drink_type = request.POST['options']
    print("This is the drinktype: "+ drink_type)
    loc_post_list = Post.objects.filter(drink_type=drink_type)    
    print("This is post list: "+ str(loc_post_list))
    """Return the posts filtered by location"""
    template = loader.get_template('posts/index.html')
    context = {
        'latest_post_list': loc_post_list,
    }
    return HttpResponse(template.render(context, request))