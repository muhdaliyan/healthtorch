from django import forms
from .models import CancerPrediction

class CancerPredictionForm(forms.ModelForm):
    class Meta:
        model = CancerPrediction
        fields = '__all__'  # Include all fields except LUNG_CANCER
        widgets = {
            'GENDER': forms.Select(choices=[("Male", "Male"), ("Female", "Female")]),
            'SMOKING': forms.Select(choices=[(1, "Yes"), (0, "No")]),
            'YELLOW_FINGERS': forms.Select(choices=[(1, "Yes"), (0, "No")]),
            'ANXIETY': forms.Select(choices=[(1, "Yes"), (0, "No")]),
            'PEER_PRESSURE': forms.Select(choices=[(1, "Yes"), (0, "No")]),
            'CHRONIC_DISEASE': forms.Select(choices=[(1, "Yes"), (0, "No")]),
            'FATIGUE': forms.Select(choices=[(1, "Yes"), (0, "No")]),
            'ALLERGY': forms.Select(choices=[(1, "Yes"), (0, "No")]),
            'WHEEZING': forms.Select(choices=[(1, "Yes"), (0, "No")]),
            'ALCOHOL_CONSUMING': forms.Select(choices=[(1, "Yes"), (0, "No")]),
            'COUGHING': forms.Select(choices=[(1, "Yes"), (0, "No")]),
            'SHORTNESS_OF_BREATH': forms.Select(choices=[(1, "Yes"), (0, "No")]),
            'SWALLOWING_DIFFICULTY': forms.Select(choices=[(1, "Yes"), (0, "No")]),
            'CHEST_PAIN': forms.Select(choices=[(1, "Yes"), (0, "No")]),
        }
