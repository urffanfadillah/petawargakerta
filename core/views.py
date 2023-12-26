from django.shortcuts import render, redirect
from .models import Location
from .forms import LocationForm

# Create your views here.
def dashboard(request):
  locations = Location.objects.all()
  print(locations)
  template = 'dashboard.html'
  context = {
    'locations': locations
  }
  return render(request, template, context)

def add_location(request):
  if request.method == 'POST':
    form = LocationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('dashboard')
  else:
    form = LocationForm()
  return render(request, 'add_location.html', {'form': form})
  