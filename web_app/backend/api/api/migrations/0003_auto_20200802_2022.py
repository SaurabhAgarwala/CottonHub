# Generated by Django 2.1.5 on 2020-08-02 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_complaint_faq_feedback'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Complaint',
        ),
        migrations.DeleteModel(
            name='FAQ',
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
    ]
