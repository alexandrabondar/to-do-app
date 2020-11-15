from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTask, name='add'),
    path('complete/<int:task_id>', views.completeTask, name='complete'),
    path('delete/<task_id>', views.deleteTask, name='delete'),
    path('edit/<int:task_id>', views.editTask, name='edit'),
    path('about', views.about, name='about')
]
