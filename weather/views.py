from django.shortcuts import render

# Create your views here.
def index(req):
    if req.method == 'POST':
        city = req.POST['city']
    else:
        city = ''
    return render(req, 'index.html', {'city': city})