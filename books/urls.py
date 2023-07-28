from django.urls import path
# from .views import BookListView, BookCreateView, BookDeleteView, BookUpdateView, BookDetailView, \
#     BookDetailUpdateDeleteView, BookListCreateView
from .views import ListView, DeleteView, DetailView, UpdateView, CreateView


urlpatterns = [
    path('list/', ListView.as_view(), name='list'),
    path('list/detail/<int:pk>/', DetailView.as_view(), name='detail'),
    path('list/delete/<int:pk>', DeleteView.as_view(), name='delete'),
    path('list/update/<int:pk>', UpdateView.as_view(), name='update'),
    path('list/create/', CreateView.as_view(), name='create'),
    # path('list/detail-update-delete/<int:pk>', BookDetailUpdateDeleteView.as_view(), name='list'),
    # path('list/list-create/', BookListCreateView.as_view(), name='list'),
]


# from .views import BookReviewViewSets
# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register('book', BookReviewViewSets, basename='book_review')
# urlpatterns = router.urls

