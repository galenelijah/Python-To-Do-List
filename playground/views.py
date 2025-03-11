from django.shortcuts import render, redirect
from .models import Task

# 📌 Display Tasks
# 📌 Add Task
def index(request):
    if request.method == "POST":
        title = request.POST['title']
        Task.objects.create(title=title)
    tasks = Task.objects.all()
    return render(request, 'playground/index.html', {'tasks': tasks})


# 📌 Delete Task
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')

# 📌 Update Task (Mark as Done)
def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('index')
