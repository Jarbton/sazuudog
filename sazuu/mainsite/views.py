from django.shortcuts import render
from django.views import View

class HomeView(View):
    template_name = 'mainsite/home.html'

    def get(self, request):
        context = {'title': 'SazuuDog - Home'}
        return render(request, self.template_name, context)


class StreamingView(View):
    template_name = 'mainsite/streaming.html'

    def get(self, request):
        context = {'title': 'SazuuDog - Streaming'}
        return render(request, self.template_name, context)


class GamingView(View):
    template_name = 'mainsite/gaming.html'

    def get(self, request):
        context = {'title': 'SazuuDog - Gaming'}
        return render(request, self.template_name, context)