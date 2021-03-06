# Generated by Django 3.1.7 on 2021-03-23 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('D3App', '0005_auto_20210321_0758'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bubble',
            options={'verbose_name': 'Bubbles'},
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('text', models.CharField(default='Name of the event', max_length=200)),
                ('bubble', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='D3App.bubble')),
                ('ev', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='D3App.event')),
            ],
        ),
    ]
