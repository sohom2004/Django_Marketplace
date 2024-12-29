from django.shortcuts import render, redirect
from items.models import Category, Items
from .forms import SignupForm

# Create your views here.
def index(request):
    item = Items.objects.all()
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': item,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        print(form)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
        
    else:
        form = SignupForm()
    
    return render(request, 'core/signup.html', {
        'form': form
    })