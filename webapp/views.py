from django.shortcuts import render, HttpResponseRedirect
from .forms import ResumeForm
from webapp.models import Resume
from django.views import View


# Create your views here.

class HomeView(View):
    def get(self, request):
        form = ResumeForm()
        can = Resume.objects.all()
        return render(request, 'webapp/home.html', {'can':can,'form':form})

    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(request, 'webapp/home.html', {'form': form})

class CandidateView(View):
    def get(self, request, pk):
        can = Resume.objects.get(pk=pk)
        return render(request, 'webapp/candidate.html', {'can':can})


