from django.core import paginator
from django.shortcuts import render
from .models import Order, Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    product_objects = Product.objects.all()

    # Search code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)

    # Paginator code
    paginator = Paginator(product_objects, 8)
    page = request.GET.get("page")
    product_objects = paginator.get_page(page)
    return render(request, 'shop/index.html', {'product_objects': product_objects})

def detail(request,id):
    product_object = Product.objects.get(id=id)
    return render(request, 'shop/detail.html', {'product_object': product_object})

def checkout(request):
    if request.method == "POST":
        items = request.POST.get("items", "")
        name = request.POST.get("inputname4", "")
        email = request.POST.get("inputEmail4", "")
        address = request.POST.get("inputAddress", "")
        city = request.POST.get("inputCity", "")
        state = request.POST.get("inputState", "")
        zip = request.POST.get("inputZip", "")
        total = request.POST.get("total", "")
        order = Order(items=items,name=name, email=email,address=address,city=city,state=state,zip=zip, total=total)
        order.save()
    return render(request, 'shop/checkout.html')