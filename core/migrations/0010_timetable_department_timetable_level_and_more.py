# Generated by Django 4.2 on 2024-04-19 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_timetable'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='timetables', to='core.department'),
        ),
        migrations.AddField(
            model_name='timetable',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='timetables', to='core.level'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='Timage',
            field=models.ImageField(blank=True, null=True, upload_to='time_table/'),
        ),
    ]