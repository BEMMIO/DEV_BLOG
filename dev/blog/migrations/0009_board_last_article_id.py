# Generated by Django 3.2.7 on 2021-09-12 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20210912_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='last_article_id',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='last article id'),
        ),
    ]