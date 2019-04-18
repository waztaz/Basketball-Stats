# Generated by Django 2.1.5 on 2019-04-17 08:00

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import roster.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_player', models.BooleanField(default=False)),
                ('is_coach', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Analytics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BasketballStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField()),
                ('stat', models.CharField(max_length=30)),
                ('shot_location', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('coach_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('game_id', models.AutoField(primary_key=True, serialize=False)),
                ('opponent', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('team_score', models.IntegerField(default=0)),
                ('opponent_score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Lineup',
            fields=[
                ('lineup_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='LineupPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lineup_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineup', to='roster.Lineup')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player', to='roster.Lineup')),
            ],
        ),
        migrations.CreateModel(
            name='LineupScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp_entered', models.DateTimeField()),
                ('time_stamp_left', models.DateTimeField()),
                ('team_score', models.IntegerField()),
                ('opponent_score', models.IntegerField()),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roster.Game')),
                ('lineup_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roster.Lineup')),
            ],
        ),
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('play_num', models.IntegerField()),
                ('position', models.CharField(max_length=100)),
                ('action', models.CharField(max_length=100)),
                ('sequence', models.IntegerField()),
                ('screen_for', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('player_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(default='no name', max_length=100)),
                ('last_name', models.CharField(default='no name', max_length=100)),
                ('height', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=0)),
                ('position', models.CharField(choices=[(roster.models.PlayerPosition('Point Guard'), 'PG'), (roster.models.PlayerPosition('Shooting Guard'), 'SG'), (roster.models.PlayerPosition('Small Forward'), 'SF'), (roster.models.PlayerPosition('Power Forward'), 'PF'), (roster.models.PlayerPosition('Center'), 'C')], max_length=2)),
                ('year_in_school', models.CharField(choices=[(roster.models.YearInSchool('Freshman'), 'FR'), (roster.models.YearInSchool('Sophomore'), 'SO'), (roster.models.YearInSchool('Junior'), 'JR'), (roster.models.YearInSchool('Senior'), 'SR')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Scout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=100)),
                ('coach_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roster.Coach')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team_id',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='roster.Team'),
        ),
        migrations.AddField(
            model_name='player',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='play',
            name='team_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roster.Team'),
        ),
        migrations.AddField(
            model_name='lineup',
            name='center',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='center', to='roster.Player'),
        ),
        migrations.AddField(
            model_name='lineup',
            name='point_guard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='point_guard', to='roster.Player'),
        ),
        migrations.AddField(
            model_name='lineup',
            name='power_forward',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='power_forward', to='roster.Player'),
        ),
        migrations.AddField(
            model_name='lineup',
            name='shooting_guard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shooting_guard', to='roster.Player'),
        ),
        migrations.AddField(
            model_name='lineup',
            name='small_forward',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='small_forward', to='roster.Player'),
        ),
        migrations.AddField(
            model_name='game',
            name='team_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roster.Team'),
        ),
        migrations.AddField(
            model_name='basketballstat',
            name='game_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roster.Game'),
        ),
        migrations.AddField(
            model_name='basketballstat',
            name='player_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roster.Player'),
        ),
        migrations.AddField(
            model_name='analytics',
            name='player_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roster.Player'),
        ),
    ]
