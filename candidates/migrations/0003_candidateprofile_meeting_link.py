# Generated by Django 5.1.6 on 2025-02-09 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0002_alter_candidateprofile_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidateprofile',
            name='meeting_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
