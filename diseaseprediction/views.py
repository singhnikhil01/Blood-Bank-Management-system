import requests
from django.shortcuts import render
from django.conf import settings
from .forms import SymptomPredictionForm
from .prediction import predict_result
import numpy as np
import pandas as pd

def predict_disease(request):
    prediction_result = None
    
    if request.method == 'POST':
        form = SymptomPredictionForm(request.POST)
        if form.is_valid():
            selected_symptoms = form.cleaned_data.get('symptoms', [])
            symptom_status = [0] * len(SymptomPredictionForm.SYMPTOM_CHOICES)
            for idx, (key, _) in enumerate(SymptomPredictionForm.SYMPTOM_CHOICES):
                if key in selected_symptoms:
                    symptom_status[idx] = 1
            
            symptom_status = pd.DataFrame([symptom_status])
           
            prediction_result = predict_result(symptom_status)
            
    else:
        form = SymptomPredictionForm()
    
    return form , prediction_result