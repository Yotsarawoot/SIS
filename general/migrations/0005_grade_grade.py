# Generated by Django 4.0 on 2022-10-20 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0004_grade_gpa_alter_grade_sid_alter_grade_term_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='grade',
            field=models.FloatField(null=True),
        ),
    ]
