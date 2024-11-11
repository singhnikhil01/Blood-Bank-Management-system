# analytics/utils.py

from collections import Counter
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from patient.models import Patient
from donor.models import Donor, BloodDonate
from blood.models import BloodRequest

def demographic_analysis():
    """
    Analyzes donor and patient demographics, including age distribution, 
    common blood groups, and average ages.
    """
    patient_ages = Patient.objects.values_list('age', flat=True)
    donor_ages = Donor.objects.values_list('age', flat=True)
    patient_blood_groups = Patient.objects.values_list('bloodgroup', flat=True)
    donor_blood_groups = Donor.objects.values_list('bloodgroup', flat=True)
    
    demographics = {
        'average_patient_age': sum(patient_ages) / len(patient_ages) if patient_ages else None,
        'average_donor_age': sum(donor_ages) / len(donor_ages) if donor_ages else None,
        'common_patient_blood_groups': Counter(patient_blood_groups).most_common(),
        'common_donor_blood_groups': Counter(donor_blood_groups).most_common(),
    }
    
    return demographics

def donation_trends():
    """
    Calculates monthly blood donation totals to analyze trends over time.
    """
    donations = (
        BloodDonate.objects
        .annotate(month=TruncMonth('date'))
        .values('month')
        .annotate(total_units=Sum('unit'))
        .order_by('month')
    )
    
    return list(donations)

def request_fulfillment_rate():
    """
    Calculates blood request fulfillment rate by comparing the number of 
    fulfilled requests to total requests.
    """
    total_requests = BloodRequest.objects.count()
    fulfilled_requests = BloodRequest.objects.filter(status="Fulfilled").count()
    fulfillment_rate = (fulfilled_requests / total_requests * 100) if total_requests else 0
    
    return {
        'total_requests': total_requests,
        'fulfilled_requests': fulfilled_requests,
        'fulfillment_rate': fulfillment_rate,
    }

def disease_analysis():
    """
    Analyzes diseases associated with blood donations to identify trends 
    in patient needs based on medical conditions.
    """
    diseases = BloodDonate.objects.values_list('disease', flat=True)
    common_diseases = Counter(diseases).most_common()
    
    return common_diseases
