from django.shortcuts import render, redirect
from django.http import HttpResponse
from categories.models import Category, Post
from categories.forms import CategoryForm, PostForm

#Controllers for the "categories" pages

def index(request):
    data = { "categories": Category.objects.all() }
    return render(request, "pages/categories/cat_index.html", data)
    
def cat_new(request):
    form = CategoryForm(request.POST or None)

    if request.method == "POST":
        try:
            form.save()
            return redirect("categories:categories_all")
        except Exception as e:
            print(e)
            return HttpResponse("Error creating new category!")

    data = {"form": form}
    return render(request, "pages/categories/cat_new.html", data)

def cat_detail(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
        posts =    category.posts.all()
    except Exception as e:
        print(e)
        return HttpResponse("That category doesn't exist!")
    
    data = {"category": category, "posts": posts}
    return render(request, "pages/categories/cat_details.html", data)
    
def cat_edit(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
    except:
        print("error")
        return HttpResponse("That category doesn't exist!")
    
    form = CategoryForm(request.POST or None, instance=category)

    if request.method == "POST":
        try:
            form.save()
            return redirect("categories:categories_detail", category_id=category_id)
        except Exception as e:
            print(e)
            return HttpResponse("Error updating category!")

    data = {"form": form, "category": category}
    return render(request, "pages/categories/cat_edit.html", data)

def cat_delete(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect('categories:categories_all')

def post_new(request, category_id):
    return HttpResponse("Hello, world. You're at the new post page.")

def post_detail(request, category_id, post_id):
    return HttpResponse(f"Hello, world. You're at the post page for category {category_id}, post {post_id}.")

def post_edit(request, category_id, post_id):
    return HttpResponse("Hello, world. You're at the post edit page.")

def post_delete(request, category_id, post_id):
    return HttpResponse("Hello, world. You're at the post delete page.")

