from selenium import webdriver
import time
#abrir o navegador no caso o edge
navegador= webdriver.Edge()
#acessar um site
navegador.get('https://www.hashtagtreinamentos.com/')

navegador.maximize_window()#aumentar a tela
#encontrar um elemento
lista_botoes = navegador.find_elements("class name", "header__titulo")

for botao in lista_botoes:
    if "Assinatura" in botao.text:
        botao.click()
        break

#botao_verde.click()
time.sleep(20)