from django.urls import path ,include
from .import views
urlpatterns = [
     path('',views.ArticleListView.as_view(),name='home'),
      path('add/',views.ArticleCreateView.as_view(),name='add'),
       path('details/<int:pk>',views.ArticleDetailView.as_view(),name='details'),
       path('edit/<int:pk>',views.ArticleUpdateView.as_view(),name='edit'),
       path('delete/<int:pk>',views.ArticleDeleteView.as_view(),name='delete'),


]
