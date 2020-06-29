from django.shortcuts import render
from .models import Item
from .forms import ItemForm
from django.shortcuts import redirect


def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'index.html', context)


def box(request):
    return render(request, 'cart.html')

def manage_items(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'management.html', context)


def item_new(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = ItemForm()
    return render(request, 'management.html', {'form': form})
