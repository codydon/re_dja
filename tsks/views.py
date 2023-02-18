from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Task, Category
from django.template import loader
from django.http import Http404
from django.urls import reverse
from datetime import datetime


# Create your views here.
def all(request):
    # return HttpResponse("This is the tsks index")
    latest_task_list = Task.objects.order_by('-task_name')[:5]
    # output = ', '.join([q.task_name for q in latest_task_list])
    # return HttpResponse(output)

    # template = loader.get_template('tsks/index.html')
    # context = {
    #     'latest_task_list': latest_task_list,
    # }
    # return HttpResponse(template.render(context, request))

    context = {'latest_task_list': latest_task_list}
    return render(request, 'tsks/all.html', context)

def t_detail(request, t_id):
    # try:
    #     task = Task.objects.get(pk=t_id)
    # except Task.DoesNotExist:
    #     raise Http404("Task does not exist")
    # return render(request, 'tsks/t_detail.html', {'task': task})

    task = get_object_or_404(Task, pk=t_id)
    return render(request, 'tsks/t_detail.html', {'task': task})

# def t_detail(request, t_id):
#     return HttpResponse("You're looking at question %s." % t_id)


def index(request):
    if request.method == 'POST':
        # Create a new instance of your model with data from the form
        new_obj = Task(
            task_name=request.POST['task'], # replace "task_name" with the name of your model's field
            p_date=datetime.now()
        )
        
        # Save the new object to the database
        new_obj.save()
        
        # Redirect the user to a success page or another relevant URL
        return redirect('tsks:all')
    
    # If the request method is not POST, render the form template
    return render(request, 'tsks/index.html')

    # return HttpResponse("This is the tsks add")