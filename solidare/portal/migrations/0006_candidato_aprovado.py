# Generated by Django 5.2 on 2025-04-19 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portal", "0005_candidato_senha"),
    ]

    operations = [
        migrations.AddField(
            model_name="candidato",
            name="aprovado",
            field=models.BooleanField(default=False),
        ),
    ]
