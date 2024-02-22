# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PIL import Image

print('Cadastre os dados do seu perfil\n')
seu_nome = input('Entre com seu nome ou apelido preferido: ')
sua_idade = input('Entre com sua idade: ')
seu_esporte = input('Entre com seu esporte predileto: ')
seu_pet = input('Entre com o nome de seu Pet: ')
sua_banda = input('Entre com sua banda ou cantor favorito: ')

print('Olá ' + seu_nome + ' espero que você esteja bem. Com ' + sua_idade + ' anos, espero que pratique ' + seu_esporte + '.')

im = Image.open('foto.jpg')
im.show()