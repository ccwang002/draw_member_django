from django.db import models
from django.utils.timezone import now


class MemberQuerySet(models.QuerySet):

    def unique_groups(self):
        return self.values_list('group_name', flat=True).distinct()


class Member(models.Model):
    name = models.CharField(max_length=256)
    group_name = models.CharField(max_length=256)
    objects = MemberQuerySet.as_manager()

    def __str__(self):
        return '%s of %s' % (self.name, self.group_name)


class HistoryQuerySet(models.QuerySet):

    def recent(self, n):
        return self.order_by('-time')[:n]


class History(models.Model):
    member = models.ForeignKey(Member, related_name="draw_histories")
    # We set USE_TZ=True and timezone being UTC,
    # so now() will return datetime.utcnow()
    # which is a timezone aware datetime obj
    time = models.DateTimeField(default=now)
    objects = HistoryQuerySet.as_manager()

    def __str__(self):
        return '%s at %s' % (self.member.name, self.time)
