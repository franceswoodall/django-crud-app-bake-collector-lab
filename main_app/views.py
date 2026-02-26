#models 
from .models import Bake, Review
from .forms import ReviewForm

#django 
from django.shortcuts import render, redirect

#django - views
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#reverse_lazy
from django.urls import reverse_lazy
from django.urls import reverse

#auth 
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Home(LoginView): 
    template_name = 'home.html'

def about(request): 
    return render(request, 'about.html')

class BakeList(ListView):
    model = Bake 
    template_name = 'bakes/bake_list.html'

    def get_queryset(self):
        return Bake.objects.filter(user=self.request.user)

class BakeDetail(LoginRequiredMixin, DetailView): 
    model = Bake 
    template_name = 'bakes/bake_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review_form'] = ReviewForm()
        return context

#Bake - CRUD 

class BakeCreate(LoginRequiredMixin, CreateView): 
    model = Bake
    fields = ['name', 'bakery', 'description', 'price']
    template_name = 'bakes/bake_form.html'
    success_url = reverse_lazy('bake-index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class BakeUpdate(LoginRequiredMixin, UpdateView): 
    model = Bake
    fields = ['name', 'bakery', 'description', 'price']
    template_name = 'bakes/bake_form.html'

class BakeDelete(LoginRequiredMixin, DeleteView):
    model = Bake
    template_name = 'bakes/bake_confirm_delete.html'
    success_url = reverse_lazy('bake-index')

#Reviews - CRUD - function based 

@login_required
def review_add(request, pk):
    form = ReviewForm(request.POST)
    if form.is_valid(): 
        new_review = form.save(commit=False)
        new_review.user = request.user
        new_review.bake_id = pk 
        new_review.save()
    return redirect('bake-detail', pk=pk)

@login_required
def review_delete(request, bake_id, review_id):
    review = Review.objects.get(id=review_id)
    if review.user == request.user: 
        review.delete()
    return redirect('bake-detail', pk=bake_id)

@login_required
def review_edit(request, bake_id, review_id):
    review = Review.objects.get(id=review_id)
    if review.user != request.user: 
        return redirect('bake-detail', pk=bake_id)

    if request.method =='POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid(): 
            form.save()
            return redirect('bake-detail', pk=bake_id)
    else: 
        form = ReviewForm(instance=review)
    return render(request, 'bakes/edit_review.html', {
        'form': form, 
        'bake_id': bake_id
    })

# SignUp

def signup(request): 
    error_message = ''
    if request.method == 'POST': 
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('bake-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)