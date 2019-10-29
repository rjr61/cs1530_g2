from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import generic

from .models import Post

class IndexView(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the last five published posts."""
        return Post.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'


class ResultsView(generic.DetailView):
    model = Post
    template_name = 'posts/results.html'

def vote(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    try:
        selected_choice = request.POST['vote']
    except (KeyError):
        # Redisplay the question voting form.
        return render(request, 'posts/detail.html', {
            'post': post,
            'error_message': "You didn't select a choice.",
        })
    else:
        if selected_choice == 'upvote':
            post.post_score += 1
            post.save()
        elif selected_choice == 'downvote':
            post.post_score -= 1
            post.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('posts:results', args=(post.id,)))