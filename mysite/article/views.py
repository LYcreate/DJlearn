from django.shortcuts import render
from article.models import Article
# Create your views here.
def latest_article(requestd):
    article_list=Article.objects.order_by('-id')
    return render(request,'articles.html',{'article_list':article_list})
