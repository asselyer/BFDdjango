# Generated by Django 2.1.2 on 2018-10-08 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20181007_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='name')),
                ('text', models.TextField(max_length=500, verbose_name='text')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='posts.Post', verbose_name='Post')),
            ],
            options={
                'verbose_name': 'коммент',
                'verbose_name_plural': 'комменты',
            },
        ),
    ]