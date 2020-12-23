from django.shortcuts import render, redirect
from .models import Dojos, Ninjas

def index(request):
    context = {
    "dojo_objects": Dojos.objects.all(),
    }    
    return render(request, 'index.html', context)

def addDojo(request):
    Dojos.objects.create(
        name=request.POST['name'], 
        city=request.POST['city'], 
        state = request.POST['state'],
    )
    return redirect('/')

def addNinja(request):
    Ninjas.objects.create(
        fname = request.POST['fname'], 
        lname = request.POST['lname'],
        dojo_id = Dojos.objects.get(id=request.POST['dojo']),
    )
    return redirect('/')


def deleteDojo(request):
    print("*****   inside deleteDojo   *****")
    dojo_id = Dojos.objects.get(id=request.POST['delete'])
    dojo_id.delete()
    return redirect('/')




# <!-- <ul id="allDojoInfo">
#     {% for i in dojo_objects %}
#     <li>
#         Ninjas at the {{ i.name }}
#         <ul>
#             {% for j in i.ninjas.all %}
#             <li>{{ j.fname }} {{ j.lname }}</li>
#             {% endfor %}
#         </ul>
#     </li>
#     {% endfor %}
# </ul> -->