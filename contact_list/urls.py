"""contact_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from list_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainPageView.as_view(), name='main_page'),
    path('new', views.NewPersonView.as_view(), name='new_person'),
    path('modify/<int:person_id>', views.ModifyPersonView.as_view(), name='modify_person'),
    path('delete/<int:person_id>', views.DeletePersonView.as_view(), name='delete_person'),
    path('show/<int:person_id>', views.ShowPersonView.as_view(), name='show_person'),
    path('add_address/<int:person_id>', views.AddAddressView.as_view(), name='add_address'),
    path('add_email/<int:person_id>', views.AddEmailView.as_view(), name='add_email'),

]
