from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .forms import PostForm
from .models import Post, Comment
from .filters import PostFilter

class NewsList(ListView):
    model = Post

    ordering = '-date'

    template_name = 'articles.html'

    context_object_name = 'articles'

    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filteset'] = self.filterset
        return context

class SearchNews(ListView):
    model = Post

    ordering = '-date'

    template_name = 'search.html'

    context_object_name = 'search'

    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class CommentList(ListView):
    model = Comment

    ordering = 'date'

    template_name = 'article.html'

    context_object_name = 'comments'

class NewsView(DetailView):
    model = Post

    template_name = 'article.html'

    context_object_name = 'article'


class PostCreateView(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'edit.html'


class PostUpdateView(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'edit.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('post_list')


def create_post(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        post = form.save(commit=False)
        if 'news' in str(request):
            post.position = 'N'
        else:
            post.position = 'A'
        form.save()
        return HttpResponseRedirect('../')

    return render(request, 'edit.html', {'form':form})
