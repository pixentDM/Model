from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import File
import os

# def delete_file(request, file_no):                                      # 파일 삭제
#     file_to_delete = get_object_or_404(File, file_no=file_no)
#     if file_to_delete.file_data:
#         if os.path.isfile(file_to_delete.file_data.path):
#             os.remove(file_to_delete.file_data.path)
#     file_to_delete.delete()
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
