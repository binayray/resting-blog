"""Api File for presentation."""

from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from .models import Blog
from .forms import BlogForm


class BlogView(TemplateView):
    """List all presentation, or create a new user."""

    template_name = 'all_presentations.html'

    def render_to_response(self, context, **response_kwargs):
        """Render method for the view."""
        context['entries'] = Blog.objects.all()
        response_kwargs.setdefault('content_type', self.content_type)
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            **response_kwargs
        )


class NewBlogView(TemplateView):
    """List all presentation, or create a new user."""

    template_name = 'add_new_blog.html'

    def render_to_response(self, context, **response_kwargs):
        """Render method for the view."""
        context['form'] = BlogForm()
        response_kwargs.setdefault('content_type', self.content_type)
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            **response_kwargs
        )


def get_blog_summary(request):
    """Get the summary of ppt over the modal."""
    pk = request.GET.get('pk', None)
    p = Blog.objects.filter(id=pk)
    ctx = {
        'blog': p
    }
    return render_to_response('blog_detail.html', ctx)