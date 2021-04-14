from django.urls import path

from books.views import BookCreateView, CategoriesListView, BookListView, CategoryCreateView, \
    CategoryUpdateView, BookUpdateView, CategoryDeleteView, BookDeleteView

urlpatterns = [
    path('categories/', CategoriesListView.as_view()),
    path('categories/create/', CategoryCreateView.as_view()),
    path('categories/update/<int:pk>/', CategoryUpdateView.as_view()),
    path('categories/delete/<int:pk>/', CategoryDeleteView.as_view()),
    path('create/', BookCreateView.as_view()),
    path('update/<int:pk>/', BookUpdateView.as_view()),
    path('delete/<int:pk>/', BookDeleteView.as_view()),
    path('', BookListView.as_view()),
]
