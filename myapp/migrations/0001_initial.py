# Generated by Django 3.1.7 on 2021-03-25 06:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('date', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('start_time', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('end_time', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('description', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('street', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('barangay', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('city', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('province', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('upvotes', models.IntegerField(default=0)),
                ('venue', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('category', models.CharField(blank=True, default='', max_length=32, null=True)),
                ('status_event', models.CharField(default='reviewing', max_length=32)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Event',
            },
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('started_organizer_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Organizer',
            },
        ),
        migrations.CreateModel(
            name='UserReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('sex', models.CharField(blank=True, max_length=10, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('email_address', models.CharField(blank=True, max_length=50, null=True)),
                ('birth_date', models.DateField(default=datetime.datetime(2021, 3, 25, 14, 57, 43, 859768), null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_id', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'UserReg',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_all_reviews', to='myapp.event')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_all_authored_reviews', to='myapp.userreg')),
            ],
            options={
                'db_table': 'Review',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(blank=True, max_length=128, null=True)),
                ('request_type', models.CharField(blank=True, max_length=128, null=True)),
                ('status_request', models.CharField(default='reviewing', max_length=128)),
                ('description', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('remarks', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='received_requests', to='myapp.event')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_requests', to='myapp.userreg')),
            ],
            options={
                'db_table': 'Request',
            },
        ),
        migrations.CreateModel(
            name='OrganizerEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roles', models.CharField(blank=True, default='', max_length=64, null=True)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='handled_by', to='myapp.event')),
                ('organizer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='handled_organizer_events', to='myapp.organizer')),
            ],
            options={
                'db_table': 'Organizer_Event',
            },
        ),
        migrations.AddField(
            model_name='organizer',
            name='custom_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organizer', to='myapp.userreg'),
        ),
        migrations.CreateModel(
            name='EventUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_voted', models.BooleanField(default=False)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_all_participants', to='myapp.event')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_all_joined_events', to='myapp.userreg')),
            ],
            options={
                'db_table': 'Event_User',
            },
        ),
        migrations.CreateModel(
            name='EventNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remind_at', models.DateTimeField(blank=True, null=True)),
                ('remind_details', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_notifications', to='myapp.event')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_notifications', to='myapp.userreg')),
            ],
            options={
                'db_table': 'Event_Notification',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='organizer_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='handled_events', to='myapp.organizer'),
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_admin_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('custom_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin', to='myapp.userreg')),
            ],
            options={
                'db_table': 'Admin',
            },
        ),
    ]
