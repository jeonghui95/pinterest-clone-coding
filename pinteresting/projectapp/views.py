from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project

@method_decorator(login_required,'post')
@method_decorator(login_required,'get')
class ProjectCreateView(CreateView):
    model = Project
    template_name = 'projectapp/create.html'
    form_class = ProjectCreationForm
    context_object_name = 'target_project'


    def get_success_url(self):
        return reverse('projectapp:detail',kwargs={'pk':self.object.pk})

class ProjectDetailView(DetailView,MultipleObjectMixin):
    model = Project
    template_name = 'projectapp/detail.html'
    context_object_name = 'target_project'

    paginate_by = 5
    
    def get_context_data(self, **kwargs):
        object_list=Article.objects.filter(project=self.get_object())
        return super(ProjectDetailView, self).get_context_data(object_list=object_list,**kwargs)
    
class ProjectListView(ListView):
    model = Project
    template_name = 'projectapp/list.html'
    context_object_name = 'project_list'
    paginate_by=1


