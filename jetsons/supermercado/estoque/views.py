import json

import requests
from django.http import JsonResponse
from django.shortcuts import render
from supermercado.encoder import Decodificador

# Create your views here.
def teste(request):
    produto = requests.get('http://143.107.145.30:1026/v2/entities/urn:ngsi-ld:Leite:001')
    produto_forma = json.loads(produto.content)

    return JsonResponse(produto_forma)


def produto_com_imagem(request):
    produto = requests.get('http://143.107.145.30:1026/v2/entities/urn:ngsi-ld:Leite:001')
    produto_dict = json.loads(produto.content)

    imagem = produto_dict['imagem']
    imagem_string = imagem['value']

    img_decode = Decodificador.decodificar(imagem_string)

    return render(request, 'produto.html', {'v_imagem': img_decode})


def decodificar_imagem(imagem):
    pass