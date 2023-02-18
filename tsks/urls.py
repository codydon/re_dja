from django.urls import path

from . import views

app_name = 'tsks'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:t_id>/', views.t_detail, name='t_detail'),
    path('/<int:t_id>/add', views.t_add, name='t_add')
    # path('<int:question_id>/', views.details, name='details')
    # path('<int:question_id>/', views.details, name='details')
]




