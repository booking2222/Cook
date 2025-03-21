# Generated by Django 5.1 on 2025-03-15 09:45

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=100)),
                ('receiver', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('media', models.FileField(blank=True, null=True, upload_to='chat_media/')),
            ],
        ),
        migrations.CreateModel(
            name='chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('applied', 'Applied'), ('approved', 'Approved'), ('reject', 'Reject')], default='Applied', max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='chefimages/')),
                ('username', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=128)),
                ('place', models.CharField(max_length=128)),
                ('languages_spoken', models.CharField(max_length=128)),
                ('experience', models.CharField(max_length=128)),
                ('signature_dishes', models.CharField(max_length=500)),
                ('service_area', models.CharField(max_length=500)),
                ('primary_cuisines', models.CharField(max_length=300)),
                ('services_offered', models.CharField(max_length=500)),
                ('certifications', models.FileField(blank=True, null=True, upload_to='chef_certifications/')),
                ('work_hours_and_days', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Chefrecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('name', models.CharField(max_length=100)),
                ('specializations', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=500)),
                ('video', models.FileField(blank=True, null=True, upload_to='video/')),
            ],
        ),
        migrations.CreateModel(
            name='decorations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('timeduration', models.IntegerField(blank=True, null=True)),
                ('event', models.CharField(blank=True, max_length=255, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank='True', null='True', upload_to='decorimage/')),
                ('description', models.TextField(blank=True, null=True)),
                ('selected_utensils', models.JSONField(blank=True, default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('applied', 'Applied'), ('approved', 'Approved'), ('reject', 'Reject')], default='Applied', max_length=20)),
                ('image', models.ImageField(blank='True', null='True', upload_to='image/')),
                ('username', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=128)),
                ('place', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_text', models.TextField()),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=128)),
                ('place', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='deccart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('rdate', models.DateField()),
                ('time', models.TimeField()),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('Paid', 'Paid'), ('refund', 'refund'), ('Rejected', 'Rejected')], default='Pending', max_length=10, null=True)),
                ('selected_utensils', models.JSONField(blank=True, default=dict)),
                ('decoration', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EVENT_BOOKING.decorations')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EVENT_BOOKING.event')),
            ],
        ),
        migrations.CreateModel(
            name='decorationtransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razorpay_order_id', models.CharField(max_length=100)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.IntegerField()),
                ('status', models.CharField(default='Created', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EVENT_BOOKING.deccart')),
            ],
        ),
        migrations.CreateModel(
            name='eventsupdates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=60, null=True)),
                ('packagename', models.CharField(blank=True, max_length=60, null=True)),
                ('chefname', models.CharField(blank=True, max_length=60, null=True)),
                ('chefimage', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('details', models.CharField(blank=True, max_length=300, null=True)),
                ('fromdate', models.DateField(blank=True, null=True)),
                ('todate', models.DateField(blank=True, null=True)),
                ('rentperday', models.IntegerField(blank=True, null=True)),
                ('package', models.DateField(blank=True, null=True)),
                ('chef', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EVENT_BOOKING.chef')),
            ],
        ),
        migrations.CreateModel(
            name='icart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveBigIntegerField(blank=True, default=1, null=True)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('status', models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=10, null=True)),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EVENT_BOOKING.eventsupdates')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EVENT_BOOKING.event')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'paid'), ('refund', 'refund')], default='Pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EVENT_BOOKING.event')),
            ],
        ),
        migrations.CreateModel(
            name='Paymentd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EVENT_BOOKING.event')),
                ('utensils', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EVENT_BOOKING.decorations')),
            ],
        ),
        migrations.CreateModel(
            name='refund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refdes', models.TextField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('refund', 'refund'), ('Rejected', 'Rejected')], default='Pending', max_length=10)),
                ('transact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EVENT_BOOKING.payment')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveBigIntegerField(default=1)),
                ('order_id', models.CharField(max_length=225)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EVENT_BOOKING.eventsupdates')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EVENT_BOOKING.event')),
            ],
        ),
        migrations.CreateModel(
            name='Utensilsform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('date', models.DateField()),
                ('rdate', models.DateField()),
                ('time', models.TimeField()),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'paid'), ('refund', 'refund')], default='Pending', max_length=10)),
                ('selected_utensils', models.JSONField(blank=True, default=dict)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EVENT_BOOKING.event')),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='utensils',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EVENT_BOOKING.utensilsform'),
        ),
    ]
