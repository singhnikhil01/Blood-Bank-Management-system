# analytics/views.py
from django.shortcuts import render
from .prediction import predict_blood_demand

def demand_forecast(request):
    blood_types = ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']
    predictions = {blood_type: predict_blood_demand(blood_type) for blood_type in blood_types}
    return render(request, 'analytics/demand_forecast.html', {'predictions': predictions})
