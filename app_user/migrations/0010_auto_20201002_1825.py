# Generated by Django 3.1.1 on 2020-10-02 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0009_collection_collectiontitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collectiontitle',
            name='collection',
        ),
        migrations.DeleteModel(
            name='Collection',
        ),
        migrations.DeleteModel(
            name='CollectionTitle',
        ),
    ]
