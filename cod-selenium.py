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

navegador.get("https://www.hashtagtreinamentos.com/curso-python")

#selecionar uma aba
abas = navegador.window_handles
navegador.switch_to.window(abas[0])



campo_nome=navegador.find_element("id","firstname").send_keys("Caio")
campo_nome=navegador.find_element("id","email").send_keys("email@aleatorio.com")
campo_nome=navegador.find_element("id","phone").send_keys("1234")

botao_para_clicar=navegador.find_element("id",'_form_2475_submit').click()
#aqui passando o botao_para_clicar como argumento para ser centralizado na pagina do javascript
navegador.execute_script("arguments[0].scrollIntoView({block:'center'})",botao_para_clicar)

#espera
#time.sleep(3)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

espera= WebDriverWait(navegador,10)
espera.until(EC.element_to_be_clickable(botao_para_clicar))

botao_para_clicar.click()
time.sleep(30)