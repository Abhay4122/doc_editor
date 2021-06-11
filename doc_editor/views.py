from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import text_editor
import json

# Create your views here.

def index(request):
    return render(request, 'doc_editor/index.html')


def doc_list(request):
    data = text_editor.objects.all()
    return render(request, 'doc_editor/doc_list.html', {'data': data})


def get_text_data(request, id):
    data = text_editor.objects.filter(id=id)
    return render(request, 'doc_editor/index.html', {'data': data})


def text_data_post(request):
    response = {
        'status': 'ok'
    }

    try:
        request_body = request.POST
        id = request_body.get('id')

        if id:
            text_editor.objects.filter(id=id).update(
                title=request_body.get('title'), text=request_body.get('body')
            )
            response['message'] = 'Document updated successfully!!'
            response['msg_typ'] = 'success'
        else:
            text_editor.objects.create(
                title=request_body.get('title'), text=request_body.get('body')
            )
            response['message'] = 'Document created successfully!!'
            response['msg_typ'] = 'success'
    except Exception as e:
        print(e)
        response['message'] = 'Some thing went wrong!!'
        response['msg_typ'] = 'error'

    return HttpResponse(json.dumps(response), content_type='application/json')