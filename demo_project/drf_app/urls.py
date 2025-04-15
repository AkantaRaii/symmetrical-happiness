from .views import BookList,home,UserList
from django.urls import path

urlpatterns = [
    path('home/',home,name='home'),
    path('api/user/<str:username>/',UserList.as_view(),name='user-list'),
    path('api/user/',UserList.as_view(),name='user-list'),
    path('api/book',BookList.as_view(),name='book-list')
]
