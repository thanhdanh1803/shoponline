from django.shortcuts import render
from mystore.models import Product, UserProfileInfo
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from cart.forms import *
from mystore.forms import *
# Create your views here.
def index(request):
    pro_list = Product.objects.order_by('name')
    pro_dict = {"products":pro_list }
    return render(request, "mystore/index.html", context=pro_dict)

def product_detail(request, id = None):
    product = Product.objects.get(pk=id)
    cart_product_form = CardAddProductForm()
    return render(request, 'mystore/product_detail.html', context= {'product': product, 'cart_product_form':cart_product_form })

def register(request):
    registered = False
    if request.method == "POST":
        form_user = UserForm(data = request.POST)
        form_por = UserProfileInfoForm(data = request.POST)
        if form_user.is_valid() and form_por.is_valid():
            user = form_user.save()
            user.set_password(user.password)
            user.save()
            profile = form_por.save(commit = False)
            profile.user = user
            print(request.FILES)
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(form_user.errors, form_por.errors)
    else:
        form_user = UserForm()
        form_por = UserProfileInfoForm()
    return render(request, "mystore/registration.html", {'user_form':form_user,\
        'profile_form': form_por, 'registered': registered})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password = password)
        if user:
            if user.is_active:
                login(request, user)
                result = "Chào bạn " + username
                return render(request, "mystore/index.html", {"result":result})
        else:
            print("Không đăng nhập được")
            print("Username: {} and password: {}".format(username, password))
            login_result = "Username và password không hợp lệ"
            return render(request, "mystore/login.html",{"login_result": login_result})
    else:
        return render(request, "mystore/login.html")

@login_required
def user_logout(request):
    logout(request)
    result = "Bạn đã đăng xuất. Vui lòng chọn 'Đăng nhập'"
    return render(request, "mystore/index.html", {"result":result})