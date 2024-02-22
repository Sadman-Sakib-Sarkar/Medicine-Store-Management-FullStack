# Generated by Django 5.0.2 on 2024-02-22 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicineStore', '0003_alter_prescription_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='medicines',
            field=models.ManyToManyField(blank=True, through='medicineStore.OrderedMedicine', to='medicineStore.medicine'),
        ),
    ]
