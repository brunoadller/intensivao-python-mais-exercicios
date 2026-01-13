import pyautogui as pygui
import time
#tempo de sepera entre os comandos do pyautogui
pygui.PAUSE = 1


#abrir o chrome e pesguisar o link
pygui.press('win')
pygui.write('chrome')
pygui.press('enter')
pygui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pygui.press('enter')


#espera carregar
time.sleep(3)

#fazer login (aqui pode preencher qualquer login)
# Passo 2: Fazer login
# selecionar o campo de email
pygui.click(x=685, y=400)
# escrever o seu email
pygui.write("pythonimpressionador@gmail.com")
pygui.press("tab") # passando pro próximo campo
pygui.write("suasenha@1234#")
pygui.press('tab') # clique no botao de login
pygui.press('enter')
time.sleep(3)

#utilizando pandas
import pandas as pd

table = pd.read_csv('docs/produtos.csv')

for linha in table.index:
    codigo = str(table.loc[linha, 'codigo'])
    marca = str(table.loc[linha,'marca'])
    tipo = str(table.loc[linha, 'tipo'])
    categoria = str(table.loc[linha, 'categoria'])
    preco_unitario = str(table.loc[linha, 'preco_unitario'])
    custo = str(table.loc[linha, 'custo'])
    obs = table.loc[linha, 'obs']
    
    pygui.click(x=685, y=294)
    pygui.write(codigo)
    pygui.press('tab')
    pygui.write(marca)
    pygui.press('tab')
    pygui.write(tipo)
    pygui.press('tab')
    pygui.write(categoria)
    pygui.press('tab')
    pygui.write(preco_unitario)
    pygui.press('tab')
    pygui.write(custo)
    pygui.press('tab')
    if not pd.isna(obs):
        pygui.write(obs)
    pygui.press('tab')
    pygui.press('enter')