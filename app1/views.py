from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils import timezone

from app1.signals import work_done


def index(request, template_name):
    if not User.objects.exists():
        User.objects.create_user(username='user')
    # 发送信号，将请求的url地址和时间一并传递过去
    work_done.send(User, path=request.path, time=timezone.now().strftime("%Y-%m-%d %H:%M:%S"))
    return render(request, template_name, locals())
