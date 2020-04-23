# signals_demo
![actions_img]

signals 使用实例

## 注意事项
- 需要在对应app的__init__.py里添加以下语句
```python
# app1/__init__.py
default_app_config = 'app1.apps.App1Config'
```
- 如果不想在__init__.py里添加上面的语句, 那么在settings里引入app的方式必须为以下形式
```python
INSTALLED_APPS = [
    # 省略其余app
    'app1.apps.App1Config',
]
```
- 需要在对应app的apps.py里添加以下语句
```python
# app1/apps.py
from django.apps import AppConfig


class App1Config(AppConfig):
    name = 'app1'

    def ready(self):
        import app1.signals  # noqa
```

[actions_img]:https://github.com/2375452377/signals_demo/workflows/Django%20CI/badge.svg
