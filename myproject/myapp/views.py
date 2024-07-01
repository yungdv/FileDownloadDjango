from django.shortcuts import render, get_object_or_404
from .models import Section, Group

def index(request):
    sections = Section.objects.all()
    return render(request, 'index.html', {'sections': sections})

def groups(request, section_id):
    section = get_object_or_404(Section, id=section_id)
    groups = section.groups.all()
    return render(request, 'groups.html', {'section': section, 'groups': groups})

def files(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    files = group.files.all()
    return render(request, 'files.html', {'group': group, 'files': files})