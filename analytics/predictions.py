# analytics/prediction.py
import pandas as pd
from .models import BloodDemandData

def predict_blood_demand(bloodgroup, days=30):
    # Retrieve historical data for a specific blood type
    data = BloodDemandData.objects.filter(bloodgroup=bloodgroup).order_by('date')
    df = pd.DataFrame.from_records(data.values('date', 'requests'))
    
    # Calculate moving average for the demand prediction
    df['moving_average'] = df['requests'].rolling(window=days).mean()
    predicted_demand = df['moving_average'].iloc[-1]  # Last value in moving average as prediction
    
    return predicted_demand
