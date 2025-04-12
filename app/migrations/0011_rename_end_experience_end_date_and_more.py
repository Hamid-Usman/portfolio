# Generated by Django 4.2.7 on 2024-05-27 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_techstack_description_remove_techstack_icon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experience',
            old_name='end',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='experience',
            old_name='job',
            new_name='job_title',
        ),
        migrations.RenameField(
            model_name='experience',
            old_name='start',
            new_name='start_date',
        ),
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='JobSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech', models.CharField(max_length=20)),
                ('Job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.experience')),
            ],
        ),
    ]
