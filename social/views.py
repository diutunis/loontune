
from django.shortcuts import render

from django.views import View
from .models import Post, UserProfile
from .forms import PostForm


class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm()
    

        context = {
            'post_list':posts,
            'form': form,
        
        }

        return render(request, 'social/post_list.html', context)  


    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

        context = {
            'post_list':posts,
            'form': form,
        
        }

        return render(request, 'social/post_list.html', context)

class PostDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        context = {
            'post': post
        }

        return render(request, 'social/post_detail.html', context)

class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        posts = Post.objects.filter(author=user).order_by('-created_on')

        context = {
            'user': user,
            'profile': profile,
            'posts':posts
            
            }
        
        return render(request, 'social/profile.html', context)





