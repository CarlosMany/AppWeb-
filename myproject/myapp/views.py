from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ItemForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item_detail.html', {'item': item})

def item_new(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm()
    return render(request, 'item_form.html', {'form': form})

def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm(instance=item)
    return render(request, 'item_form.html', {'form': form})

def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return redirect('item_list')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_dashboard')
            else:
                return redirect('user_dashboard')
        else:
            return HttpResponse("Invalid login")
    return render(request, 'login.html')

def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('login')
    items = Item.objects.all()
    return render(request, 'admin_dashboard.html', {'items': items})

def user_dashboard(request):
    if not request.user.is_authenticated or request.user.is_staff:
        return redirect('login')
    return render(request, 'user_dashboard.html', {'user': request.user})

def main_view(request):
    return render(request, 'main.html')