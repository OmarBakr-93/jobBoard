from django.shortcuts import render

# Create your views here.

def jobs(request):
    
    context ={}
    return render(request,'job/jobs.html',context)



def job_details(request,id):
    
    context ={}
    return render(request,'job/job_details.html',context)