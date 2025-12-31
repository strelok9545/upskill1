from django.shortcuts import render
from django.views import View
from django.views.generic import ListView,TemplateView,DetailView
from .models import Subject,Course

# Create your views here.


# class IndexView(View):

#     def get(self,request,subject_slug = None):

#         if subject_slug is None:
#             subjects = Subject.objects.all()


#         context = {
#             'subjects':subjects.order_by('id')
#         }
#         return render(request,'upskill/index.html',context)

class IndexView(ListView):
    model = Subject
    template_name = 'upskill/index.html'
    context_object_name = 'subjects'
    ordering = ['id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        subject_slug = self.kwargs.get('subject_slug')

        courses = Course.objects.all()

        if subject_slug:
            courses = courses.filter(subject_slug = subject_slug)

        context['courses'] = courses

        return context
    

class Aboutview(TemplateView):
    template_name = 'upskill/about.html'


class Courseview(TemplateView):
    template_name = 'upskill/course.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context
    

class CourseDetail(DetailView):
    template_name = 'upskill/detail.html'
    queryset = Course.objects.all()