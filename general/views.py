from django.http.response import HttpResponse
from django.shortcuts import render
import pymongo
from .models import Grade
from .forms import GPAForm, GPAModelForm, GPAHistoryModelForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = GPAModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            std = Grade()
            std.sID = data['sID']
            std.term = data['term']
            std.year = data['year']
            print(std.sID, std.term, std.year)
            gpa = Grade.objects.get(sID=std.sID, term=std.term, year=std.year)
            print(gpa.gpa)
    else:
        form = GPAModelForm()
        gpa = Grade()
    context = {'form': form, 'gpa': gpa.gpa}
    return render(request, 'general\home.html', context)

def home1(request):
    if request.method == 'POST':
        form = GPAHistoryModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            std = Grade()
            std.sID = data['sID']
            print(std.sID)
            obj = Grade.objects.filter(sID=std.sID)
            print(obj)
            g = []
            for x in obj:
                g.append(x.gpa)
    else:
        form = GPAHistoryModelForm()
        g = ['']
    context = {'form': form, 'gpa': g}
    return render(request, 'general\home_copy.html', context)

def home2(request):
    if request.method == 'POST':
        form = GPAModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            std = Grade()
            std.sID = data['sID']
            std.term = data['term']
            std.year = data['year']
            print(std.sID, std.term, std.year)
            grade = Grade.objects.get(sID=std.sID, term=std.term, year=std.year)
            print(grade.grade)
    else:
        form = GPAModelForm()
        grade = Grade()
    context = {'form': form, 'grade': grade.grade}
    return render(request, 'general\home_copy2.html', context)

def home3(request):
    if request.method == 'POST':
        form = GPAHistoryModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            std = Grade()
            std.sID = data['sID']
            print(std.sID)
            obj2 = Grade.objects.filter(sID=std.sID)
            print(obj2)
            G = []
            for x in obj2:
                G.append(x.grade)
    else:
        form = GPAHistoryModelForm()
        G = ['']
    context = {'form': form, 'grade': G}
    return render(request, 'general\home_copy3.html', context)

def about(request):
    return HttpResponse('More General')


# client = pymongo.MongoClient("mongodb+srv://Npie:1959@cluster0.mgtsznh.mongodb.net/?retryWrites=true&w=majority")
# db = client.test


