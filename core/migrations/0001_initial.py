# Generated by Django 4.2 on 2024-03-05 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('idc', models.IntegerField(primary_key=True, serialize=False)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_department', to='core.department')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_level', to='core.level')),
                ('subject', models.ManyToManyField(related_name='student_subject', to='core.subject')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('idc', models.IntegerField(primary_key=True, serialize=False)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_department', to='core.department')),
                ('level', models.ManyToManyField(related_name='doctor_level', to='core.level')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_subject', to='core.subject')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance_student', to='core.student')),
            ],
        ),
    ]