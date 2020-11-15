from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect


def index(request):
    # if request.method == 'POST':
    #     if "create_task" in request.POST:
    #         form = TaskForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #         else:
    #             error: "The form is not valid. Please try again"
        # if "delete_task" in request.POST:
        #     task = Task.objects.get('id')
        #     task.delete()

    form = TaskForm()
    tasks = Task.objects.order_by('-id')
    context = {'title': 'Main page', 'tasks': tasks,  'form': form}
    return render(request, "main/index.html", context)


@require_POST
def addTask(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        new_task = Task(title_task=request.POST['title_task'], description_task=request.POST['description_task'])
        new_task.save()
    return redirect('index')


def completeTask(request, task_id):
    task = Task.objects.get(id=task_id)
    task.complete = True
    task.save()
    return redirect('index')


def deleteTask(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')


def editTask(request, task_id):
    # task = Task.objects.get(id=task_id)
    # form = TaskForm(instance=task)
    # if request.method == 'POST':
    #     form = TaskForm(request.POST, instance=task)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('index')
    # return render(request, 'main/edit.html', {"task_edit_form": form})
    if request.method == 'POST':
        task = Task.objects.get(id=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            task = Task.objects.get(id=task_id)
            return render(request, 'main/edit.html', {'task': task, 'form': form})


def about(request):
    return render(request, "main/about.html")
