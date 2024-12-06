from .utils import load_pickle_and_return 
#load the label , load the model , predict the output and return the result 
model = load_pickle_and_return("diseaseprediction/models/model.pkl")
label = load_pickle_and_return("diseaseprediction/models/label_encoder.pkl")

def predict_result(input):
    y_pred = model.predict(input)
    y_pred_original = label.inverse_transform(y_pred)
    return y_pred_original[0]
    