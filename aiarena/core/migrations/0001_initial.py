# Generated by Django 3.0.8 on 2020-12-18 21:46

import aiarena.core.models.bot
import aiarena.core.models.map
import aiarena.core.models.match_participation
import aiarena.core.models.mixins
import aiarena.core.models.result
import aiarena.core.models.season_participation
import aiarena.core.storage
import aiarena.core.validators
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import private_storage.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelativeResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField()),
                ('result', models.CharField(choices=[('none', 'None'), ('win', 'Win'), ('loss', 'Loss'), ('tie', 'Tie')], max_length=32)),
                ('result_cause', models.CharField(choices=[('game_rules', 'Game Rules'), ('crash', 'Crash'), ('timeout', 'Timeout'), ('race_mismatch', 'Race Mismatch'), ('match_cancelled', 'Match Cancelled'), ('initialization_failure', 'Initialization Failure'), ('error', 'Error')], max_length=32)),
                ('elo_change', models.SmallIntegerField()),
                ('avg_step_time', models.FloatField()),
                ('game_time_formatted', models.CharField(max_length=32)),
                ('game_steps', models.IntegerField()),
                ('replay_file', models.FileField(upload_to='')),
                ('match_log', private_storage.fields.PrivateFileField(storage=aiarena.core.storage.OverwritePrivateStorage(base_url='/'), upload_to='')),
            ],
            options={
                'managed': False,
            },
        ),
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
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('patreon_level', models.CharField(choices=[('none', 'None'), ('bronze', 'Bronze'), ('silver', 'Silver'), ('gold', 'Gold'), ('platinum', 'Platinum'), ('diamond', 'Diamond')], default='none', max_length=16)),
                ('type', models.CharField(choices=[('WEBSITE_USER', 'Website User'), ('ARENA_CLIENT', 'Arena Client'), ('SERVICE', 'Service')], default='WEBSITE_USER', max_length=16)),
                ('extra_active_bots_per_race', models.IntegerField(default=0)),
                ('extra_periodic_match_requests', models.IntegerField(default=0)),
                ('receive_email_comms', models.BooleanField(default=True)),
                ('sync_patreon_status', models.BooleanField(default=True)),
                ('can_request_games_for_another_authors_bot', models.BooleanField(default=False)),
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
            name='Bot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z\\._\\-]*$', 'Only alphanumeric (A-Z, a-z, 0-9), period (.), underscore (_) and hyphen (-) characters are allowed.')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('bot_zip', private_storage.fields.PrivateFileField(storage=aiarena.core.storage.OverwritePrivateStorage(base_url='/'), upload_to=aiarena.core.models.bot.bot_zip_upload_to, validators=[aiarena.core.validators.validate_bot_zip_file])),
                ('bot_zip_updated', models.DateTimeField(editable=False)),
                ('bot_zip_md5hash', models.CharField(editable=False, max_length=32)),
                ('bot_zip_publicly_downloadable', models.BooleanField(default=False)),
                ('bot_data_enabled', models.BooleanField(default=True)),
                ('bot_data', private_storage.fields.PrivateFileField(blank=True, null=True, storage=aiarena.core.storage.OverwritePrivateStorage(base_url='/'), upload_to=aiarena.core.models.bot.bot_data_upload_to)),
                ('bot_data_md5hash', models.CharField(editable=False, max_length=32, null=True)),
                ('bot_data_publicly_downloadable', models.BooleanField(default=False)),
                ('plays_race', models.CharField(choices=[('T', 'Terran'), ('Z', 'Zerg'), ('P', 'Protoss'), ('R', 'Random')], max_length=1)),
                ('type', models.CharField(choices=[('cppwin32', 'cppwin32'), ('cpplinux', 'cpplinux'), ('dotnetcore', 'dotnetcore'), ('java', 'java'), ('nodejs', 'nodejs'), ('python', 'python')], max_length=32)),
                ('game_display_id', models.UUIDField(default=uuid.uuid4)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bots', to=settings.AUTH_USER_MODEL)),
            ],
            bases=(models.Model, aiarena.core.models.mixins.LockableModelMixin),
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('file', models.FileField(storage=aiarena.core.storage.OverwriteStorage(), upload_to=aiarena.core.models.map.map_file_upload_to)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('started', models.DateTimeField(blank=True, db_index=True, editable=False, null=True)),
                ('require_trusted_arenaclient', models.BooleanField(default=True)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='assigned_matches', to=settings.AUTH_USER_MODEL)),
                ('map', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Map')),
                ('requested_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='requested_matches', to=settings.AUTH_USER_MODEL)),
            ],
            bases=(models.Model, aiarena.core.models.mixins.LockableModelMixin, aiarena.core.models.mixins.RandomManagerMixin),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.TextField(blank=True, max_length=40, null=True)),
                ('text', models.TextField(max_length=500)),
                ('yt_link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, editable=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_opened', models.DateTimeField(blank=True, null=True)),
                ('date_closed', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('created', 'Created'), ('paused', 'Paused'), ('open', 'Open'), ('closing', 'Closing'), ('closed', 'Closed')], default='created', max_length=16)),
                ('previous_season_files_cleaned', models.BooleanField(default=False)),
            ],
            bases=(models.Model, aiarena.core.models.mixins.LockableModelMixin),
        ),
        migrations.CreateModel(
            name='TrophyIcon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('image', models.ImageField(upload_to='trophy_images/')),
            ],
        ),
        migrations.CreateModel(
            name='ArenaClient',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('trusted', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arenaclients', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('core.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='WebsiteNotice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('display', models.BooleanField(default=True)),
                ('posted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trophy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('bot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Bot')),
                ('icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.TrophyIcon')),
            ],
        ),
        migrations.CreateModel(
            name='SeasonParticipation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elo', models.SmallIntegerField(default=1600)),
                ('match_count', models.IntegerField(default=0)),
                ('win_perc', models.FloatField(blank=True, null=True, validators=[aiarena.core.validators.validate_not_nan, aiarena.core.validators.validate_not_inf])),
                ('win_count', models.IntegerField(default=0)),
                ('loss_perc', models.FloatField(blank=True, null=True, validators=[aiarena.core.validators.validate_not_nan, aiarena.core.validators.validate_not_inf])),
                ('loss_count', models.IntegerField(default=0)),
                ('tie_perc', models.FloatField(blank=True, null=True, validators=[aiarena.core.validators.validate_not_nan, aiarena.core.validators.validate_not_inf])),
                ('tie_count', models.IntegerField(default=0)),
                ('crash_perc', models.FloatField(blank=True, null=True, validators=[aiarena.core.validators.validate_not_nan, aiarena.core.validators.validate_not_inf])),
                ('crash_count', models.IntegerField(default=0)),
                ('elo_graph', models.FileField(blank=True, null=True, storage=aiarena.core.storage.OverwriteStorage(), upload_to=aiarena.core.models.season_participation.elo_graph_upload_to)),
                ('highest_elo', models.IntegerField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=255)),
                ('bot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Bot')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Season')),
            ],
            bases=(models.Model, aiarena.core.models.mixins.LockableModelMixin),
        ),
        migrations.CreateModel(
            name='SeasonBotMatchupStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_count', models.IntegerField(blank=True, null=True)),
                ('win_count', models.IntegerField(blank=True, null=True)),
                ('win_perc', models.FloatField(blank=True, null=True, validators=[aiarena.core.validators.validate_not_nan, aiarena.core.validators.validate_not_inf])),
                ('loss_count', models.IntegerField(blank=True, null=True)),
                ('loss_perc', models.FloatField(blank=True, null=True, validators=[aiarena.core.validators.validate_not_nan, aiarena.core.validators.validate_not_inf])),
                ('tie_count', models.IntegerField(blank=True, null=True)),
                ('tie_perc', models.FloatField(blank=True, null=True, validators=[aiarena.core.validators.validate_not_nan, aiarena.core.validators.validate_not_inf])),
                ('crash_count', models.IntegerField(blank=True, null=True)),
                ('crash_perc', models.FloatField(blank=True, null=True, validators=[aiarena.core.validators.validate_not_nan, aiarena.core.validators.validate_not_inf])),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('bot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='season_matchup_stats', to='core.SeasonParticipation')),
                ('opponent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opponent_matchup_stats', to='core.SeasonParticipation')),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, editable=False)),
                ('started', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('finished', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('complete', models.BooleanField(default=False)),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Season')),
            ],
            bases=(models.Model, aiarena.core.models.mixins.LockableModelMixin),
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('MatchCancelled', 'MatchCancelled'), ('InitializationError', 'InitializationError'), ('Error', 'Error'), ('Player1Win', 'Player1Win'), ('Player1Crash', 'Player1Crash'), ('Player1TimeOut', 'Player1TimeOut'), ('Player1RaceMismatch', 'Player1RaceMismatch'), ('Player1Surrender', 'Player1Surrender'), ('Player2Win', 'Player2Win'), ('Player2Crash', 'Player2Crash'), ('Player2TimeOut', 'Player2TimeOut'), ('Player2RaceMismatch', 'Player2RaceMismatch'), ('Player2Surrender', 'Player2Surrender'), ('Tie', 'Tie')], db_index=True, max_length=32)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('replay_file', models.FileField(blank=True, null=True, upload_to=aiarena.core.models.result.replay_file_upload_to)),
                ('game_steps', models.IntegerField(db_index=True)),
                ('arenaclient_log', models.FileField(blank=True, null=True, upload_to=aiarena.core.models.result.arenaclient_log_upload_to)),
                ('interest_rating', models.FloatField(blank=True, db_index=True, null=True)),
                ('date_interest_rating_calculated', models.DateTimeField(blank=True, null=True)),
                ('replay_file_has_been_cleaned', models.BooleanField(default=False)),
                ('arenaclient_log_has_been_cleaned', models.BooleanField(default=False)),
                ('match', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='result', to='core.Match')),
                ('submitted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='submitted_results', to=settings.AUTH_USER_MODEL)),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='matches_won', to='core.Bot')),
            ],
            bases=(models.Model, aiarena.core.models.mixins.LockableModelMixin),
        ),
        migrations.CreateModel(
            name='MatchParticipation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant_number', models.PositiveSmallIntegerField()),
                ('starting_elo', models.SmallIntegerField(null=True)),
                ('resultant_elo', models.SmallIntegerField(null=True)),
                ('elo_change', models.SmallIntegerField(null=True)),
                ('match_log', private_storage.fields.PrivateFileField(blank=True, null=True, storage=aiarena.core.storage.OverwritePrivateStorage(base_url='/'), upload_to=aiarena.core.models.match_participation.match_log_upload_to)),
                ('avg_step_time', models.FloatField(blank=True, null=True, validators=[aiarena.core.validators.validate_not_nan, aiarena.core.validators.validate_not_inf])),
                ('result', models.CharField(blank=True, choices=[('none', 'None'), ('win', 'Win'), ('loss', 'Loss'), ('tie', 'Tie')], max_length=32, null=True)),
                ('result_cause', models.CharField(blank=True, choices=[('game_rules', 'Game Rules'), ('crash', 'Crash'), ('timeout', 'Timeout'), ('race_mismatch', 'Race Mismatch'), ('match_cancelled', 'Match Cancelled'), ('initialization_failure', 'Initialization Failure'), ('error', 'Error')], max_length=32, null=True)),
                ('use_bot_data', models.BooleanField(default=True)),
                ('update_bot_data', models.BooleanField(default=True)),
                ('match_log_has_been_cleaned', models.BooleanField(default=True)),
                ('bot', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Bot')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Match')),
            ],
            bases=(models.Model, aiarena.core.models.mixins.LockableModelMixin),
        ),
        migrations.AddField(
            model_name='match',
            name='round',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Round'),
        ),
        migrations.CreateModel(
            name='ArenaClientStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('idle', 'Idle'), ('starting_game', 'Starting Game'), ('playing_game', 'In Game'), ('submitting_result', 'Submitting Result')], max_length=17)),
                ('logged_at', models.DateTimeField(auto_now_add=True)),
                ('arenaclient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statuses', to='core.ArenaClient')),
            ],
        ),
    ]
