# Generated by Django 5.0 on 2024-07-12 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_director_movieinfo_directed_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='acters',
            field=models.ManyToManyField(related_name='acted_movies', to='movies.actor'),
        ),
    ]
