from logs import logs, criar_mensagem_error
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from navegador import SeleniumDriver
import os
from time import sleep
navegador = SeleniumDriver()
driver = navegador.run()

# Definindo um parâmetro padrão de busca
parametro_busca_padrao = 'blogs de suplementos alimentares'
# Dando a oportunidade do usuário inserir uma nova busca
parametro_busca = '' # input("Insira um parâmetro de busca, caso oposto vamos pegar um padrão:\n\n")
# se o usuário não inserir pega o padrão
parametro_busca = parametro_busca_padrao if parametro_busca == "" else parametro_busca
# Define a url
url_base =  f"https://www.google.com/search?q={parametro_busca}&hl=pt-BR"

# Abrindo o navegador
driver.get(url=url_base)
# Instancia expressões de manipulação do navegador
actions = ActionChains(driver)
# driver.maximize_window()
# Pegando os resultados de pesquisa
campo01 = driver.find_elements(By.XPATH, "//div[@class='yuRUbf']/div/span/a/div/div/div/span")  #titulo01
campo02 = driver.find_elements(By.XPATH, "//div[@class='yuRUbf']//h3")                          #titulo02
campo03 = driver.find_elements(By.XPATH, "//div[contains(@class,'VwiC3b yXK7lf')]//span")       #subtexto
# campo04 = driver.find_elements(By.XPATH, "//div[@class='yuRUbf']/div/span/a/@href")             #http
campo04 = driver.find_element(By.)

# resultados = []
# [print(resultado.text) for resultado in resultados]

[print(c1.text) for c1 in campo01]
[print(c2.text) for c2 in campo02]
[print(c3.text) for c3 in campo03]


# pausando o processo, é interessante para debugar rsrs :D
sleep(20)
driver.quit()

