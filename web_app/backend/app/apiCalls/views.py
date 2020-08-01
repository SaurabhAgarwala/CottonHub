from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
import json

base_url = "https://cotton-forecast.herokuapp.com/"

def get_user_id(auth_token):

    headers = {
        "Authorization": "token "+auth_token
    }
    url = base_url + "auth/users/me/"
    resp = requests.get(url , headers = headers)
    response_json = resp.json()
    print(response_json)
    return response_json['id']

@csrf_exempt
def login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        if password == "":
            data = {
                "username": username
            }
            send_otp(data)
            request.session["username"] = username
            return redirect("/otplogin/")

        else:
        
            url = base_url + "auth/token/login/"
            request_obj = {
                "username": username,
                "password": password
            }
            resp = requests.post(url, data = request_obj)
            print(resp.json())
            response_json = resp.json()
            try:
                auth_token = response_json['auth_token']
                request.session['auth_token'] = auth_token
                request.session['user_id'] = get_user_id(auth_token)
                return redirect("/dashboard")
            except:
                print(response_json)
                data = {
                    "errors": response_json["non_field_errors"][0]
                }
                print(data)
                return render(request,"apiCalls/login.html",data)

    else:

        return render(request, "apiCalls/login.html")

def send_otp(request_obj):
    url = base_url + "otplogin/"
    headers = {
        "media-type": "application/json",
        "Content-Type": "application/json"
    }
    print(json.dumps(request_obj))

    resp = requests.post(url,data = json.dumps(request_obj),headers = headers)
    print(resp)
    print(resp.text)

@csrf_exempt
def otpLogin(request):

    if request.method == "POST":
        
        url = base_url + "verifyotp/"
        request_obj = {
            "username": request.POST.get("username"),
            "otp": request.POST.get("otp")
        }
        headers = {
            "media-type": "application/json",
            "Content-Type": "application/json"
        }
        resp = requests.post(url, data = json.dumps(request_obj), headers = headers)
        response_json = resp.json()
        print(response_json)
        request.session["auth_token"] = response_json['auth_token']
        del request.session["username"]

        return redirect("/dashboard")
    
    else:
        data = {
            "username": request.session["username"]
        }
        return render(request,"apiCalls/otplogin.html",data)

def logout(request):

    headers = {
        "Authorization": "token "+request.session['auth_token']
    }

    url = base_url + "/auth//token/logout/"
    requests.post(url,headers = headers)
    del request.session['auth_token']
    del request.session['user_id']
    return redirect("/login/")


@csrf_exempt
def signUp(request):

    if request.method == "POST":
        
        url = base_url + "auth/users/"
        username = request.POST.get("username")
        password = request.POST.get("password")
        request_obj = {
            "username": username,
            "password": password,
            "re_password": request.POST.get("re_password"),
            "pan": request.POST.get("pan"),
            "aadhar": request.POST.get("aadhar"),
            "first_name": request.POST.get("first_name"),
            "last_name": request.POST.get("last_name")

        }
        resp = requests.post(url, data = request_obj)
        response_json = resp.json()

        if resp.status_code == 400:
            errors = {}
            for key, value in response_json.items():
                errors[key] = value[0]
            print(errors)
            return render(request,"apiCalls/signup.html",{"errors":errors})

        else:

            request_obj_for_login = {
                "username": username,
                "password" : password
            }
            url = base_url + "auth/token/login/"
            resp = requests.post(url, data = request_obj_for_login)
            response_json = resp.json()
            try:
                auth_token = response_json['auth_token']
                request.session['auth_token'] = auth_token
                return redirect("/dashboard")
            except:
                return render(request,"apiCalls/invalid_page_before_login.html")

    else:

        return render(request, "apiCalls/signup.html")

