from rest_framework import permissions, generics, status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

import requests

from api.models import NewsModels
from api.serializers import NewsSerializers


# Create your views here.

class NewsView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'api/index.html'
    throttle_scope = 'news'
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        url = "https://newsapi.org/v2/everything?q=apple&from=2023-11-27&to=2023-11-27&sortBy=popularity&apiKey" \
              "=5a11aa5a769a49909d8cc2cefdfc77c5"
        response = requests.get(url)
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
                        NewsModels.objects.create(title=titles, link=url_link, photo=image_url, content=content,
                                                  date_time=date_time)
                        serialized_data = NewsSerializers(NewsModels.objects.all(), many=True).data
                        context = {'news': serialized_data}
                        return Response(context)
                    else:
                        pass
