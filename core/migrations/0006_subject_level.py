# Generated by Django 4.2 on 2024-04-12 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_doctor_subject_doctor_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject_level', to='core.level'),
        ),
    ]
