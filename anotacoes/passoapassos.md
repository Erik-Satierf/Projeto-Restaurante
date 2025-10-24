# Como criar uma classe no Django

## Passo 1: Criar Backend

1. crie um ambiente virtual para isolar o projeto, no terminal escreva:
```bash
python -m venv venv
```

depois ative ele:
```bash
venv\Scripts\activate
```

2. Instale o Django, no terminal
```bash
pip install django
```

3.Crie o Projeto base
no terminal escreva
```bash
django-admin startproject backend .
```

4.Roda o servidor pela primeira vez
Terminal
```bash
python manage.py runserver
```
## Passo 2: Instalar Django REST Framework
1. terminal
```bash
pip install djangorestframework
```
2. Registrar no Projeto em backend/settings.py
em INSTALLED_APPS deixe dessa forma
```bash
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
]
```
## Passo 3: Criar a pasta (App) da classe

1. Abra o terminal e digite o comando:

```bash
python manage.py startapp nome_da_classe
```

2. Tambem registre em INSTALLED_APPS
```bash
INSTALLED_APPS = [
    ...
    'rest_framework',
    'cardapio',
]
```

3. Depois que a aplicação for criada, abra o arquivo models.py dentro da nova pasta.
Lá dentro, crie sua classe e defina os atributos

```bash
from django.db import models

class [Classe](models.Model):
    [atributo] = models.[tipo_de_atributo](max_length=255)
    [atributo] = models.[tipo_de_atributo](max_digits=6, decimal_places=2)
                                                                                
    def __str__(self):
        return self.atributo    //retorna o atributo

"max_lenght" = maximo de caracteres
"max_digits" = maximmo de digitos
"decimal_places" = casas decimais, usada principalmente em dinheiro
```

4. Dentro da pasta da classe criada procure por urls.py e escreva isso:
```bash
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import [Classe]ViewSet

router = DefaultRouter()
router.register(r'[classe]', [Classe]ViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

5. E por fim, conecta isso ao urls principal do projeto (backend/urls.py):
```bash
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('[classe].urls')),
]
```
6. Rode e teste
```bash
python manage.py runserver
```
## Passo 4: Testar no insomnia

1. Aplica as migracoes para o banco de dados
no terminal digita um e dps o outro
```bash
python manage.py makemigrations
python manage.py migrate
```

2. Cria o serializers na classe, novo arquivo chamado "serializers.py", digita la
```bash
from rest_framework import serializers
from .models import [Classe]

class [Classe]Serializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = '__all__'  # vai pegar todos os campos: id, nome, preco
```

3. Criar a viewSet
No cardapio/views.py substitui ou adiciona:
```bash
from rest_framework import viewsets
from .models import [Classe]
from .serializers import [Classe]Serializer

class [Classe]ViewSet(viewsets.ModelViewSet):
    queryset = [Classe].objects.all()
    serializer_class = [Classe]Serializer
```

4. Configurar URLs
No cardapio/urls.py:
```bash
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import [Classe]ViewSet

router = DefaultRouter()
router.register(r'[classe]', [Classe]ViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```
E no backend/urls.py, garante que tá assim:
```bash
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('[class].urls')),
]
```