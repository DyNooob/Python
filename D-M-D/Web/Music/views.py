# 专门在浏览器中返回要显示的数据包
from django.http import request
from django.shortcuts import render

from .models import Music
from django.views.generic import View

# Create your views here.

# 实现搜索功能
from django.db.models import Q


# 使用函数将内容显示到浏览器
def index(request):
    # if request.method == 'POST':
    #     pass
    return render(request, 'index.html', locals())


# 使用类将内容显示到浏览器
class Search(View):
    def get(self, request):
        # 首先在页面中获取用户输入的数据
        search_text = request.GET['search_text']
        print(search_text)

        if not search_text:
            return render(request, 'index.html', locals())

        # 搜索
        response_list = Music.objects.filter(Q(name__icontains=search_text) | Q(singer__icontains=search_text))

        # 记录搜索数据
        with open('record.txt' , 'a', encoding='utf-8') as f:
            if not response_list:
                f.write('\n', + search_text + '\t0')
            else:
                f.write('\n', + search_text + '\t0')
            return render(request, 'result.html', locals())

    def post(self, request):
        pass
