# Generated by Django 4.1.7 on 2023-03-31 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_board_input_type_alter_board_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='result_text',
        ),
    ]
