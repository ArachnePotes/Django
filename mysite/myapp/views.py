from django.shortcuts import render

from services.models import Service
from staff.models import satff
from activitie.models import Activity
from about.models import about

def index(request):
    services = Service.objects.all()
    return render(request,'myapp/index.html',
                  {'services': services,}
                  )

def contact(request):
    people = satff.objects.all()
    return render(request,'myapp/contact.html',
                 {'people': people,}
                  )              

def services(request):
    activities = Activity.objects.all()
    return render(request,'myapp/services.html',
                  {'activities': activities,}
                  )

def info(request):
    topics = about.objects.all()
    return render(request,'myapp/about.html',
                  {'topics': topics,}
                  )
    
