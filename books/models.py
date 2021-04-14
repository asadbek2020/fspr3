from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class AuthorModel(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True, blank=True)

    # author.books.all()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'


class CategoryModel(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class BookModel(models.Model):
    title = models.CharField(max_length=50)
    page_count = models.IntegerField(null=True, blank=True)
    author = models.ForeignKey(AuthorModel,
                               on_delete=models.PROTECT,
                               related_name='books')
    category = models.ForeignKey(CategoryModel,
                                 on_delete=models.PROTECT,
                                 related_name='books',
                                 null=True)
    description = RichTextUploadingField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'
