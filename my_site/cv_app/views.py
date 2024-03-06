from django.shortcuts import render
from django.shortcuts import redirect
from .forms import DetailForm
from .models import Detail
# import pdfkit
from django.http import HttpResponse
from django.template import loader
# import io
# Create your views here.

def homeview(request):
    detail = Detail.objects.all()
    return render(request, 'cv_app/home.html', context = {'detail':detail})

def detailview(request, id):
    detail = Detail.objects.get(id=id)
    return render(request, 'cv_app/detail.html', context={'detail':detail})

def cv_form(request):
    if request.method == 'POST':
        form = DetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cv_app:home')
    else:
        form = DetailForm()
    return render(request, 'cv_app/cv_form.html', context = {'form':form})

# def download(request, id):
#     options = {
#         'page-size':'A4',
#         'encoding':"UTF-8",
#         'enable-local-file-access':''
#     }
#     detail = Detail.objects.get(id=id)
#     template = loader.get_template('cv_app/download.html')
#     html = template.render({'detail':detail})
#     pdf = pdfkit.from_string(html,False,options)
#     response = HttpResponse(pdf,content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename = resume.pdf'
    
#     return response