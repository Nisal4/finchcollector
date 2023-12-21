from django.urls import path
from . import views
from .views import FinchCreate, FinchUpdate, FinchDelete, FinchDetail, FeedingCreate


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='finches_index'),
    path('finches/<int:finch_id>/', views.finch_detail, name='finch_detail'),
    path('finches/add/', FinchCreate.as_view(), name='finch_add'),
    path('finches/<int:pk>/edit/', FinchUpdate.as_view(), name='finch_edit'),
    path('finches/<int:pk>/delete/', FinchDelete.as_view(), name='finch_delete'),
    path('finches/<int:pk>/', FinchDetail.as_view(), name='finch_detail'),
    path('finches/<int:pk>/add_feeding/', FeedingCreate.as_view(), name='feeding_add'),
]