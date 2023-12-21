from django.shortcuts import render, redirect

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
    return render(request, 'finches/index.html', {'finches': finches})



