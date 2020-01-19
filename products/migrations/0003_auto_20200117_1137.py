# Generated by Django 3.0.1 on 2020-01-17 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_auto_20200107_1638'),
        ('products', '0002_auto_20200107_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='category.Category'),
        ),
    ]