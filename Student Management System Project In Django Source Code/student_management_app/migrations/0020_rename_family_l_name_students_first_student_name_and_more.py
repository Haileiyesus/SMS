# Generated by Django 4.1.5 on 2023-02-04 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0019_logintype_activate_type_logintype_insert_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='family_l_name',
            new_name='first_student_name',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='family_m_name',
            new_name='last_student_name',
        ),
        migrations.RemoveField(
            model_name='students',
            name='family_name',
        ),
        migrations.RemoveField(
            model_name='students',
            name='phone_no',
        ),
    ]
