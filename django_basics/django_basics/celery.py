import os
import django
from celery import Celery
from django.conf import settings

# 设置系统环境变量，安装django，必须设置，否则在启动celery时会报错
# celery_study 是当前项目名
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_basics.settings')
django.setup()
#实例化一个celery类
celery_application = Celery('django_basics')
#指定配置文件的位置
celery_application.config_from_object('django.conf:settings')
#自动从settings的配置INSTALLED_APPS中的应用目录下加载 tasks.py
celery_application.autodiscover_tasks(lambda: settings.INSTALLED_APPS)