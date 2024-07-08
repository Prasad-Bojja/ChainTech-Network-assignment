from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import UserSubmission

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        submission = UserSubmission(name=name, email=email)
        submission.save()
 
    context = {
        'current_time': datetime.now(),
    }
    return render(request, 'index.html', context)


def display_submissions(request):
    submissions = UserSubmission.objects.all()
    context = {'submissions': submissions}
    return render(request, 'submissions.html', context)
