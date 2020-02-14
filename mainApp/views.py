from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm
# Create your views here.


def main_page(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'mainApp/mainPage.html', context)


def about_page(request):
    return render(request, 'mainApp/aboutPage.html', {'title': 'About'})


def post_detail_page(request, post):
    post = get_object_or_404(Post, slug=post)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect(request.path)
    else:
        comment_form = CommentForm()
    context = {'post': post, 'comments': comments,
               'new_comment': new_comment, 'comment_form': comment_form}

    return render(request, 'mainApp/postdetailPage.html', context)
