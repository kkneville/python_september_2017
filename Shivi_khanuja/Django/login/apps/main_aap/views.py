from django.shortcuts import render, redirect, reverse
from ..login.models import User

def current_user(request):
    return User.objects.get(id=request.session['user_id'])


def dashboard(request):
    if 'user_id' in request.session:
        context= {
            'user': current_user(request),
        }    
        return render(request,'main_aap/success.html',context)
    
    return redirect(reverse('landing'))




