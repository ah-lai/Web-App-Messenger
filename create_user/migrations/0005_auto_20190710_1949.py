# Generated by Django 2.2.2 on 2019-07-10 23:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('create_user', '0004_auto_20190704_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=45)),
                ('lname', models.CharField(max_length=45)),
                ('location', models.CharField(max_length=45)),
                ('phone_num', models.CharField(max_length=15, unique=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user',
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
