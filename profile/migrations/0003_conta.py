# Gerado por Django 4.2.3 on 2023-07-07 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0002_rename_ategoria_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apelido', models.CharField(max_length=50)),
                ('banco', models.CharField(choices=[('PA', 'PanAmericano'), ('CE', 'Caixa Economica')], max_length=2)),
                ('tipo', models.CharField(choices=[('pf', 'Pessoa Física'), ('pj', 'Pessoa Jurídica')], max_length=2)),
                ('valor', models.FloatField()),
                ('icone', models.ImageField(upload_to='icones')),
            ],
        ),
    ]
