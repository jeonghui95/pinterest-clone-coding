
from django.http import HttpResponseForbidden

from articleapp.models import Article
from profileapp.models import Profile


def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        if article.writer != request.user:
            return HttpResponseForbidden()
        return func(request,*args,**kwargs)
    return decorated