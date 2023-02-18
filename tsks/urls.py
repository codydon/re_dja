from django.urls import path

from . import views

app_name = 'tsks'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:t_id>/', views.t_detail, name='t_detail'),
    path('all/', views.all, name='all')
    path('delete/', views.delete_tasks, name='delete_tasks')
    # path('<int:question_id>/', views.details, name='details')
    # path('<int:question_id>/', views.details, name='details')
]




