from django.shortcuts import render
from django.views import View
from .models import Person, Address, Telephone, Email, Group

# Create your views here.
class MainPageView(View):
    def get(self, request):
        persons = Person.objects.all()
        ctx = {
            'persons': persons
        }
        return render(request, 'main.html', ctx)
