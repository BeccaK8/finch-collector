from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('finches/<int:finch_id>/add_photo/', views.add_photo, name='add_photo'),
    path('finches/<int:finch_id>/assoc_feeder/<int:feeder_id>/', views.assoc_feeder, name='assoc_feeder'),
    path('finches/<int:finch_id>/unassoc_feeder/<int:feeder_id>/', views.unassoc_feeder, name='unassoc_feeder'),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),

    # feeder routes
    path('feeders/', views.FeederList.as_view(), name='feeders_index'),
    path('feeders/create/', views.FeederCreate.as_view(), name='feeders_create'),
    path('feeders/<int:pk>/update', views.FeederUpdate.as_view(), name='feeders_update'),
    path('feeders/<int:pk>/delete', views.FeederDelete.as_view(), name='feeders_delete'),
    path('feeders/<int:pk>/', views.FeederDetail.as_view(), name='feeder_detail'),
]