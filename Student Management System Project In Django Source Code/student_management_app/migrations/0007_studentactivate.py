# Generated by Django 4.1.5 on 2023-01-30 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0006_alter_customuser_first_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentActivate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now=True)),
                ('activater_name', models.CharField(max_length=100)),
                ('activate_birr', models.CharField(max_length=10)),
                ('activate_status', models.IntegerField(default=0)),
                ('activate_txn', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management_app.students')),
            ],
        ),
    ]
