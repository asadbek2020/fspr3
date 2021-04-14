from django.db.models import Q
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from books.forms import BookModelForm, CategoryModelForm
from books.models import BookModel, CategoryModel


class BookListView(ListView):
    template_name = 'books_list.html'

    def get_queryset(self):
        q = self.request.GET.get('q', '')

        return BookModel.objects.filter(
            Q(title__icontains=q) |
            Q(author__name__icontains=q) |
            Q(category__title__icontains=q)
        )


class BookCreateView(CreateView):
    template_name = 'form.html'
    form_class = BookModelForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create book'
        return context


class CategoryCreateView(CreateView):
    template_name = 'form.html'
    form_class = CategoryModelForm
    success_url = '/categories/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create category'
        return context


class CategoryUpdateView(UpdateView):
    model = CategoryModel
    form_class = CategoryModelForm
    success_url = '/categories/'
    template_name = 'form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update category'
        return context


class BookUpdateView(UpdateView):
    model = BookModel
    form_class = BookModelForm
    success_url = '/'
    template_name = 'form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update book'
        return context


class CategoriesListView(ListView):
    template_name = 'categories_list.html'
    model = CategoryModel


class BookDeleteView(DeleteView):
    model = BookModel
    success_url = '/'


class CategoryDeleteView(DeleteView):
    model = CategoryModel
    success_url = '/categories/'
