from django.db import models

class CancerPrediction(models.Model):
    GENDER = models.CharField(max_length=10)  # Male/Female
    AGE = models.IntegerField()
    SMOKING = models.BooleanField(default=False)
    YELLOW_FINGERS = models.BooleanField(default=False)
    ANXIETY = models.BooleanField(default=False)
    PEER_PRESSURE = models.BooleanField(default=False)
    CHRONIC_DISEASE = models.BooleanField(default=False)
    FATIGUE = models.BooleanField(default=False)
    ALLERGY = models.BooleanField(default=False)
    WHEEZING = models.BooleanField(default=False)
    ALCOHOL_CONSUMING = models.BooleanField(default=False)
    COUGHING = models.BooleanField(default=False)
    SHORTNESS_OF_BREATH = models.BooleanField(default=False)
    SWALLOWING_DIFFICULTY = models.BooleanField(default=False)
    CHEST_PAIN = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.GENDER} - {self.AGE}"
