from django.shortcuts import render, redirect
from django.views import View
from .models import Person, Address, Telephone, Email, Group
from .forms import PersonCreateForm


# Create your views here.
class MainPageView(View):
    def get(self, request):
        persons = Person.objects.order_by('name')
        ctx = {
            'persons': persons
        }
        return render(request, 'main.html', ctx)


class NewPersonView(View):
    def get(self, request):
        form = PersonCreateForm()
        return render(request, 'new.html', {'form': form})

    def post(self, request):
        form = PersonCreateForm(request.POST)
        if form.is_valid():
            p = Person()
            p.name = form.cleaned_data['name']
            p.surname = form.cleaned_data['surname']
            p.description = form.cleaned_data['description']
            p.save()
            return redirect('/')


class ModifyPersonView(View):
    def get(self, request, person_id):
        person = Person.objects.get(pk=person_id)
        form = PersonCreateForm()
        return render(request, 'new.html', {'form': form})

    def post(self, request, person_id):
        person = Person.objects.get(pk=person_id)
        form = PersonCreateForm(request.POST)
        if form.is_valid():
            p = Person()
            p.name = form.cleaned_data['name']
            p.surname = form.cleaned_data['surname']
            p.description = form.cleaned_data['description']
            p.pk = person_id
            p.save()
            return redirect('/')


class DeletePersonView(View):
    def get(self, request, person_id):
        p = Person.objects.get(pk=person_id)
        p.delete()
        return redirect('/')


class ShowPersonView(View):
    def get(self, request, person_id):
        person = Person.objects.get(pk=person_id)
        ctx = {
            'person': person
        }
        return render(request, 'show.html', ctx)
