from django.http import HttpResponse
from rest_framework import permissions, generics, status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

import requests
from random import randint
from api.models import NewsModels
from api.serializers import NewsSerializers


# Create your views here.

class NewsView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'api/index.html'
    throttle_scope = 'news'
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        num = randint(1, 100)
        url1 = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=5a11aa5a769a49909d8cc2cefdfc77c5"
        url2 = "https://newsapi.org/v2/everything?q=tesla&from=2023-10-29&sortBy=publishedAt&apiKey" \
               "=5a11aa5a769a49909d8cc2cefdfc77c5"
        url3 = "https://newsapi.org/v2/everything?q=apple&from=2023-11-28&to=2023-11-28&sortBy=popularity&apiKey=5a11aa5a769a49909d8cc2cefdfc77c5"
        if num // 2 == 0:
            response = requests.get(url1)
            if response.status_code == 200:
                data = response.json()
                if 'articles' in data:
                    for item in data['articles']:
                        title_te = item.get('title')
                        if not NewsModels.objects.filter(title=title_te).exists():
                            titles = item.get('title')
                            url_link = item.get('url')
                            image_url = item.get('urlToImage')
                            content = item.get('content')
                            date_time = item.get('publishedAt')
                            news_data = NewsModels(
                                title=titles,
                                link=url_link,
                                photo=image_url,
                                content=content[:200],
                                date_time=date_time[:10]
                            )
                            news_data.save()
                            news_data = NewsModels.objects.all()
                            context = {'news': news_data}
                            return Response(context)
                    else:
                        pass
        elif num // 3 == 0:
            response = requests.get(url3)
            if response.status_code == 200:
                data = response.json()
                if 'articles' in data:
                    for item in data['articles']:
                        title_te = item.get('title')
                        if not NewsModels.objects.filter(title=title_te).exists():
                            titles = item.get('title')
                            url_link = item.get('url')
                            image_url = item.get('urlToImage')
                            content = item.get('content')
                            date_time = item.get('publishedAt')
                            news_data = NewsModels(
                                title=titles,
                                link=url_link,
                                photo=image_url,
                                content=content[:200],
                                date_time=date_time[:10]
                            )
                            news_data.save()
                            news_data = NewsModels.objects.all()
                            context = {'news': news_data}
                            return Response(context)
                    else:
                        pass
        else:
            response = requests.get(url2)
            if response.status_code == 200:
                data = response.json()
                if 'articles' in data:
                    for item in data['articles']:
                        title_te = item.get('title')
                        if not NewsModels.objects.filter(title=title_te).exists():
                            titles = item.get('title')
                            url_link = item.get('url')
                            image_url = item.get('urlToImage')
                            content = item.get('content')
                            date_time = item.get('publishedAt')
                            news_data = NewsModels(
                                title=titles,
                                link=url_link,
                                photo=image_url,
                                content=content[:200],
                                date_time=date_time[:10]
                            )
                            news_data.save()
                            news_data = NewsModels.objects.all()
                            context = {'news': news_data}
                            return Response(context)
                    else:
                        pass


def migration(request):
    import os
    os.system('python3 manage.py makemigrations')
    os.system('python3 manage.py migrate --no-input')
    return HttpResponse('Migration Done')