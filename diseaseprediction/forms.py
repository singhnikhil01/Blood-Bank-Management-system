from django import forms

class SymptomPredictionForm(forms.Form):
    SYMPTOM_CHOICES = [
        ('throat_irritation', 'Throat Irritation'),
        ('redness_of_eyes', 'Redness of Eyes'),
        ('sinus_pressure', 'Sinus Pressure'),
        ('runny_nose', 'Runny Nose'),
        ('congestion', 'Congestion'),
        ('loss_of_smell', 'Loss of Smell'),
        ('increased_appetite', 'Increased Appetite'),
        ('polyuria', 'Polyuria (Frequent Urination)'),
        ('receiving_blood_transfusion', 'Receiving Blood Transfusion'),
        ('receiving_unsterile_injections', 'Receiving Unsterile Injections')
    ]
    
    symptoms = forms.MultipleChoiceField(
        choices=SYMPTOM_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )