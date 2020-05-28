from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def loginPage(request):
    context = {}
    return render(request, 'inv/login.html', context)


def redirect_view(request):
    response = redirect('/admin/')
    return response


@login_required(login_url='login')
def index(request):
    items = Laptops.objects.all()
    context = {
        'items': items
    }
    return render(request, 'inv/index.html', context)


@login_required(login_url='login')
def display_laptops(request):
    items = Laptops.objects.all()
    context = {
        'items': items
    }
    return render(request, 'inv/index.html', context)


@login_required(login_url='login')
def display_desktops(request):
    items = Desktops.objects.all()
    context = {
        'items': items
    }
    return render(request, 'inv/index.html', context)


@login_required(login_url='login')
def display_mobiles(request):
    items = Mobiles.objects.all()
    context = {
        'items': items
    }
    return render(request, 'inv/index.html', context)


@login_required(login_url='login')
def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls()
        return render(request, 'inv/add_new.html', {'form': form})


@login_required(login_url='login')
def add_laptop(request):
    return add_item(request, LaptopForm)


@login_required(login_url='login')
def add_desktop(request):
    return add_item(request, DesktopForm)


@login_required(login_url='login')
def add_mobile(request):
    return add_item(request, MobileForm)


@login_required(login_url='login')
def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=item)

        return render(request, 'inv/edit_item.html', {'form': form})


@login_required(login_url='login')
def edit_laptop(request, pk):
    return edit_item(request, pk, Laptops, LaptopForm)


@login_required(login_url='login')
def edit_desktop(request, pk):
    return edit_item(request, pk, Desktops, DesktopForm)


@login_required(login_url='login')
def edit_mobile(request, pk):
    return edit_item(request, pk, Mobiles, MobileForm)


@login_required(login_url='login')
def delete_laptop(request, pk):

    template = 'inv/index.html'
    Laptops.objects.filter(id=pk).delete()

    items = Laptops.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


@login_required(login_url='login')
def delete_desktop(request, pk):

    template = 'inv/index.html'
    Desktops.objects.filter(id=pk).delete()

    items = Desktops.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


@login_required(login_url='login')
def delete_mobile(request, pk):

    template = 'inv/index.html'
    Mobiles.objects.filter(id=pk).delete()

    items = Mobiles.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)
