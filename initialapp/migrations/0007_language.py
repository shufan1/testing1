# Generated by Django 2.0.5 on 2018-05-24 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initialapp', '0006_delete_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(help_text='Enter the language of this book', max_length=20)),
            ],
        ),
    ]
