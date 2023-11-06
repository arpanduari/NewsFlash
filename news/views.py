from django.shortcuts import render, redirect
import os
import requests
import random


API_KEY = os.environ.get("NEWS_API")
BASE_URL = f"https://newsapi.org/v2/top-headlines?apikey={API_KEY}&country=in"
BASE_URL_E = f"https://newsapi.org/v2/everything?apikey={API_KEY}"


# Create your views here.
def index(request):
    top_news = requests.get(f"{BASE_URL}").json()
    newses = top_news['articles']
    random.shuffle(newses)
    return render(request, "news/index.html", context={"newses": newses})


def category_news(request, category):
    print(category)
    top_news = requests.get(f"{BASE_URL}&category={category}").json()
    newses = top_news['articles']
    random.shuffle(newses)
    return render(
        request,
        "news/category_news.html",
        context={"newses": newses, "category": category},
    )


def search_result(request):
    if request.method == "POST":
        search_query = request.POST.get("search_query")
        if search_query is not None and search_query != "":
            all_news = requests.get(f"{BASE_URL_E}&q={search_query}").json()
            return render(
                request,
                "news/query.html",
                context={"newses": all_news["articles"], "q": search_query},
            )
        else:
            return redirect("home")
def about(request):
    return render(request, "news/about.html")
