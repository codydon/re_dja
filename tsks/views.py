from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Task, Category
from django.template import loader
from django.http import Http404
from django.urls import reverse

# Create your views here.
def index(request):
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
    return render(request, 'tsks/index.html', context)

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


def t_add(request, t_id):
    task = get_object_or_404(Task, pk=t_id)
    try:
        selected_task = task.task_name.get(pk=request.POST['task'])
    except(KeyError, Category.DoesNotExist):
        return render(request, 'tsks/t_detail.html', { 
            'task': task,
            'error_message': "you didnt select a category"
        })
    else:
        selected_task += 1
        selected_task.save()
        return(HttpResponseRedirect(reverse('tsks:t_add', args=(task.id,))))