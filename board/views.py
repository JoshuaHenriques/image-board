from django.shortcuts import render
from .models import Post

# Create your views here.


def index(request):
    posts = Post.objects.all().order_by('created_at')
    return render(request, 'board/index.html', {
        'show_board': True,
        'board_posts': posts
    })


def post_details(request, post_slug):
    try:
        selected_post = Post.objects.get(slug=post_slug)
        comments = selected_post.comments.all()
        return render(request, 'board/post-details.html', {
            'post_found': True,
            'post': selected_post,
            'comments': comments
        })
    except Exception as exc:
        '''
			Create a 404 page
        '''
        return render(request, 'board/post-details.html', {
			'post_found': False
		})
