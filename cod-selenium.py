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

#selecionar uma aba
abas = navegador.window_handles
navegador.switch_to.window(abas[1])

navegador.get("https://www.hashtagtreinamentos.com/curso-python")

campo_nome=navegador.find_element("id","firstname").send_keys("Caio")
campo_nome=navegador.find_element("id","email").send_keys("email@aleatorio.com")
campo_nome=navegador.find_element("id","phone").send_keys("1234")
#botao_verde.click()
time.sleep(30)