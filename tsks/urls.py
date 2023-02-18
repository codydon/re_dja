from django.urls import path

from . import views

app_name = 'tsks'
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('<int:taskID>/delete/', views.delete, name='delete')
    # path('<int:question_id>/', views.details, name='details')
]




