from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.template.defaultfilters import slugify

# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    if request.method == 'GET':
        post_form = PostForm()
    else:
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.slug = slugify(post.title)
            post.save()
            redirect('/')
        
        
    return render(request, 'board/index.html', {
        'show_board': True,
        'board_posts': posts,
        'form': post_form
    })


def post_details(request, post_slug):
    try:
        selected_post = Post.objects.get(slug=post_slug)
        comments = Comment.objects.filter(post=selected_post)
        
        if request.method == 'GET':            
            comment_form = CommentForm()
        else:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = selected_post
                comment.save()
        
        return render(request, 'board/post-details.html', {
			'post_found': True,
			'post': selected_post,
			'comments': comments,
			'form': comment_form
		})
    except Exception as exc:
        '''
                        Create a 404 page
        '''
        print(exc)
        return render(request, 'board/post-details.html', {
            'post_found': False
        })
