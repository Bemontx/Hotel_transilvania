from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import ClienteForm

# Create your views here.

class HomeView(View):
    def get(self,request,*args, **kwargs):
        context={}
        return render(request,'inicio.html',context)

class ServiciosView(View):
    def get(self,request, *args, **kwargs):
        context={}
        return render(request,'servicios.html', context)

# vista reservas y formulario    
class ReservasView(View):
    def get(self,request,*args, **kwargs):
        form = ClienteForm()
        context = {
            'form': form
        }
        return render(request,'reservas.html', context)
    
    def post(self,request,*args, **kwargs):
        form = ClienteForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context = {'form': form}
            return render(request,'reservas.html',context)