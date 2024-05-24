from django.shortcuts import render

# Create your views here.
def product(request):
    if request.method=="POST":
        a=int(request.POST['a'])
        b=int(request.POST['b'])
        cal=b*a
        return render(request,"product.html",{'amt':cal})
    else:
        return render(request,"product.html")