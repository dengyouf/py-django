from django.shortcuts import render
from django.http import HttpResponse

import logging
logger = logging.getLogger(__name__)
# Create your views here.
def test(request):

    logger.debug("日志测试 debug 级别")
    logger.info("日志测试 info 级别")
    logger.warning("日志测试 warning 级别")
    logger.error("日志测试 error 级别")
    logger.critical("日志测试 critical 级别")
    return HttpResponse("日志学习")