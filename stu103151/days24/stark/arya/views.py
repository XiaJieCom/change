from django.shortcuts import render

# Create your views here.
from django.utils.encoding import smart_str
from django.http import FileResponse
from stark import settings


def file_download(request):
    file_path = request.GET.get('file_path')
    if file_path:
        file_center_dir = settings.SALT_CONFIG_FILES_DIR
        file_path = "%s%s" %(file_center_dir,file_path)
        filename = file_path.split('/')[-1]

        response = FileResponse(open(file_path,'rb'))
        response['Content-Disposition'] = 'attachment; filename=%s' %filename
        response['X-Sendfile'] = smart_str(file_path)

        return response
    else:
        raise KeyError



