from django.shortcuts import render
from django.template import loader, Context, Template
from django.template.response import TemplateResponse,SimpleTemplateResponse
# Create your views here.


def get_customer_id(func):

    def coustomer(*args, **kwargs):
        # req = args.GET('req', None)
        # if req:
        coustomer_id = '11111'
        content = {'coustomer_id': coustomer_id}
        t = Template('gongjijin/gjj_index.html')
        c = Context(content)
        return t.render(c)
    return coustomer


class TemplateResponse_2(SimpleTemplateResponse):
    rendering_attrs = SimpleTemplateResponse.rendering_attrs + ['_request']

    def __init__(self, request, template, content_type=None,
                 status=None, charset=None, using=None):
        super().__init__(
            template, get_request_val(request), content_type, status, charset, using)
        self._request = request


def get_request_val(req):
    content = ''
    if req.method == 'GET':
        content = {'customer_id': req.GET.get('customer_id', None), 'serial_no': req.GET.get('serial_no', None)}
    elif req.method == 'POST':
        content = {'customer_id': req.POST.get('customer_id', None), 'serial_no': req.POST.get('serial_no', None)}
    if content:
        return content
    raise ValueError


def index(req):
    return TemplateResponse_2(req, 'gongjijin/gjj_index.html')