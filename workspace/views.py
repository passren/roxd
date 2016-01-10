from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return redirect('/workspace/roads')

def roads(request):
    return render(request, 'workspace_roads.html')