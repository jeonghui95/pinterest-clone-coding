
from django.http import HttpResponseForbidden

from articleapp.models import Article
from profileapp.models import Profile
from projectapp.models import Project


def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        project = Project.objects.get(pk=kwargs['pk'])
        if  project.user != request.user:
            return HttpResponseForbidden()
        return func(request,*args,**kwargs)
    return decorated