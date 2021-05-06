# Generated by Django 3.2 on 2021-05-03 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(default='laku', max_length=20)),
                ('packagesize', models.CharField(default=3, max_length=20)),
                ('unitprice', models.IntegerField(default=3)),
                ('unitsinstock', models.IntegerField(default=3)),
                ('companyname', models.CharField(default='lakufirma', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(default='lakufirma', max_length=50)),
                ('contactname', models.CharField(default='Tommi', max_length=50)),
                ('address', models.CharField(default='tie 3', max_length=100)),
                ('phone', models.CharField(default='0700123123', max_length=20)),
                ('email', models.CharField(default='mika.silli@silli.com', max_length=50)),
                ('country', models.CharField(default='lakufirma', max_length=50)),
            ],
        ),
    ]
