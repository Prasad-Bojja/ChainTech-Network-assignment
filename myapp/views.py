from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from .models import UserSubmission
from .forms import SubmissionForm

def index(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            submission = UserSubmission(name=name, email=email)
            submission.save()
            return redirect('/submissions/')

    else:
        form = SubmissionForm()
 
    context = {
        'current_time': datetime.now(),
        'form': form
    }
    return render(request, 'index.html', context)


def display_submissions(request):
    submissions = UserSubmission.objects.all()
    context = {'submissions': submissions}
    return render(request, 'submissions.html', context)
