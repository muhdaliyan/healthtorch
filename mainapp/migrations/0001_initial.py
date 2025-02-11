# Generated by Django 5.1.6 on 2025-02-11 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CancerPrediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GENDER', models.CharField(max_length=10)),
                ('AGE', models.IntegerField()),
                ('SMOKING', models.IntegerField()),
                ('YELLOW_FINGERS', models.IntegerField()),
                ('ANXIETY', models.IntegerField()),
                ('PEER_PRESSURE', models.IntegerField()),
                ('CHRONIC_DISEASE', models.IntegerField()),
                ('FATIGUE', models.IntegerField()),
                ('ALLERGY', models.IntegerField()),
                ('WHEEZING', models.IntegerField()),
                ('ALCOHOL_CONSUMING', models.IntegerField()),
                ('COUGHING', models.IntegerField()),
                ('SHORTNESS_OF_BREATH', models.IntegerField()),
                ('SWALLOWING_DIFFICULTY', models.IntegerField()),
                ('CHEST_PAIN', models.IntegerField()),
                ('LUNG_CANCER', models.CharField(blank=True, max_length=3, null=True)),
            ],
        ),
    ]
