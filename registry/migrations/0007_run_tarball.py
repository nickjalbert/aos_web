# Generated by Django 3.2.7 on 2021-09-14 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registry", "0006_auto_20210914_0834"),
    ]

    operations = [
        migrations.AddField(
            model_name="run",
            name="tarball",
            field=models.FileField(null=True, upload_to="tarballs/"),
        ),
    ]