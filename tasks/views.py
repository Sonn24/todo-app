from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import*
from .forms import*

# Create your views here.

def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')    

    context = {'tasks':tasks, 'form':form}
    return render(request,'tasks/lists.html', context)
def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form =TaskForm(instance=task)

    context = {'form':form}

    return render(request, 'tasks/update_task.html', context)
