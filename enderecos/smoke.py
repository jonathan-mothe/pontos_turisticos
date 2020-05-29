from smoketest import SmokeTest
from rest_framework import status
from rest_framework.response import Response
import requests


 # GET /enderecos - para listar
class ApiDemoTestGet(SmokeTest):
    
    def test_endereco_get(self):
        headers = {'Authorization': 'Token 7b9969eca3e0a1713b597f106251e9684eff5f94'}
        url = 'http://127.0.0.1:8000/enderecos/'

        resposta = requests.get(url, headers=headers)
        resposta_dict = resposta.json()
        self.assertTrue(resposta_dict)


# POST /enderecos - para criação
class ApiDemoTestPost(SmokeTest):

    def test_endereco_post(self):
        headers = {'Authorization': 'Token 7b9969eca3e0a1713b597f106251e9684eff5f94'}
        url = 'http://127.0.0.1:8000/enderecos/'
        new_endereco = {
            'linha1': 'Mais um', 
            'linha2': 'Mais um2', 
            'cidade': 'Belo Horizonte', 
            'estado': 'MG', 
            'pais': 'Brasil'
        }

        resposta = requests.post(url, headers=headers, data=new_endereco)
        resposta_dict = resposta.json()
        endereco_response = resposta_dict
        
        self.assertTrue(endereco_response)


# PATCH /enderecos/:id - para atualização parcial 
class ApiDemoTestPatch(SmokeTest):

    def test_endereco_patch(self):
        headers = {'Authorization': 'Token 7b9969eca3e0a1713b597f106251e9684eff5f94'}
        url = 'http://127.0.0.1:8000/enderecos/45/'
        update_endereco = {
            'latitude': '666666', 
            'longitude': '777777'
        }

        resposta = requests.patch(url, headers=headers, data=update_endereco)
        resposta_dict = resposta.json()
        endereco_response = resposta_dict
        
        self.assertTrue(endereco_response)


# PUT /enderecos/:id - para editar
class ApiDemoTestPut(SmokeTest):

    def test_endereco_put(self):
        headers = {'Authorization': 'Token 7b9969eca3e0a1713b597f106251e9684eff5f94'}
        url = 'http://127.0.0.1:8000/enderecos/48/'
        update_endereco = {
            'linha1': 'Test PUT', 
            'linha2': 'Test PUT2', 
            'cidade': 'Pernambuco', 
            'estado': 'PE', 
            'pais': 'Brasil'
        }

        resposta = requests.put(url, headers=headers, data=update_endereco)
        resposta_dict = resposta.json()
        endereco_response = resposta_dict

        self.assertTrue(endereco_response)



# DELETE /enderecos/:id - para deleção 
class ApiDemoTestDelete(SmokeTest):

    def test_endereco_delete(self):
        headers = {'Authorization': 'Token 7b9969eca3e0a1713b597f106251e9684eff5f94'}
        url = 'http://127.0.0.1:8000/enderecos/49/'
#        delete_endereco = {}
        
        resposta = requests.delete(url, headers=headers)
        resposta_dict = resposta.json()
        endereco_response = resposta_dict

        self.assertTrue(endereco_response)
  