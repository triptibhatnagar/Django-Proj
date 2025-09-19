from django.urls import reverse_lazy
from django.db.models import F


from .models import Blog, BlogView




class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'
    ordering = ['-created_at']
    paginate_by = 10




class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'


    def get(self, request, *args, **kwargs):
# call the superclass to ensure self.object is set
        response = super().get(request, *args, **kwargs)
        blog = self.get_object()
        user = request.user


# Only count views from authenticated users (members). If you prefer sessions/anonymous, see extras.
        if user.is_authenticated:
# create BlogView only if it doesn't already exist for (blog, user)
            if not BlogView.objects.filter(blog=blog, user=user).exists():
                BlogView.objects.create(blog=blog, user=user)
# atomic increment of cached counter
        Blog.objects.filter(pk=blog.pk).update(views_count=F('views_count') + 1)
        return response




class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['title', 'content']
    template_name = 'blog/blog_form.html'


    def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)




class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    fields = ['title', 'content']
    template_name = 'blog/blog_form.html'


def test_func(self):
    blog = self.get_object()
    return self.request.user == blog.author




class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    return self.request.user == blog.author