from django.shortcuts import render, redirect
from django.views import View

from .models import Blog



class BlogView(View):
    template = 'blog_details.html'

    def get(self, request, *args, **kwargs):
        id = kwargs.pop('pk', None)
        if id is None:
            return redirect('/')

        blog = Blog.objects.filter(publish=True, pk=id).first()
        context = {'blog': blog}

        if blog is None:
            return redirect('/')

        return render(request, self.template, context)


class HomeView(View):
    template = 'home.html'

    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.filter(publish=True)
        context = {'blogs':blogs}
        return render(request, self.template, context=context)