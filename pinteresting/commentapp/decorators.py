
from django.http import HttpResponseForbidden

from commentapp.models import Comment
from profileapp.models import Profile


def comment_ownership_required(func):
    def decorated(request, *args, **kwargs):
        comment = Comment.objects.get(pk=kwargs['pk'])
        if comment.writer != request.user:
            return HttpResponseForbidden()
        return func(request,*args,**kwargs)
    return decorated