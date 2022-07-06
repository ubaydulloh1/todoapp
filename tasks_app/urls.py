from django.urls import path
from . import views


app_name = 'tasks_app'

urlpatterns = [
    path('create', views.create_task, name='create-task'),
    path('<str:pk>', views.task_detail, name='task-detail'),
    path('<str:pk>/edit', views.edit_task, name='task-edit'),
    path('<str:pk>/delete/confirm', views.delete_task, name='delete-task'),

    path('<str:pk>/pin-unpin', views.pin_task, name='pin-task'),
    path('<str:pk>/set-as-done', views.set_as_task, name='set-as-done-task'),
]
