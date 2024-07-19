from django.urls import path
from . import views

urlpatterns = [

path('author/add/', views.add_author, name='add_author'),
path('book/add/', views.add_book, name='add_book'),
path('borrow/add/', views.add_borrow_record, name='add_borrow_record'),
path('authors/list/', views.AuthorListView.as_view(), name='author_list'),
path('books/list/', views.book_list, name='book_list'),
path('borrows/list/', views.borrow_list, name='borrow_list'),
path('export/', views.export_library_data, name='export_library_data'),
]