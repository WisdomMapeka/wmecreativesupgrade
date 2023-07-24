from django.shortcuts import render
from . models import Articles, Categories, AnalyticsCode, Comments, Messages, Photos_collections
from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.http import HttpResponse, JsonResponse
import datetime

from .serializers  import Photos_collectionsSerializers 
from rest_framework import viewsets
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


# Create your views here.
def index(request):
    all_posts = Articles.objects.filter(article_status='publish').order_by("-id")
    categories = Categories.objects.filter(is_series=False)
    return render(request, 'blog/index.html', {"posts":all_posts,
                                               "categories":categories})

def article(request, slug):
    categories = Categories.objects.filter(is_series=False)
    post = Articles.objects.get(slug = slug, article_status='publish')

    if post.num_views == None:
        post.num_views =1
        post.save()
    else:
        post.num_views +=1
        post.save()

    return render(request, 'blog/article.html', {"post":post,
                                                 "categories":categories})


def article_list(request, category):
    categories = Categories.objects.filter(is_series=False)
    try:
        category_id = Categories.objects.filter(name = category).first().id
    except AttributeError:
        category_id = 0
    print(category_id)
    posts = Articles.objects.filter(category = category_id, article_status='publish').order_by("-id")
    print(posts)
    return render(request, 'blog/article-list.html', {"posts":posts, 
                                                      "category":category,
                                                      "categories":categories})

"""
THis view list all cateries with the the booled is_series set to True.
If a person click on each category they are taken to the usuall list of articles page based 
on category, with a series of article belonging to that category.

THe only difference is that, the category name is treated a a title of some series this time
"""
def series_articles_title_list(request):
    categories = Categories.objects.filter(is_series=False)
    categories_series = Categories.objects.filter(is_series=True)

    return render(request, 'blog/series-article-titles-list.html', { 
                                                      "categories_series":categories_series,
                                                      "categories":categories})



def save_comment(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        comment = request.POST.get('actual_comment', None)
        blog_id = request.POST.get('blog_id', None)
        print(blog_id)
        
        blog = Articles.objects.get(id=blog_id)
        save_comment = Comments.objects.create(name=name, comment=comment, blog=blog)
        save_comment.save()

        mydict = {"name":name, "comment":comment, "blog_id":blog_id, "date_created":save_comment.date_created}
    print(save_comment.date_created)
    return JsonResponse(mydict)

def like_dislike_comment(request, val, comment_id):
    total = ''
    if val == 'like':
        comment = Comments.objects.get(id=comment_id)
        comment.likes +=1
        comment.save()
        total = comment.likes
    elif val == 'dislike':
        comment = Comments.objects.get(id=comment_id)
        comment.dislikes +=1
        comment.save()
        total = comment.dislikes
        print(val)
        print(comment)
    else:
        pass
    
    comment_like_dislike_details = {"total_like_dislike":total, "val":val, "comment_id":comment_id }
    print(total, val)
    return JsonResponse(comment_like_dislike_details)


def sendmessage(request):
    if request.method == "POST":
        name = request.POST.get("name", None)
        email = request.POST.get("email", None)
        phone = request.POST.get("phone", None)
        message = request.POST.get("message", None)
        
        user_message = Messages.objects.create(name=name, email=email, phone=phone, message=message)
        user_message.save()

    return render(request, 'blog/sendmessage.html')


def contacts(request):
    return render(request, 'blog/contacts.html')




# -------------API-----------------------
@csrf_exempt
def images_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        images = Photos_collections.objects.all()
        serializer = Photos_collectionsSerializers(images, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)

    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = Photos_collectionsSerializers(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)



