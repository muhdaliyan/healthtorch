import pickle
import numpy as np
from django.shortcuts import render
from .forms import CancerPredictionForm



def about(request):
    return render(request, "about.html")



model_path = "./model/svc_model.pkl"
with open(model_path, "rb") as file:
    model = pickle.load(file)

def index(request):
    prediction = None

    if request.method == "POST":
        form = CancerPredictionForm(request.POST)
        if form.is_valid():
            # Convert GENDER to numeric
            gender = 1 if form.cleaned_data['GENDER'].strip().lower() == "male" else 0

            # Ensure all values are converted to integers
            try:
                data = np.array([
                    gender,  # Fixed: Added 'GENDER' as the first feature
                    int(form.cleaned_data['AGE']),
                    int(form.cleaned_data['SMOKING']),
                    int(form.cleaned_data['YELLOW_FINGERS']),
                    int(form.cleaned_data['ANXIETY']),
                    int(form.cleaned_data['PEER_PRESSURE']),
                    int(form.cleaned_data['CHRONIC_DISEASE']),
                    int(form.cleaned_data['FATIGUE']),  # Fixed extra space
                    int(form.cleaned_data['ALLERGY']),  # Fixed extra space
                    int(form.cleaned_data['WHEEZING']),
                    int(form.cleaned_data['ALCOHOL_CONSUMING']),
                    int(form.cleaned_data['COUGHING']),
                    int(form.cleaned_data['SHORTNESS_OF_BREATH']),
                    int(form.cleaned_data['SWALLOWING_DIFFICULTY']),
                    int(form.cleaned_data['CHEST_PAIN'])
                ]).reshape(1, -1)

                print("Input Data Shape:", data.shape)  # Debugging
                print("Input Data Values:", data)  # Debugging

                # Make prediction
                prediction = model.predict(data)[0]
            except KeyError as e:
                print(f"Error: Missing field in form data - {e}")
                prediction = "Error: Missing data"
            except ValueError as e:
                print(f"Error: Invalid input format - {e}")
                prediction = "Error: Invalid data format"

    else:
        form = CancerPredictionForm()

    return render(request, "index.html", {"form": form, "prediction": prediction})

