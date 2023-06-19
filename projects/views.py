from django.shortcuts import render
from projects.models import Project


def project_index(request):
    projects = Project.objects.all()  # query

    # The context dictionary is used to send information to our template.
    context = {
        'projects': projects
    }

    # We add context is as an argument to render().
    # Any entries in the context dictionary are available in the template,
    # as long as the context argument is passed to render().
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)