from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import CommentForm, PostForm, UpdatePostForm
from django.contrib import messages

# Create your views here.


def main_page(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'mainApp/mainPage.html', context)


def about_page(request):
    return render(request, 'mainApp/aboutPage.html', {'title': 'About'})


@login_required
def create_post_page(request):
    new_post = None
    if request.method == 'POST':
        post_form = PostForm(data=request.POST)
        if post_form.is_valid:
            new_post = post_form.save(commit=False)
            new_post.author = request.user
            new_post.slug = new_post.title
            post_form.save()
            messages.success(request, 'Post created successfuly')
            return redirect("mainApp:mainpage")
    else:
        post_form = PostForm()

    return render(request, 'mainApp/postCreatePage.html', {'post_form': post_form})


@login_required
def update_post_page(request, post):
    old_post = get_object_or_404(Post, slug=post)
    updated_post = None
    if request.user == old_post.author:
        if request.method == 'POST':
            update_post_form = UpdatePostForm(data=request.POST)
            if update_post_form.is_valid:
                updated_post = update_post_form.save(commit=False)
                old_post.title = updated_post.title
                old_post.content = updated_post.content
                old_post.save()
                messages.success(request, 'Post Updated successfuly')
                return redirect("mainApp:mainpage")
        else:
            update_post_form = UpdatePostForm()
    else:
        messages.error(request, 'You cannot update this Post ')
        return redirect("mainApp:mainpage")

    context = {'old_post': old_post, 'updated_post': updated_post,
               'update_post_form': update_post_form}

    return render(request, 'mainApp/postUpdatePage.html', context)


@login_required
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
            messages.success(request, 'comment posted successfuly')
            return redirect(request.path)
    else:
        comment_form = CommentForm()
    context = {'post': post, 'comments': comments,
               'new_comment': new_comment, 'comment_form': comment_form}

    return render(request, 'mainApp/postdetailPage.html', context)


@login_required
def delete_post_page(request, post):
    old_post = get_object_or_404(Post, slug=post)
    if request.user == old_post.author:
        old_post.delete()
        messages.success(request, 'Post Deleted successfuly')
        return redirect("mainApp:mainpage")
    else:
        messages.error(request, 'You cannot delete this Post ')
        return redirect("mainApp:mainpage")

    context = {'old_post': old_post}

    return render(request, 'mainApp/postUpdatePage.html', context)
