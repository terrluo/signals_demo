#!/usr/bin/python
"""
在web开发中, 你可能会遇到下面这种场景:
在用户完成某个操作后, 自动去执行一些后续的操作. 譬如用户完成修改密码后,你要发送一份确认邮件

观察者模式：观察者模式(Observer)完美的将观察者和被观察的对象分离开。
    举个例子，用户界面可以作为一个观察者，业务数据是被观察者，
    用户界面观察业务数据的变化，发现数据变化后，就显示在界面上

两个重要的对象：sender 和 receiver
    sender dispatch a signal, receiver receive signal and do something
    sender 是一个object, receiver是一个方法，或者对象的方法
    将sender和receiver关联起来是通过signal dispatchers, 即Signal.connect()方法来关联sender,receiver

注册信号不应该在app的models或者根目录，django建议我们将signals放到config里面
"""
import logging

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from app1.models import App

logger = logging.getLogger(__name__)


def create_app_v1(sender, instance, **kwargs):
    """
    在mode对象执行save函数时，就会触发该信号

    create_app_v1是receiver，User是sender, post_save是signal, 上面代码可以理解成：

        当User对象执行save函数后，就会执行create_app_v1函数

    如果去掉post_save.connect的sender参数，如： post_save.connect(create_app_v1)，
    则就是任意一个model执行了save函数，都会调用create_app_v1函数

    :param sender:
    :param instance: instance参数就是sender的实例化对象
    :param kwargs:
    :return:
    """
    logger.info('create_app_v1 收到 post_save 信号')
    logger.info('instance={}'.format(instance))
    App.objects.create(create_by=instance)


post_save.connect(receiver=create_app_v1, sender=User)


"""
关联sender和receiver还可以通过@receiver装饰器来完成

两个参数, signal可以是元组或者列表, 或者单个信号, **kwargs是位置参数
def receiver(signal, **kwargs)
"""
@receiver(post_save, sender=User)
def create_app_v2(sender, instance, **kwargs):
    logger.info('create_app_v2 收到 post_save 信号')
    App.objects.create(create_by=instance)
