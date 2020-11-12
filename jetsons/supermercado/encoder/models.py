from django.db import models

# Create your models here.
# coding: UTF-8
import base64, uuid

'''
Funcionamento do processo de encode e decode dos arquivos a serem armazenados no server
'''

'''
A classe Codificador recebe um arquivo e retorna o string base64 que representa o arquivo
'''
class Codificador:

	def codificar(self, arquivo):
		with open(arquivo, 'rb') as arquivo_ler:
			dados = arquivo_ler.read()
			encoded = base64.b64encode(dados)
			base64_message = encoded.decode('utf-8')

		return base64_message


'''
A classe Decodificador recebe uma string, representando o arquivo que foi convertido, e retorna
um novo arquivo, com um nome aleatório
'''
class Decodificador:

	def decodificar(self, referencia):
		base64img_bytes = referencia.encode('utf-8')
		# pasta em que o arquivo será salvo
		pasta = 'imgs/encoded/'
		# o arquivo é PNG, por padrão
		arquivo = pasta + str(uuid.uuid4()) + ".png"

		with open(arquivo, 'wb') as file_to_save:
			decoded = base64.decodebytes(base64img_bytes)
			file_to_save.write(decoded)