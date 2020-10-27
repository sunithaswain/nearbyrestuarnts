# Generated by Django 3.1.1 on 2020-10-06 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commentuser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resturant',
            name='comment',
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_details', models.CharField(max_length=70)),
                ('timefield', models.DateTimeField()),
                ('resturant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commentuser.resturant')),
            ],
        ),
    ]
