
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ategoria',
            new_name='categoria',
        ),
    ]
