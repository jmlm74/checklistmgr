# Generated by Django 3.1.1 on 2020-10-23 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_checklist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklistdone',
            name='cld_remarks',
            field=models.TextField(null=True, verbose_name='Remarks'),
        ),
        migrations.AddField(
            model_name='checklistdone',
            name='cld_valid',
            field=models.BooleanField(default=False, verbose_name='Valid'),
        ),
        migrations.CreateModel(
            name='CheckListPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pho_caption', models.CharField(max_length=30, null=True, verbose_name='Caption')),
                ('pho_file', models.FileField(upload_to='photos/%Y/%m/', verbose_name='Photo')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('pho_chklst_done', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pho_chklst', to='app_checklist.checklistdone')),
            ],
        ),
    ]
