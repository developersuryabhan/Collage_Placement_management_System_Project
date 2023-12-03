from django.shortcuts import render, redirect,get_object_or_404
from .forms import StudentForm,CompanyForm,InterviewForm,InterviewEditForm,PlacementForm,StudentEditForm
from .models import Students,Companies,Interviews,Placements

# Create your views here.
def index(reqeust):
    return render(reqeust,"index.html")


def register_student(request):
    context = dict()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Student Register Successfully."
        else:
            msg = "Something went wrong!"
        context.update({"res":msg})

    context.update({
        'form': StudentForm(),
        "students":Students.objects.all()
    })
    return render(request,"add_student.html", context)


def register_company(request):
    context = dict()
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Company Register Successfully."
        else:
            msg = "Something went wrong!"
        context.update({"res":msg})

    context.update({
        'form': CompanyForm(),
        "companies":Companies.objects.all()
    })
    return render(request, 'company_registration.html',context)


def interviews_page(request):
    context = dict()
    if request.method == 'POST':
        form = InterviewForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Interview Scheduled Successfully."
        else:
            msg = "Something went wrong!"
        context.update({"res":msg})

    context.update({
        'form': InterviewForm(),
        "intervew_data":Interviews.objects.all()
    })
    return render(request, 'interviews_page.html',context)


def interview_update(request, id):
    context = dict()
    obj = get_object_or_404(Interviews, interview_id=id)
    if request.method == 'POST':
        form = InterviewEditForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            msg = "Interview Updated Successfully."
            return redirect("/interviews")
        else:
            msg = "Something went wrong!"
        context.update({"res": msg})
    else:
        form = InterviewEditForm(instance=obj)
    context.update({
        'form': form,
        "interview_data": obj,
    })
    return render(request, "interview_update.html", context)


def placements(request):
    context = dict()
    if request.method == 'POST':
        form = PlacementForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Interview Scheduled Successfully."
        else:
            msg = "Something went wrong!"
        context.update({"res":msg})

    context.update({
        'form': PlacementForm(),
        "placements_data":Placements.objects.all()
    })
    return render(request, 'placements.html',context)


# Log________________________
def Login(request):
    return render(request,"login.html")


# Logout----------------------
def logout(self, request):
        request.session.clear()
        return redirect('login')


