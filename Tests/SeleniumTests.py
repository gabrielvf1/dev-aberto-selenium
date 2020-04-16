from selenium import webdriver
import os
import time

browser = webdriver.Chrome()
browser.get('http://Gabriel:Gabriel@0.0.0.0:80')
lista = browser.find_elements_by_class_name('nav-link')
browser.get("http://0.0.0.0/?ID=2")
browser.find_element_by_id("resposta").send_keys(os.getcwd()+"/Desafio5_errofuncinv.py")
browser.find_element_by_css_selector('.btn.btn-primary').click()
time.sleep(1)
browser.find_element_by_id("resposta").send_keys(os.getcwd()+"/Desafio5_errofuncerrada.py")
browser.find_element_by_css_selector('.btn.btn-primary').click()
time.sleep(1)
lista = browser.find_elements_by_class_name('table-responsive')
for i in lista:
    func_inv = i.text[44:65]
    func_err = i.text[86:140]

assert func_inv == "Função inválida. Erro"
assert func_err == "Nome da função inválido. Usar 'def desafio2(...)' Erro"

browser.get("http://0.0.0.0/?ID=1")
browser.find_element_by_id("resposta").send_keys(os.getcwd()+"/desafio.py")
browser.find_element_by_css_selector('.btn.btn-primary').click()
time.sleep(1)
browser.find_element_by_id("resposta").send_keys(os.getcwd()+"/desafio_erroabc.py")
browser.find_element_by_css_selector('.btn.btn-primary').click()
time.sleep(1)
lista = browser.find_elements_by_class_name('table-responsive')
for i in lista:
    erro_abc = i.text[44:54]
    sem_erro = i.text[75:89]

assert sem_erro == "Sem erros. OK!"
assert erro_abc == "a b c Erro"
browser.find_element_by_css_selector('.btn.btn-light.my-2.my-sm-0').click()
logout_text = browser.find_element_by_css_selector(".alert.alert-warning").text
assert logout_text == "Logout com sucesso"

print("Teste Bem Sucedido")