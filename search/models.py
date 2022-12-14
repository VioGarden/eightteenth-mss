from django.db import models
from django.conf import settings


class AotData(models.Model): # Entire Song Dataset
    song = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    annid = models.IntegerField(blank=True)
    show = models.CharField(max_length=200)
    opedin = models.CharField(max_length=25)
    h720 = models.URLField(max_length=100, blank=True)
    h480 = models.URLField(max_length=100, blank=True)
    mp3 = models.URLField(max_length=100, blank=True)
    def __str__(self):
        return """Song: %s | Artist: %s | annid: %s | Show: %s | Type: %s
        """%(self.song, self.artist, self.annid, self.show, self.opedin)


class MySongUser(models.Model): # List of all Users
    MyUser = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )
    my_songs = models.ManyToManyField(AotData, through='UserList')
    def __str__(self):
        return "%s"%(self.MyUser)


class UserList(models.Model): # List of Songs that have been added by users
    ProfileUser = models.ForeignKey(MySongUser, on_delete=models.CASCADE)
    ProfileSong = models.ForeignKey(AotData, on_delete=models.CASCADE)
    ProfileScore = models.IntegerField(blank=True, null=True, unique=False)
    class Meta:
        unique_together = [['ProfileUser', 'ProfileSong']]
    def __str__(self):
        return "%s : %s"%(self.ProfileUser, self.ProfileSong.song)

