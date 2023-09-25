from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404, redirect
from .forms import NewItemForm, EditItemForm

from item.models import Item, Category


def detail(request, pk):
    item = get_object_or_404(Item,pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold = False).exclude(pk=pk)[0:3]
    return render(request, 'item/detail.html',{
        'item':item,
        'related_items':related_items
        })


@login_required
def new(request):

    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            #commit=false porque al guardar el item en la bd, no hay el campo created_By
            #y tendría error
            item=form.save(commit=False)
            item.created_by= request.user
            item.save()
            return redirect('item:detail',pk=item.id)
    
    else:
        form=NewItemForm()

    return render(request, 'item/form.html', {'form':form, 'title':'New Item'})


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by = request.user)
    item.delete()

    return redirect('dashboard:index')



@login_required
def edit(request,pk):
    item = get_object_or_404(Item, pk=pk, created_by = request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            item.save()

            return redirect('item:detail',pk=item.id)
    
    else:
        form=EditItemForm(instance=item)

    is_edit_form = isinstance(form, EditItemForm)

    return render(request, 'item/form.html', {'form':form, 'title':'Edit Item', 'is_edit_form':'is_edit_form'})