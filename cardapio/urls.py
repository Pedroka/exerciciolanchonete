from django.conf.urls import url
from cardapio.views import cardapio_lanches, monte_o_seu_lanche

app_name = 'lanches'
urlpatterns = [
    url('', cardapio_lanches,name='lanches'),
]