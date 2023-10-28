from django.shortcuts import render, redirect
from .models import MenuItem
from .forms import MenuItemForm

def menu_list(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu/menu_list.html', {'menu_items': menu_items})

def add_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuItemForm()
    return render(request, 'menu/menu_form.html', {'form': form})

def edit_menu_item(request, pk):
    menu_item = MenuItem.objects.get(pk=pk)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, instance=menu_item)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuItemForm(instance=menu_item)
    return render(request, 'menu/menu_form.html', {'form': form})

def remove_menu_item(request, pk):
    menu_item = MenuItem.objects.get(pk=pk)
    menu_item.delete()
    return redirect('menu_list')

