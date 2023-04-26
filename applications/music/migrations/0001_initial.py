# Generated by Django 2.2.6 on 2023-04-26 14:51

import applications.music.utils
import applications.music.validators
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='专辑名称')),
                ('all_artist_ids', django_mysql.models.ListTextField(models.IntegerField(), default=list, size=None)),
                ('max_year', models.IntegerField(default=0)),
                ('song_count', models.IntegerField(default=-1, verbose_name='歌曲统计')),
                ('plays_count', models.IntegerField(default=0, verbose_name='播放次数')),
                ('duration', models.FloatField(default=0, verbose_name='歌曲时长s')),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('accessed_date', models.DateTimeField(null=True, verbose_name='访问时间')),
                ('full_text', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('size', models.IntegerField(default=0, verbose_name='文件大小')),
                ('comment', models.CharField(max_length=255, null=True)),
                ('paths', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(default='', max_length=255, null=True)),
                ('mbz_album_id', models.CharField(max_length=255, null=True)),
                ('mbz_album_artist_id', models.CharField(max_length=255, null=True)),
                ('mbz_album_type', models.CharField(max_length=255, null=True)),
                ('mbz_album_comment', models.CharField(max_length=255, null=True)),
                ('external_url', models.CharField(default='', max_length=255, null=True)),
                ('external_info_updated_at', models.DateTimeField(null=True)),
            ],
            options={
                'verbose_name': '专辑',
                'verbose_name_plural': '专辑',
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('album_count', models.IntegerField(default=0)),
                ('full_text', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('order_artist_name', models.CharField(blank=True, max_length=255, null=True)),
                ('sort_artist_name', models.CharField(blank=True, max_length=255, null=True)),
                ('song_count', models.IntegerField(blank=True, default=0, null=True)),
                ('size', models.IntegerField(blank=True, default=0, null=True)),
                ('mbz_artist_id', models.CharField(blank=True, max_length=255, null=True)),
                ('small_image_url', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('medium_image_url', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('large_image_url', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('similar_artists', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('external_url', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('external_info_updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '艺术家',
                'verbose_name_plural': '艺术家',
            },
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, max_length=500, null=True)),
                ('creation_date', models.DateTimeField(default=datetime.datetime.now)),
                ('last_fetch_date', models.DateTimeField(blank=True, null=True)),
                ('size', models.IntegerField(blank=True, null=True)),
                ('mimetype', models.CharField(blank=True, max_length=200, null=True)),
                ('file', models.ImageField(max_length=255, upload_to=applications.music.utils.get_file_path, validators=[applications.music.validators.ImageDimensionsValidator(min_height=50, min_width=50), applications.music.validators.FileValidator(allowed_extensions=['png', 'jpg', 'jpeg'], max_size=5242880)])),
            ],
            options={
                'verbose_name': '附件',
                'verbose_name_plural': '附件',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': '风格',
                'verbose_name_plural': '风格',
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('path', models.CharField(default='', max_length=255)),
                ('has_cover_art', models.BooleanField(default=False)),
                ('track_number', models.IntegerField(default=0)),
                ('disc_number', models.IntegerField(default=0)),
                ('plays_count', models.IntegerField(default=0, null=True, verbose_name='播放量')),
                ('year', models.IntegerField(default=0, null=True)),
                ('size', models.IntegerField(default=0, verbose_name='文件大小')),
                ('suffix', models.CharField(default='', max_length=255, null=True, verbose_name='后缀')),
                ('mimetype', models.CharField(default='', max_length=255, null=True)),
                ('duration', models.FloatField(default=0, verbose_name='歌曲时长s')),
                ('bit_rate', models.IntegerField(default=0, null=True)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('accessed_date', models.DateTimeField(null=True, verbose_name='访问时间')),
                ('full_text', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('comment', models.TextField(null=True)),
                ('lyrics', models.TextField(null=True)),
                ('mbz_track_id', models.CharField(default='', max_length=255)),
                ('mbz_album_id', models.CharField(default='', max_length=255)),
                ('mbz_artist_id', models.CharField(default='', max_length=255)),
                ('mbz_album_artist_id', models.CharField(default='', max_length=255)),
                ('mbz_album_type', models.CharField(default='', max_length=255)),
                ('mbz_album_comment', models.CharField(default='', max_length=255)),
                ('mbz_release_track_id', models.CharField(default='', max_length=255)),
                ('album', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tracks', to='music.Album')),
                ('artist', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tracks', to='music.Artist')),
                ('genre', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tracks', to='music.Genre')),
            ],
            options={
                'verbose_name': '歌曲',
                'verbose_name_plural': '歌曲',
            },
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('creation_date', models.DateTimeField(default=datetime.datetime.now)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('privacy_level', models.CharField(choices=[('me', 'Only me'), ('followers', 'Me and my followers'), ('instance', 'Everyone on my instance, and my followers'), ('everyone', 'Everyone, including people on other instances')], default='instance', max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlists', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='attachment_cover',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='artist_cover', to='music.Attachment'),
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='albums', to='music.Artist'),
        ),
        migrations.AddField(
            model_name='album',
            name='attachment_cover',
            field=models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='album_cover', to='music.Attachment'),
        ),
        migrations.AddField(
            model_name='album',
            name='genre',
            field=models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='albums', to='music.Genre'),
        ),
        migrations.CreateModel(
            name='TrackFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(default=datetime.datetime.now)),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='track_favorites', to='music.Track')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='track_favorites', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-creation_date',),
                'unique_together': {('track', 'user')},
            },
        ),
    ]
