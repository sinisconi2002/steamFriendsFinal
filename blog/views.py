from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from blog.models import Post


# Create your views here.
def allposts(request):
    context = {
        'posts': Post.objects.all(),
    }
    return HttpResponse(render(request, 'AllPost.html', context))


class PostDetailView(DetailView):
    model = Post
    template_name = 'BlogPostPage.html'


class PostCreation(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image']
    template_name = 'AddNewPost.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image']
    template_name = 'UpdatePost.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog/allposts'
    template_name = "DeletePost.html"
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False