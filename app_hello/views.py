from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


def hello(request):
    context = {
        'name': 'Ali',
        'now': datetime.now(),
        'news': [
            {
                'id': 1,
                'title': 'news 1'
            },
            {
                'id': 2,
                'title': 'news 2'
            },
            {
                'id': 3,
                'title': 'news 3'
            }
        ]
    }
    return render(request, 'hello.html', context)


def resume(request, id):
    user = get_object_or_404(User, id=id)
    context = {'user': user}
    return render(request, 'resume.html', context)