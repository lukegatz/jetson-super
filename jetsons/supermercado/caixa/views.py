import json

import requests
from django.http import JsonResponse
from django.shortcuts import render
from encoder.models import Decodificador as dc

# Aqui ficam as views do sistema de caixa
def teste(request):
    produto = requests.get('http://143.107.145.30:1026/v2/entities/urn:ngsi-ld:Leite:001')
    produto_forma = json.loads(produto.content)

    return JsonResponse(produto_forma)

def produto_com_imagem(request):
    produto = requests.get('http://143.107.145.30:1026/v2/entities/urn:ngsi-ld:Coca_Cola:001')
    produto_dict = json.loads(produto.content)

    imagem = produto_dict['imagem']['value']
    # problema com padding
    imagem = imagem + '===' # "===" é o máximo de padding
    # decodificando a imagem utilizando o método do Decoder
    img_decode = dc.decodificar(request, imagem)
    print(img_decode) # apenas garantindo que passamos um str aqui

    return render(request, 'produto.html', {'v_imagem': img_decode})

def lista_produtos(request, tag):
    # listaTags
    # listaTags = []
    # pegar carrinho pela tag, volta o id do carrinho
    # carrinho = request.get(tag)

    # while refProduto # como escrever aqui?
    # pegue as tags, armazene em listaTags

    # while enquanto tiver tag na lista
    # get produto pela tag
    # rode o decoder da imagem
    # armazenar os dados do produto para o render
    # get valor, some o valor

    # lista = request.get('http://143.107.145.30:1026/v2/entities/urn:ngsi-ld:Coca_Cola:001')
    pass

def tratar_promocoes(request):
    pass