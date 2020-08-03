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

def redirectToLoginOrDashboard(request):


    try:
        auth_token = request.session["auth_token"]
        return redirect("/dashboard/")
    
    except:

        return redirect("/login/")

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
        try:
            request.session["auth_token"] = response_json['auth_token']
            del request.session["username"]
            request.session["user_id"] = get_user_id(response_json["auth_token"])
        

            return redirect("/dashboard/")
        except:
            data = {
                "errors": response_json["message"]
            }
            print(data)
            return render(request,"apiCalls/login.html",data)
    
    else:
        data = {
            "username": request.session["username"]
        }
        print(data)
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

def dashboard(request):

    try:
        auth_token = request.session['auth_token']
        return render(request,"apiCalls/dashboard.html")

    except:
        return redirect("/login/")

def getFaq(request):

    url = base_url + "faq"
    headers = {
        "Content-Type": "application/json"
    }
    resp = requests.get(url, headers = headers)
    response_json = resp.json()
    return JsonResponse(response_json, safe = False)


def faq(request):
    return render(request,"apiCalls/faq.html")

def privacypolicy(request):
    return render(request,"apiCalls/privacypolicy.html")

@csrf_exempt
def feedback(request):
    if request.method == "POST":
        try:
            auth_token = request.session['auth_token']
            headers = {
                "Authorization": "token "+auth_token,
                "Content-Type": "application/json"
            }
            print(request.POST)

            request_payload = {
                "body": request.POST.get("body"),
                "subject": request.POST.get("subject")
            }
            print(request_payload)
            url = base_url + "feedback/"
            resp = requests.post(url, data = json.dumps(request_payload), headers = headers)

            print(resp.status_code)
            print(resp.json)

            response_obj = {

            }

            return render(request,"apiCalls/feedback.html", response_obj)

        except:
            return redirect("/login/")
    else:
        try:
            auth_token = request.session['auth_token']
            return render(request,"apiCalls/feedback.html")

        except:
            return redirect("/login/")


def profile(request):
    try:
        auth_token = request.session['auth_token']
        headers = {
            "Authorization": "token "+auth_token
        }
        url = base_url+"auth/users/me/"
        resp = requests.get(url,headers = headers)
        response_obj = resp.json()
        return render(request,"apiCalls/profile.html",response_obj)

    except:
        return redirect("/login")

@csrf_exempt
def updateProfile(request):
    try:
        auth_token = request.session['auth_token']
        headers = {
            "Authorization": "token "+auth_token,
            "Content-Type": "application/json"
        }
        url = base_url+"auth/users/me/"
        request_data = json.dumps(request.POST)
        resp = requests.put(url,data = request_data, headers = headers)
        response_obj = resp.json()
        return redirect("/profile/")
    except:
        return redirect("/login")

@csrf_exempt
def cart(request):

    try:
        auth_token = request.session["auth_token"]
        return render(request,"apiCalls/cart.html")

    except:
        return redirect("/login/")


@csrf_exempt
def getCottonDetails(request):

    headers = {
        "Content-Type": "application/json"
    }

    url = base_url + "cottontype/"
    resp = requests.get(url, headers = headers)
    response_obj = resp.json()

    return JsonResponse(response_obj, safe = False)

@csrf_exempt
def getMarket(request):

    headers = {
        "Content-Type": "application/json"
    }

    url = base_url + "market/"
    resp = requests.get(url, headers = headers)
    response_obj = resp.json()

    return JsonResponse(response_obj, safe = False)

@csrf_exempt
def Inventory(request):

    try:
        auth_token = request.session["auth_token"]
        headers = {
            "Authorization": "token "+auth_token,
            "Content-Type": "application/json"
        }
        
        url = base_url + "inventory/"
        resp = requests.get(url, headers = headers)
        response_obj = resp.json()
        print(response_obj)
        return JsonResponse(response_obj, safe = False)
    except:
        return redirect("/login/")

@csrf_exempt
def getInventoryDetails(request):

    try: 
        auth_token = request.session["auth_token"]

        return render(request,"apiCalls/inventory.html")

    except:
        return redirect("/login/")


@csrf_exempt
def getInventoryOfUser(request):

    try:
        auth_token = request.session["auth_token"]
        headers = {
            "Authorization": "token "+auth_token,
            "Content-Type": "application/json"
        }

        print(auth_token)
        
        url = base_url + "inventory/me/"
        resp = requests.get(url, headers = headers)
        response_obj = resp.json()
        return JsonResponse(response_obj, safe = False)
    except:
        return redirect("/login/")

@csrf_exempt
def deleteInventory(request,id):
    try:
        auth_token = request.session["auth_token"]
        print(auth_token)
        print(id)

        headers = {
            "Authorization": "token "+auth_token
        }

        url = base_url + "inventory/"+str(id) + "/"

        print(url)

        resp = requests.delete(url, headers = headers)
        print(resp.text)
        print(resp.status_code)

        return redirect("/userinventory/")
    
    except:
        return redirect("/login/")

@csrf_exempt
def getOrders(request):

    try:
        auth_token = request.session["auth_token"]
        print(auth_token)
        headers = {
            "Authorization": "token "+auth_token,
            "Content-Type": "application/json"
        }

        url = base_url + "orderitem/me/"
        print("here after url")

        resp = requests.get(url, headers = headers)
        print(resp.status_code)
        response_obj = resp.json()
        print(response_obj)
        return JsonResponse(response_obj, safe = False)

    except:
        return redirect("/login/")

def orderHistory(request):

    try:
        auth_token = request.session["auth_token"]
        return render(request, "apiCalls/orderhistory.html")
    except:
        return redirect("/login/")

def deleteOrder(request,id):

    try:
        auth_token = request.session["auth_token"]
        print(auth_token)
        print(id)

        headers = {
            "Authorization": "token "+auth_token,
        }

        url = base_url + "orderitem/"+str(id) + "/"

        print(url)

        resp = requests.delete(url, headers = headers)
        print(resp.text)
        print(resp.status_code)

        return redirect("/cart/")
    
    except:
        return redirect("/login/")

def placeOrder(request,id):

    try:
        auth_token = request.session["auth_token"]
        print(auth_token)
        print(id)

        headers = {
            "Authorization": "token "+auth_token
        }

        url = base_url + "placeorder/"+str(id) + "/"

        print(url)

        resp = requests.put(url, headers = headers)
        print(resp.status_code)
        response_json = resp.json()
        print(response_json)

        return redirect("/cart/")
    
    except:
        return redirect("/login/")


@csrf_exempt
def buyProduct(request):

    if request.method == "POST":

        try:
            print(request.POST)
            auth_token = request.session["auth_token"]
            headers = {
                "Authorization": "token "+auth_token,
                "Content-Type": "application/json"
            }

            request_payload = {
                "user_uid": request.session["user_id"],
                "cotton_type": request.POST.get("cottontype"),
                "inventory_id": request.POST.get("inventoryId"),
                "quantity": request.POST.get("quantity"),
                "name": request.POST.get("name"),
                "mobile": request.POST.get("mobile"),
                "shipping_address" : request.POST.get("address")
            }

            print(request_payload)

            url = base_url+"addtocart/"
            resp = requests.post(url,data = json.dumps(request_payload), headers = headers)

            print(resp.status_code)
            response_json = resp.json()

            print(response_json)

            return render(request,"apiCalls/buyProduct.html")

        except:
            return redirect("/dashboard/")

    else:
        print("entered in buy")
        try:
            print("entered inside try")
            auth_token = request.session["auth_token"]
            # headers = {
            #     "Authorization": "token "+auth_token,
            #     "Content-Type": "application/json"
            # }
            # url = base_url+"cottontype"
            # resp = requests.get(url, headers = headers)

            # print(resp.status_code)
            # cotton_types = resp.json()
            # print(cotton_types)
            # print(cotton_types)

            # data = {
            #     "cotton_types": cotton_types
            # }

            
            return render(request,"apiCalls/buyProduct.html")
        
        except:
            return redirect("/login/")


@csrf_exempt
def sellProduct(request):

    if request.method == "POST":

        print(request.POST)

        try:
            auth_token = request.session["auth_token"]
            user_id = request.session["user_id"]
            print(user_id)
            headers = {
                "Authorization": "token "+auth_token,
                "Content-Type": "application/json"
            }

            request_payload = {
                "user_uid": str(user_id),
                "cotton_type": request.POST.get("cottontypes"),
                "quantity": request.POST.get("quantity"),
                "selling_price": request.POST.get("price")
            }

            print(request_payload)

            url = base_url+"sell/"
            print(url)
            print(json.dumps(request_payload))
            resp = requests.post(url, data = json.dumps(request_payload) , headers = headers)

            print(resp.status_code)

            response_json = resp.json()

            print(response_json)


            return redirect("/dashboard/")

        except:
            return redirect("/login/")

    else:
        return render(request,"apiCalls/sellProduct.html")

@csrf_exempt
def analysis(request):

    try:
        auth_token = request.session["auth_token"]
        
        return render(request, "apiCalls/analysis.html")

    except:
        return redirect("/login/")

def getAllTypeCottonAnalysis(request):

    try:
        auth_token = request.session["auth_token"]
        headers = {
            "Authorization": "token "+auth_token,
            "Content-Type": "application/json"
        }
        url = base_url + "analysis/"
        resp = requests.get(url, headers = headers)
        print(resp.status_code)
        response_json = resp.json()
        print(response_json)
        return JsonResponse(response_json, safe = False)
    except:

        return redirect("/login")

@csrf_exempt
def getAnalysis(request):
    if(request.method == "POST"):
        try:
            print(request.body)
            print("in views")
            content = json.loads(request.body)
            print(content)
            auth_token = request.session["auth_token"]
            print(auth_token)
            headers = {
                "Authorization": "token "+auth_token,
                "Content-Type": "application/json"
            }
            print(headers)
            print(content["market"])
            keys = content.keys()
            params = {}
            for i in keys:
                if content[i] != "":
                    params[i] = content[i]
            print(params)
            url = base_url + "analysis/specific/"

            resp = requests.get(url , headers = headers, params = params)
            print(resp.url)

            response_json = resp.json()

            print(response_json)

            return JsonResponse(response_json, safe = False)

        except:
            data = {
                "error": "You must be logged in access this functionality"
            }
            return JsonResponse(data)
    else:
        data = {
            "message": "Request method not allowed"
        }
        return JsonResponse(data)