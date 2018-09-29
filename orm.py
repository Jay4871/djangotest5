import datetime
import os

# print(models.Person.objects.all())
# B/S 架构  浏览器 服务器  如果在python脚本或者文件中，加载Django项目的配置和变量信息
# if __name__ == "__main__":
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangotest5.settings")
#
#     import  django
#     django.setup()
#
#
#     from app01 import models
#
#
#     #如何实现数据的批量添加
#     # models.Book(title='helloworld')
#
#     objects=[models.Book(title="helloworld{}".format(i)) for i  in range(1009)]
#
#     models.Book.objects.bulk_create(objects,10)


import json

s = '{"name":"zhangsan","age":18}'

list = []

# <editor-fold desc="Description">
result = json.loads(s)


def method_name():
    print(result, type(result))
    result2 = json.dumps(result)
    # </editor-fold>
    print(result2, type(result2))


method_name()

datetime = datetime()

if __name__ == '__main__':
     pass


        

