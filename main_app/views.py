from django.shortcuts import render, redirect
from .models import Finch, Feeding
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from .forms import FeedingForm
# Create your views here.
finches = [
    {"id": 1, "species": "Zebra Finch", "color": "Black and White", "size": "Small"},
    {"id": 2, "species": "Gouldian Finch", "color": "Multi-colored", "size": "Small"},
    {"id": 3, "species": "Bengalese Finch", "color": "Brown and White", "size": "Small"}
]
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})

def finch_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', {'finch': finch})

class FinchCreate(CreateView):
    model = Finch
    fields = ['species', 'color', 'size']
    template_name = 'finches/finch_form.html'
    success_url = reverse_lazy('finches_index')

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['species', 'color', 'size']
    template_name = 'finches/finch_form.html'
    success_url = reverse_lazy('finches_index')

class FinchDelete(DeleteView):
    model = Finch
    template_name = 'finches/finch_confirm_delete.html'
    success_url = reverse_lazy('finches_index')

class FinchDetail(DetailView):
    model = Finch

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feedings'] = Feeding.objects.filter(finch=self.kwargs['pk'])
        return context
    
class FeedingCreate(CreateView):
    model = Feeding
    form_class = FeedingForm