from django.urls import path
from . import views
from django.conf.urls import url, include

urlpatterns = [
    path('', views.library_home, name='library_home'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^book/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]