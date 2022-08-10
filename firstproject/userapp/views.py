from ast import Pass
from http.client import HTTPResponse
from pickle import TRUE
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import pymysql
import re
from .form import *
import datetime
# Create your views here.

usersuperlevel=[0]
userlevel=[0,1]

def authcheck(request):
    return request.session.get('level')

def accountcheck(request):
    return request.session.get('account')

def readCommonSession(request):
    return dict(request.session)


def setSession(request, key, value):
    request.session[key] = value
    return redirect('/')


def delSession(request, key):
    if key in request.session:
        del request.session[key]
        return HttpResponse("COOKIE刪除完成")
    else:
        return HttpResponse('KEY不存在')


def readSession(request, key):
    if key in request.session:
        data = request.session[key]
        return HttpResponse(str(data))
    else:
        return HttpResponse('KEY不存在')

# ***************************************************************


def delCookie(request, key):
    if key in request.COOKIES:
        response = HttpResponse("COOKIE刪除完成")
        response.delete_cookie(key)
        return response
    else:
        return HttpResponse('KEY不存在')


def readCookie(request, key):
    if key in request.COOKIES:
        return HttpResponse(request.COOKIES[key])
    else:
        return HttpResponse('KEY不存在')


def setCookie(request, key, value):
    response = HttpResponse("COOKIE儲存完成")
    response.set_cookie(key, value, max_age=300)
    return response


def setCookieRed(request, key, value):
    response = redirect("/")
    response.set_cookie(key, value, max_age=300)
    return response

# ***************************************************************


def userinput(request):
    form = userdata()
    return render(request, 'userinput.html', {'form': form,'session':readCommonSession(request)})


def index1(request):
    return render(request, 'index.html', {'session':readCommonSession(request)})


def index2(request):
    return HttpResponse("<h1>我是index</h1>")

# ***************************************************************


def login(request):
    if request.method == "GET":
        if 'name' in request.session:
            return HttpResponse("<h1>登入已完成</h1>")
        else:
            return render(request, 'userapp/login.html',{'session':readCommonSession(request)})
    else:
        account = request.POST.get('account')
        password = request.POST.get('password')
        db = pymysql.connect(host='127.0.0.1', user='QvQ',
                             passwd='19950713', database='mdu')
        cursor = db.cursor()
        sql = 'SELECT * from account where account="{}"'.format(account)
        cursor.execute(sql)
        db.commit()
        data = cursor.fetchone()
        db.close()
        if data[3] == password:
            request.session['id'] = data[0]
            request.session['name'] = data[1]
            request.session['account'] = data[2]
            request.session['level'] = data[4]
            request.session['time'] = str(datetime.datetime.now())[:19]
            # return HttpResponse("<h1>登入完成</h1>")
            return redirect('/')
        else:
            return HttpResponse("<h1>帳號密碼錯誤</h1>")

def logout(request):
    if 'name' in request.session:
        del request.session['id']
        del request.session['name']
        del request.session['account']
        del request.session['level']
        del request.session['time']
        return redirect('/')
    else:
        return HttpResponse("<h1>已登出</h1>")

# def logincheck(request):
#     userid=request.POST.get('account')
#     password=request.POST.get('password')
#     if userid == 'QvQ' and password == '1234':
#         return HttpResponse("<h1>登入完成</h1>")
#     else:
#         return HttpResponse("<h1>帳號密碼錯誤</h1>")


def strLengthCheck(string, strMin, strMax):
    string = string.strip()
    length = len(string)
    if length > strMax:
        return [3, "超過文字上限長度: 最多"+str(strMax)+'字']
    elif length < strMin:
        return [2, "低於文字最低長度: 最少"+str(strMin)+'字']
    else:
        return[1, "文字長度合格"]


def strRuleCheck(string):
    string = string.strip()
    # if not string:
    #     return [3, "文字不應為空白"]
    ptn = re.findall(r'(\w+)', string)
    if ptn:
        if ptn[0] == string:
            return [1, '文字合格']
        else:
            return [2, '文字不應含空白或特殊字元']
    else:
        return [3, "文字不應含空白或特殊字元"]

# ***************************************************************


def useradd(request):
    if request.method == "GET":
        
        return render(request, 'userapp/useradd.html',{'session':readCommonSession(request)})
    else:
        account = request.POST.get('account')
        password = request.POST.get('password')
        name = request.POST.get('name')
        retname = strLengthCheck(name, 3, 10)
        retacc = strLengthCheck(account, 3, 10)
        retpwd = strLengthCheck(password, 8, 16)
        ckname = strRuleCheck(name)
        ckacc = strRuleCheck(account)
        ckpwd = strRuleCheck(password)
        # errormsg=['姓名','帳號','密碼']
        errmsg = []
        data = [-1, name, account, password]
        Pass = TRUE
        if retacc[0] != 1:
            errmsg.append('帳號'+retacc[1])
            Pass = False
            # return render(request,'userapp/userupdate.html',{'data':data ,'btn':'重新建立','opt':3,
            # # 'error':retacc[1],'errormsg':errormsg[1]})

        if ckacc[0] != 1:
            Pass = False
            errmsg.append('帳號'+ckacc[1])

        # 密碼驗證太麻煩,先關掉

        # if retpwd[0] != 1:
        #     errmsg.append('密碼'+retpwd[1])
        #     Pass = False

        #     # return render(request,'userapp/userupdate.html',{'data':data ,'btn':'重新建立','opt':3,
        #     # 'error':retpwd[1],'errormsg':errormsg[2]})

        # if ckpwd[0] != 1:
        #     pwd = re.search(r'(\s)', password)
        #     # return HttpResponse(pwd)
        #     if pwd != None:
        #         Pass = False
        #         errmsg.append('密碼不應含有空白')
        # else:
        #     Pass = False
        #     errmsg.append('密碼應有特殊字元')

        # if not re.search(r"[A-Z]", password):
        #     Pass = False
        #     errmsg.append('密碼應有大寫英文')

        # if not re.search(r"[a-z]", password):
        #     Pass = False
        #     errmsg.append('密碼應有小寫英文')

        # if not re.search(r"\d", password):
        #     Pass = False
        #     errmsg.append('密碼應有數字')

        if retname[0] != 1:
            errmsg.append('姓名'+retname[1])
            Pass = False
            # return render(request,'userapp/userupdate.html',{'data':data ,'btn':'重新建立','opt':3,
            # 'error':retname[1],'errormsg':errormsg[0]})

        if ckname[0] != 1:
            Pass = False
            errmsg.append('姓名'+ckname[1])

        if not Pass:
            return render(request, 'userapp/userupdate.html', {'data': data, 'btn': '重新建立', 'opt': 3,
                                                               'error': errmsg})

        priority = 2  # 2 一般使用者帳號
        db = pymysql.connect(host='127.0.0.1', user='QvQ',
                             passwd='19950713', database='mdu')
        cursor = db.cursor()
        sql = 'SELECT * from account where account="{}"'.format(account)
        cursor.execute(sql)
        db.commit()
        data = cursor.fetchone()
        if data != None:
            return HttpResponse("<h1>帳號已存在  <a href='/useradd/'>回上頁</a></h1>")
        else:
            sql = "insert into account (name,account,password,priority) values ('{}','{}','{}','{}')"\
                .format(name, account, password, priority)
            cursor.execute(sql)
            db.commit()
            db.close()
            return HttpResponse("<h1>帳號創建成功  <a href=/>回首頁</a></h1>")


def userlist(request):
    if authcheck(request) == None:
        return HttpResponse('請先登入')
    if authcheck(request) not in userlevel:
        return HttpResponse('權限不足')
    db = pymysql.connect(host='127.0.0.1', user='QvQ',
                         passwd='19950713', database='mdu')
    cursor = db.cursor()
    if authcheck(request) in usersuperlevel:
        sql = 'SELECT * from account'
    else:
        sql = 'SELECT * from account where id={}'.format(request.session.get('id'))
    cursor.execute(sql)
    db.commit()
    data = cursor.fetchall()
    db.close()
    return render(request, 'userapp/userlist.html', {'data': data,'session':readCommonSession(request)})


def userdelete(request, uid=0):
    if authcheck(request) not in userlevel:
        return HttpResponse('請先登入')
    if authcheck(request) not in usersuperlevel:
        return HttpResponse('權限不足')
    if request.method == 'POST':
        uid = request.POST.get('id')
    db = pymysql.connect(host='127.0.0.1', user='QvQ',
                         passwd='19950713', database='mdu')
    cursor = db.cursor()
    sql = 'delete from account where id={}'.format(uid)
    cursor.execute(sql)
    db.commit()
    db.close()
    return redirect("/userlist/")

# ***************************************************************


def userupdate(request, uid=-1):
    if authcheck(request) == None:
        return HttpResponse('請先登入')   

    if authcheck(request) not in usersuperlevel:
        return HttpResponse('權限不足')

    if request.method == "GET":
        db = pymysql.connect(host='127.0.0.1', user='QvQ',
                             passwd='19950713', database='mdu')
        cursor = db.cursor()
        sql = 'SELECT * from account where id = {}'.format(uid)
        cursor.execute(sql)
        db.commit()
        db.close()
        data = cursor.fetchone()
        if data == None:
            return HttpResponse("<h1>查無帳號</h1>")
        else:
            return render(request, 'userapp/userupdate.html', 
            {'data': data, 'btn': '修改', 'opt': 2 ,'session':readCommonSession(request)})
        
    else:
        uid = request.POST.get('id')
        name = request.POST.get('name')
        password = request.POST.get('password')
        priority = request.POST.get('priority')
        db = pymysql.connect(host='127.0.0.1', user='QvQ',
                             passwd='19950713', database='mdu')
        cursor = db.cursor()
        # if priority == None:
        #     sql = "update account set password='{}',name='{}' where id = {}".format(
        #         password, name, uid)
        # else:
        sql = "update account set password='{}',name='{}',priority={} where id = {}".format(
                password, name, priority, uid)
        cursor.execute(sql)
        db.commit()
        db.close()
        return redirect('/userlist/')


def userupdatecheck(request):
    uid = request.POST.get('id')
    name = request.POST.get('name')
    password = request.POST.get('password')
    data = [uid, name, 0, password]
    return render(request, 'userapp/userupdate.html', {'data': data, 'btn': '確認修改', 'opt': 9999 ,'session':readCommonSession(request)})
    # 後臺確認修改的方式 目前沒用 要把 userupdate() 的 opt 改 1 userupdatecheck opt 改 2 才可以啟用
