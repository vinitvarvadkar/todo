from django.shortcuts import render,redirect

from django.http import HttpResponse

from .forms import TodoForm

from .models import Todo

# Create your views here.

# def hi(request):
#     return HttpResponse("Welcome Task Application!")


def hi(request):
    form= TodoForm()
    task= Todo.objects.all()

    if request.method == 'POST':
        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('hi')
    
    context ={'task': task, 'TodoForm':form}

    return render(request, 'createtodo.html',context)



def update_task(request,pk):
    task= Todo.objects.get(id=pk)

    form=TodoForm(instance=task)

    if request.method=="POST":
        form=TodoForm(request.POST,instance=task)
        
        if form.is_valid():
            form.save()
        return redirect('hi')


    context={'task':task, 'TodoForm':form}

    return render(request,"update.html",context=context)


# def Update_task(request,pk):
#     pass

# def Delete_task(request,pk):
#     pass




def update_task(request,pk):
    task = Todo.objects.get(id=pk)

    form = TodoForm(instance=task)

    if request.method=="POST":

        form = TodoForm(request.POST,instance=task)

        if form.is_valid():

            form.save()

            return redirect('hi')
        
    context={'TodoForm':form}
    return render(request,'update.html',context)




def delete_task(request,pk):
    task=Todo.objects.get(id=pk)

    if request.method=="POST":
        task.delete()

        return redirect('hi')
    
    context={'TodoForm': Todo}
    return render(request,'delete.html',context)



















