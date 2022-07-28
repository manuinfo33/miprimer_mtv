from django.shortcuts import render
from App_family.models import Family

def create_person(request):
    new_person= Family.objects.create(name="Jazmin", age=23)
    context={
        "new_person":new_person
    }
    return render(request,"new_person.html",context=context)

