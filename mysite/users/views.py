from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data('username')

    form = UserCreationForm()
    context = {
        'form':form,
    }
    return render(request,'users/register.html',context)

