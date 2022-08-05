from django.shortcuts import render, HttpResponse
import pickle
import os 
# from datetime import datetime
# from home.models import Contact
# from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable1":"Harry is great",
        "variable2":"Rohan is great"
    } 
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")

def result(request):
    model = pickle.load(open('model.pkl','rb'))
    age = request.GET['Age']
    bmi = request.GET['BMI']
    children = request.GET['Children']
    sex = request.GET['Sex']
    smoker = request.GET['smoke']
    region = request.GET['region']
   
    res = model.predict([[age,bmi,children,sex,smoker,region]])
    print(res)
   
    return HttpResponse(res)
    
    # return render(request, 'result.html')
