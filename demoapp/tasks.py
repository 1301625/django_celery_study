from __future__ import absolute_import
from .celery import app

# @shared_task
# def add(x,y):
#     return x + y
#
# @shared_task
# def mul(x,y):
#     return x * y
#
# @shared_task
# def xsum(numbers):
#     return sum(numbers)




@app.task
def world(num):
    for x in range(num):
        print("**************진짜 퇴근좀 하자***************")
    return num


@app.task
def callable_task():
    for x in range(5):
        print("------------------spawn by user-------------------")