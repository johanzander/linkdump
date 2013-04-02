from django.shortcuts import render_to_response
from django.core.paginator import Paginator
from linkdump.linktracker.models import Link
from django.template import RequestContext


def render_response(req, *args, **kwargs):
    kwargs['context_instance'] = RequestContext(req)
    return render_to_response(*args, **kwargs)


def list(request, page = 1, message = ""):
    page = int(page)
    link_list = Paginator(Link.objects.all(), 5)
    has_previous = link_list.page(page).has_previous()
    has_next = link_list.page(page).has_next()


    return render_response(
        request,
        'links/list.html',
        {'link_list': link_list.page(page),
         'has_previous': has_previous,
         'previous_page': page - 1,
         'has_next': has_next,
         'next_page': page + 1,
         'message': message}
    )

def new(request):
    return render_response(
        request,
        'links/form.html',
        {'action': 'add', 'button': 'Add'}
    )


def edit(request, id):
    link = Link.objects.get(id=id)
    return render_response(
        request,
        'links/form.html',
        {'link': link,
         'action': 'update/' + id,
         'button': 'Update'}
    )


def add(request):
    link_description = request.POST['link_description']
    link_url = request.POST['link_url']
    link = Link(
        link_description = link_description,
        link_url = link_url
    )
    link.save()
    return list(request, message='Link added!')


def update(request, id):
    link = Link.objects.get(id=id)
    link.link_description = request.POST['link_description']
    link.link_url = request.POST['link_url']
    link.save()
    return list(request, message='Link updated!')


def delete(request, id):
    Link.objects.get(id=id).delete()
    return list(request, message='Link deleted!')

