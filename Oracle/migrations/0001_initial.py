# Generated by Django 3.2.8 on 2021-11-19 17:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('datestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('datestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, default='None', max_length=100, null=True)),
                ('lname', models.CharField(blank=True, default='None', max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, default='None', max_length=100, null=True)),
                ('dob', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('cnic', models.CharField(default=0, max_length=16)),
                ('housestreet', models.CharField(blank=True, default='None', max_length=100, null=True)),
                ('city', models.CharField(blank=True, default='None', max_length=100, null=True)),
                ('country', models.CharField(blank=True, default='None', max_length=100, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='fault.jpg', null=True, upload_to='profiles')),
                ('salary', models.IntegerField(blank=True, default=0, null=True)),
                ('email', models.CharField(blank=True, default='None', max_length=100, null=True)),
                ('joining', models.DateTimeField(auto_now_add=True, null=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Oracle.department')),
                ('designation', models.ManyToManyField(blank=True, to='Oracle.Designation')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('datestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('datestamp', models.DateTimeField(null=True)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Oracle.employee')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Oracle.taskstatus')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100, null=True)),
                ('lname', models.CharField(max_length=100, null=True)),
                ('profile_pic', models.ImageField(default='clients/linuxghost.jpg', null=True, upload_to='clients')),
                ('mobile', models.CharField(max_length=100, null=True)),
                ('cnic', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('username', models.CharField(max_length=100, null=True, unique=True)),
                ('password', models.CharField(max_length=100, null=True)),
                ('bill', models.IntegerField(null=True, unique=True)),
                ('wire', models.BooleanField(default=True)),
                ('router', models.BooleanField(default=True)),
                ('reference', models.CharField(max_length=200, null=True)),
                ('due', models.IntegerField(null=True)),
                ('datestamp', models.DateTimeField(auto_now_add=True)),
                ('package', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Oracle.package')),
            ],
        ),
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billA', models.IntegerField(null=True)),
                ('discount', models.IntegerField(null=True)),
                ('datestamp', models.DateTimeField(default=datetime.datetime(2021, 11, 19, 22, 22, 6, 98022), null=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='Oracle.client', to_field='username')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Oracle.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Half Time', 'Half Time'), ('Leave', 'Leave')], max_length=100, null=True)),
                ('datestamp', models.DateTimeField(default=datetime.datetime(2021, 11, 19, 22, 22, 6, 94015), null=True)),
                ('month', models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], default='November', max_length=100, null=True)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Oracle.employee')),
            ],
        ),
    ]
