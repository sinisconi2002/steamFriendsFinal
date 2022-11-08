from django.urls import path

from blog.views import *

urlpatterns = [
    path('allposts/', allposts, name="all"),
    path('post/<int:pk>/', PostDetailView.as_view(), name='postdetailed'),
    path('post/create/', PostCreation.as_view(), name='createpost'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='updatepost'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='deletepost')
]