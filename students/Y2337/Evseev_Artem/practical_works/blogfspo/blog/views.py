from django.shortcuts import render
from django.http import Http404
from blog.models import Owner


def detail(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'detail.html', {"owner": owner})
