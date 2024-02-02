from django.shortcuts import render, redirect
from .models import Product, Customer, Category, Cart, Customer_Order, Customer_feedback


def index(request):

    products1 = Product.objects.filter(category=1)
    products2 = Product.objects.filter(category=2)
    products3 = Product.objects.filter(category=3)
    products4 = Product.objects.filter(category=4)


    context = {
        'products1': products1,
        'products2': products2,
        'products3': products3,
        'products4': products4
    }
    return render(request, 'pages/index.html', context)

def allfeedback(request):
    feed = Customer_feedback.objects.all().order_by('-id')

    context = {
        'feed': feed
    }
    return render(request, 'pages/allfeedback.html', context)


def cart(request):

    user_id = request.session.get('id', None)
    if user_id is not None:
        cart = Cart.objects.filter(Customer_id=user_id, Status='oncart')
    else:
        cart = None

    context = {
        'cart': cart
    }
    return render(request, 'pages/cart.html', context)


def Order(request):

    user_id = request.session.get('id', None)
    if user_id is not None:
        cart = Customer_Order.objects.filter(Customer_id=user_id).exclude(Status='received')



    else:
        cart = None
    context = {
        'cart': cart
    }
    return render(request, 'pages/Ordered.html', context)

def allorder(request):

    order = Customer_Order.objects.exclude(Status="received")
    context = {
        'order': order
    }
    return render(request, 'pages/allorders.html', context)


def storefront(request):

    products1 = Product.objects.filter(category=1)
    products2 = Product.objects.filter(category=2)
    products3 = Product.objects.filter(category=3)
    products4 = Product.objects.filter(category=4)

    context = {
        'products1': products1,
        'products2': products2,
        'products3': products3,
        'products4': products4
    }
    return render(request, 'pages/storefront.html', context)



def register(request):


    return render(request, 'pages/register.html')

def login(request):


    return render(request, 'pages/login.html')

def front(request):


    return render(request, 'pages/front.html',)

def Addproduct(request):
    products = Product.objects.all()
    categories = Category.objects.all()


    context = {
        'products': products,
        'categories': categories

    }

    return render(request, 'pages/add.html', context)



def additem(request):
    # Retrieve data from the form submission
    name = request.POST.get('productName')
    price = request.POST.get('price')
    quantity = request.POST.get('quantity')
    category_name = request.POST.get('category')


    category = get_object_or_404(Category, name=category_name)


    if 'image' in request.FILES:
        pimage = request.FILES['image']
    else:
        pimage = None

    # Create the Product instance with the correct Category instance
    prod = Product.objects.create(name=name, price=price, quantity=quantity, image=pimage, category=category)
    prod.save()

    return redirect("/administrator")



def feedback(request):

    name = request.POST.get('name')
    email = request.POST.get('email')
    feedbacks = request.POST.get('feedback')


    if not name:
        name = "Anonymous"

    feed = Customer_feedback.objects.create(name=name, email=email, feedback=feedbacks)
    feed.save()

    return redirect("/storefront")



def addorder(request, id):

    customer_name = request.POST.get('customer_name')
    customer_address = request.POST.get('customer_address')
    customer_contact = request.POST.get('customer_contact')
    customer_id = request.POST.get('customer_id')


    price = float(request.POST.get('item_price'))
    quantity = int(request.POST.get('item_quantity'))
    item_name = request.POST.get('item_name')


    total_price = price * quantity

    cart = get_object_or_404(Cart, id=id)
    cart.Status ="Ordered"
    cart.save()

    order = Customer_Order.objects.create(
        name=item_name,
        Quantity=quantity,
        Price=total_price,
        CustomerName=customer_name,
        CustomerAddress=customer_address,
        CustomerContact=customer_contact,
        Customer_id=customer_id,
        Status="ongoing"


    )
    order.save()

    return redirect("/cart")

def addtocart(request):

    name = request.POST.get('productName')
    price = request.POST.get('price')
    quantity = request.POST.get('quantity')
    customerid = request.POST.get('customerid')

    prod = Cart.objects.create(name=name, Price=price, Quantity=quantity, Status="oncart", Customer_id=customerid)
    prod.save()

    return redirect("/storefront")




def delete(request,id):
    prod = Product.objects.get(id=id)
    prod.delete()

    return redirect("/administrator")

def received(request,id):

    cart = get_object_or_404(Customer_Order, id=id)
    cart.Status = "received"
    cart.save()
    return redirect("/Order")

def delivery(request,id):

    cart = get_object_or_404(Customer_Order, id=id)
    cart.Status = "On Delivery"
    cart.save()
    return redirect("/allorder")

def cartdelete(request,id):
    prod = Cart.objects.get(id=id)
    prod.delete()

    return redirect("/cart")



def update(request, id):
    products = Product.objects.get(id=id)
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories

    }
    return render(request, 'pages/update.html', context)






from django.shortcuts import get_object_or_404




def updaterecord(request, id):
    name = request.POST.get('productName')
    price = request.POST.get('price')
    quantity = request.POST.get('quantity')
    category_name = request.POST.get('category')


    category = get_object_or_404(Category, name=category_name)


    if 'image' in request.FILES:
        pimage = request.FILES['image']
    else:
        pimage = None


    prod = get_object_or_404(Product, id=id)


    prod.name = name
    prod.price = price
    prod.quantity = quantity
    prod.image = pimage
    prod.category = category
    prod.save()

    return redirect("/administrator")










def UserRegister(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        uname = request.POST.get('username', '')
        contact = request.POST.get('contactNumber', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        address = request.POST.get('address', '')

        # Validate that the user already exists
        user = Customer.objects.filter(email=email)
        if user:
            message = "User already exists"
            return render(request, "pages/register.html", {'msg': message})
        else:
            insertuser = Customer.objects.create(name=name, username=uname, email=email, contact=contact, address=address, password=password, role='customer')
            insertuser.save()
            message = "User registered successfully"
            return render(request, "pages/login.html", {'msg': message})


    return render(request, "pages/register.html")




def LoginUser(request):
    if request.method == "POST":
        email = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Checking the email with the database
            user = Customer.objects.get(username=email)

            if user.password == password:
                request.session['id'] = user.id
                request.session['name'] = user.name
                request.session['username'] = user.username
                request.session['email'] = user.email
                request.session['address'] = user.address
                request.session['contact'] = user.contact

                if user.role == "customer":

                    return redirect("storefront")
                else:
                    return redirect("index")
            else:
                message = "Password does not match"
                return render(request, "pages/login.html", {'msg': message})

        except Customer.DoesNotExist:
            message = "User does not exist"
            return render(request, "pages/register.html", {'msg': message})

    return render(request, "pages/login.html")
