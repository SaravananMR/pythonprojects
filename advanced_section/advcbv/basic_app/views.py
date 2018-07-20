from django.shortcuts import render
from django.views.generic import (View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy
from . import models

def sendingmail(request):
    subject = "HELLO WORLD!"
    message = "WELCOME"
    from_email = settings.EMAIL_HOST_USER
    to_email = ['saravanan.ravi@disys.com']

    send_mail(subject = subject, from_email = from_email, recipient_list = to_email, message = message, fail_silently = False)

    return HttpResponse("Success")




class IndexView(TemplateView):
    template_name = 'index.html'

#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         context['injectme'] = 'BASIC INJECTION!'
#         return context
#     # def get(self,request):
#     #     return HttpResponse("Class based view")
# # Create your views here.
# # def index(request):
# #     return render(request,'index.html')





class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")
    