from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('schools/', views.SchoolListView.as_view(), name='schools'),
    path('school/<int:pk>', views.SchoolDetailView.as_view(), name='school-detail'),
    path('coordinators/', views.CoordinatorsListView.as_view(), name='coordinators'),
    path('coordinator/<int:pk>', views.CoordinatorsDetailView.as_view(), name='coordinator-detail'),
    path('testschedules/', views.TestScheduleListView.as_view(), name='testschedules'),
    path('testschedule/<str:pk>', views.TestScheduleDetailView.as_view(), name='testschedule-detail'),
]

urlpatterns += [  
    path('school/create/', views.SchoolCreate.as_view(), name='school_create'),
    path('school/<int:pk>/update/', views.SchoolUpdate.as_view(), name='school_update'),
    path('school/<int:pk>/delete/', views.SchoolDelete.as_view(), name='school_delete'),
    path('coordinator/create/', views.CoordinatorsCreate.as_view(), name='coordinator_create'),
    path('coordinator/<int:pk>/update/', views.CoordinatorsUpdate.as_view(), name='coordinator_update'),
    path('coordinator/<int:pk>/delete/', views.CoordinatorsDelete.as_view(), name='coordinator_delete'),
    path('testschedule/create/', views.TestScheduleCreate.as_view(), name='testschedule_create'),
    path('testschedule/<str:pk>/update/', views.TestScheduleUpdate.as_view(), name='testschedule_update'),
    path('testschedule/<str:pk>/delete/', views.TestScheduleDelete.as_view(), name='testschedule_delete'),
]
