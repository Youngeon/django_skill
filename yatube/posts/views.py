from django.shortcuts import render
from django.http import HttpResponse

def index(request):    
    return HttpResponse('''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="description" content="Краткое описание страницы">
    <title>Заголовок для отображения в названии вкладки</title>
    <link rel="icon" href="fav.ico" type="image">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="manifest" href="/site.webmanifest">
    <meta name="msapplication-TileColor" content="#da532c">
    <meta name="theme-color" content="#ffffff">
  </head>
  <body>
    <header>
        Верхняя часть страницы: логотип, контакты
      <nav>
        Меню (навигация)
      </nav>
    </header>
    <main>
      Основное содержимое страницы
    </main>
    <footer>
      Подвал
    </footer>
  </body>
</html>''')


# Страница со группами
def group_posts(request,slug):
    return HttpResponse(f'Группы {slug}')


# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
#def ice_cream_detail(request, pk):
    #return HttpResponse(f'Мороженое номер {pk}') 
