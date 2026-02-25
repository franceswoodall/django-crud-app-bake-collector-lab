#models 
from .models import Bake, Review

from .forms import ReviewForm

#django 
from django.shortcuts import render, redirect
from django.shortcuts import render

#django - views
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User

#reverse_lazy
from django.urls import reverse_lazy
from django.urls import reverse



# Create your views here.

class Home(LoginView): 
    template_name = 'home.html'

def about(request): 
    return render(request, 'about.html')

class BakeList(ListView):
    model = Bake 
    template_name = 'bakes/bake_list.html'

class BakeDetail(DetailView): 
    model = Bake 
    template_name = 'bakes/bake_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review_form'] = ReviewForm()
        return context


class BakeCreate(CreateView): 
    model = Bake
    fields = ['name', 'bakery', 'description', 'price']
    template_name = 'bakes/bake_form.html'
    

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)

class BakeUpdate(UpdateView): 
    model = Bake
    fields = ['name', 'bakery', 'description', 'price']
    template_name = 'bakes/bake_form.html'

class BakeDelete(DeleteView):
    model = Bake
    template_name = 'bakes/bake_confirm_delete.html'
    success_url = reverse_lazy('bake-index')

def add_review(request, pk):
    form = ReviewForm(request.POST)
    if form.is_valid(): 
        new_review = form.save(commit=False)
        new_review.bake_id = pk
        new_review.save()
    return redirect('bake-detail', pk=pk)