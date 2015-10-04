import random
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.decorators.http import require_GET
from django.utils.timezone import activate
from .models import Member, History

def home(request):
    # return HttpResponse("<p>Hello World!</p>")
    return render(request, 'draw_member/home.html')

@require_GET
def draw(request):
    # Retrieve all related members
    group_name = request.GET.get('group_name', 'ALL')
    if group_name == 'ALL':
        valid_members = Member.objects.all()
    else:
        valid_members = Member.objects.filter(group_name=group_name)
    # Raise 404 if no members are found given the group name
    if not valid_members.exists():
        raise Http404("No member in group '%s'" % group_name)
    # Lucky draw
    lucky_member = random.choice(valid_members)
    # Update history
    draw_history = History(member=lucky_member)
    draw_history.save()

    return HttpResponse("<p>{0.name}（團體：{0.group_name}）</p>".format(lucky_member))


def history(request):
    # activate('Asia/Taipei')
    recent_draws = History.objects.order_by('-time').all()[:10]
    return render(request, 'draw_member/history.html', {
        'recent_histories': recent_draws,
    })
