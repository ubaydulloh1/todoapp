from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib import messages

from .forms import TaskModelForm
from .models import Task
from django.urls import reverse_lazy

from datetime import datetime


@login_required(login_url=reverse_lazy('users:login'))
def create_task(request):
    form = TaskModelForm()

    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            messages.success(request, "Task muvaffaqiyatli qo'shildi!")
            return redirect('users:home')
        else:
            messages.error(request, "To'g'ri to'ldiring!")

    context = {
        'form': form,
        'page': 'create-page'
        }
    return render(request, 'tasks_app/create_update_task.html', context)




@login_required(login_url=reverse_lazy('users:login'))
def task_detail(request, pk):
    task = get_object_or_404(Task, id=pk)

    context = {'task': task}
    return render(request, 'tasks_app/task_detail.html', context)



@login_required(login_url=reverse_lazy('users:login'))
def edit_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    form = TaskModelForm(instance=task)

    if request.method == "POST":
        form = TaskModelForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task muvaffaqiyatli tahrirlandi!")
            return redirect('users:home')
        else:
            messages.error(request, "To'g'ri to'ldiring!")

    context = {
        'form': form,
        'page': 'edit-page'
        }
    return render(request, 'tasks_app/create_update_task.html', context)



@login_required(login_url=reverse_lazy('users:login'))
def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    
    if request.method == "POST":
        task_title = task.title
        task.delete()
        messages.success(request, f"'{task_title}' muvaffiqatli o'chirildi!")
        return redirect('users:home')

    context = {
        'task': task,
    }
    return render(request, 'tasks_app/delete.html', context)


@login_required(login_url=reverse_lazy('users:login'))
def pin_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    
    task.is_pinned = not task.is_pinned
    if task.is_pinned:
        task.pinned_at = datetime.now()
    else:
        task.pinned_at = None
    task.save()

    if task.is_pinned:
        messages.success(request, f"{task.title} is pinned!")
    else:
        messages.info(request, f"{task.title} is unpinned!")
    return redirect('users:home')



@login_required(login_url=reverse_lazy('users:login'))
def set_as_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    
    task.is_completed = not task.is_completed
    if task.is_completed:
        task.completed_at = datetime.now()
    else:
        task.pinned_at = None
    task.save()

    if task.is_completed:
        messages.success(request, f"{task.title} is completed!")
    else:
        messages.info(request, f"{task.title} is uncompleted!")
    
    return redirect('users:home')
