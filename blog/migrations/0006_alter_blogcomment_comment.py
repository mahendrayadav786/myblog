# Generated by Django 4.0.2 on 2022-02-15 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blogcomment_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='comment',
            field=models.TextField(),
        ),
    ]
