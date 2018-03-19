from django.shortcuts import render, redirect
from django.views import View
from .models import Person, Address, Telephone, Email, Group
from .forms import PersonCreateForm, AddressCreateForm, TelephoneCreateForm, EmailCreateForm


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
        ctx = {
            'form': form,
            'person': person
        }
        return render(request, 'modify.html', ctx)

    def post(self, request, person_id):
        person = Person.objects.get(pk=person_id)
        form = PersonCreateForm(request.POST)
        if form.is_valid():
            p = Person()
            p.name = form.cleaned_data['name']
            p.surname = form.cleaned_data['surname']
            p.description = form.cleaned_data['description']
            p.pk = person.id
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
            'person': person,
        }
        return render(request, 'show.html', ctx)


class AddAddressView(View):
    def get(self, request, person_id):
        person = Person.objects.get(pk=person_id)
        form = AddressCreateForm()
        ctx = {
            'person': person,
            'form': form
        }
        return render(request, 'new.html', ctx)

    def post(self, request, person_id):
        person = Person.objects.get(pk=person_id)
        form = AddressCreateForm(request.POST)
        if form.is_valid():
            a = Address()
            a.city = form.cleaned_data['city']
            a.street = form.cleaned_data['street']
            a.house = form.cleaned_data['house']
            a.flat = form.cleaned_data['flat']
            a.person_id = person.id
            a.save()
            return redirect('/')


class AddTelephoneView(View):
    def get(self, request, person_id):
        person = Person.objects.get(pk=person_id)
        form = TelephoneCreateForm()
        ctx = {
            'person': person,
            'form': form
        }
        return render(request, 'new.html', ctx)

    def post(self, request, person_id):
        person = Person.objects.get(pk=person_id)
        form = TelephoneCreateForm(request.POST)
        if form.is_valid():
            t = Telephone()
            t.number = form.cleaned_data['number']
            t.type = form.cleaned_data['type']
            t.person_id = person.id
            t.save()
            return redirect('/')


class AddEmailView(View):
    def get(self, request, person_id):
        person = Person.objects.get(pk=person_id)
        form = EmailCreateForm()
        ctx = {
            'person': person,
            'form': form
        }
        return render(request, 'new.html', ctx)

    def post(self, request, person_id):
        person = Person.objects.get(pk=person_id)
        form = EmailCreateForm(request.POST)
        if form.is_valid():
            e = Email()
            e.email = form.cleaned_data['email']
            e.type = form.cleaned_data['type']
            e.person_id = person.id
            e.save()
            return redirect('/')
