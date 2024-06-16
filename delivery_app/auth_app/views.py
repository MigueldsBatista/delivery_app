from django.shortcuts import render

# Create your views here.
def login(request):

    if request.method=='POST':
        usuario=request.POST.get('usuario')
        senha=request.POST.get('senha')

    return render(request, 'index.html')

def cadastro(request):
    
    return render(request, 'cadastro.html')