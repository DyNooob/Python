import jsonpickle as jsonpickle
from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from index.models import Chat
from django.contrib.auth.models import User

# Create your views here.
# user = {'uname': 'admin', 'pwd': 'dy12345.'}
error = {}


def index(request):
    try:
        user_n = jsonpickle.loads(request.session.get('user'))
        user_id = jsonpickle.loads(request.session.get('user_id'))
        user_data = {}
        user_data['my_name'] = user_n
        user_data['my_id'] = user_id
        chat_data = Chat.objects.all()
        chat_data_test = reversed(chat_data) # 倒叙列表 让最新的消息在前面
        return render(request, 'index.html', {'user': user_data, 'chat_data': chat_data_test})
    except:
        return render(request, 'login.html')


def login(request):
    try:
        user_n = jsonpickle.loads(request.session.get('user'))
        user_id = jsonpickle.loads(request.session.get('user_id'))
        if user_n and user_id:
            return HttpResponseRedirect('../index/')
        else:
            return render(request, 'login.html')
    except:
        return render(request, 'login.html')

def logout(request):
    del request.session['user']
    del request.session['user_id']
    return render(request, 'logout_ok.html')


def login_check(request):
    if request.POST:
        in_uname = request.POST['uname']
        in_password = request.POST['passwd']
        if in_uname and in_password:
            user = authenticate(username=in_uname, password=in_password)
            if user:
                user_data = User.objects.get(username=in_uname)
                request.session['user'] = jsonpickle.dumps(in_uname)
                request.session['user_id'] = jsonpickle.dumps(user_data.id)
                return render(request, 'ok.html')
            else:
                error['error_data'] = '用户名或密码错误'
                return render(request, 'fail.html', error)
        else:
            error['error_data'] = '请确保用户名和密码不为空！'
            return render(request, 'fail.html', error)
    else:
        return HttpResponse('Only need POST!')


def chat_data_write(request):
    if request.POST:
        user_name = jsonpickle.loads(request.session.get('user'))
        user_id = jsonpickle.loads(request.session.get('user_id'))
        chat_data_write_in = request.POST['chat']
        Chat.objects.create(user_id=user_id, user_name=user_name, chat_data=chat_data_write_in)
        return HttpResponseRedirect('../index/')
    else:
        return HttpResponse('Not use GET, please return /index/ and use POST to do it.', 403)