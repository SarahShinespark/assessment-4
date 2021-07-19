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
    form = PostForm(request.POST or None)

    if request.method == "POST":
        try:
            form.save()
            return redirect("categories:categories_all")
        except Exception as e:
            print(e)
            return HttpResponse("Error creating new post!")

    data = {"form": form, "category_id": category_id}
    return render(request, "pages/posts/post_new.html", data)

def post_detail(request, category_id, post_id):
    try:
        category = Category.objects.get(pk=category_id)
        post =    Post.objects.get(pk=post_id)
    except Exception as e:
        print(e)
        return HttpResponse("Failed to retrieve post.")
    
    data = {"category": category, "post": post}
    return render(request, "pages/posts/post_details.html", data)

def post_edit(request, category_id, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except:
        print("error")
        return HttpResponse("That post doesn't exist!")
    
    form = PostForm(request.POST or None, instance=post)

    if request.method == "POST":
        try:
            form.save()
            return redirect("categories:posts_detail", category_id=category_id, post_id=post_id)
        except Exception as e:
            print(e)
            return HttpResponse("Error updating post!")

    data = {"form": form, "category_id": category_id, "post_id": post_id}
    return render(request, "pages/posts/post_edit.html", data)

def post_delete(request, category_id, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('categories:categories_detail', category_id=category_id)

