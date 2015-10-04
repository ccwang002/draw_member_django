from django.db import models
from django.utils.timezone import now


class MemberGroupManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().values_list('group_name')

    def unique(self):
        return (t[0] for t in self.distinct())


class Member(models.Model):
    name = models.CharField(max_length=256)
    group_name = models.CharField(max_length=256)
    objects = models.Manager()  # preserve the default Manager

    def __str__(self):
        return '%s of %s' % (self.name, self.group_name)

    # Method 1: create a manager to handle all group-related operation
    groups = MemberGroupManager()

    # Method 2: create a new method
    @classmethod
    def unique_groups(cls):
        return (t[0] for t in cls.objects.values_list('group_name').distinct())


class History(models.Model):
    member = models.ForeignKey(Member, related_name="draw_histories")
    # We set USE_TZ=True and timezone being UTC,
    # so now() will return datetime.utcnow()
    # which is a timezone aware datetime obj
    time = models.DateTimeField(default=now)

    def __str__(self):
        return '%s at %s' % (self.member.name, self.time)
