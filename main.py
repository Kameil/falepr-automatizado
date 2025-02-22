from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Chrome()

browser.get('https://falepr.presidencia.gov.br/form/')


try:
    browser.execute_script("acessarSistema()")
except:
    pass


time.sleep(1)
terms_1 = browser.find_element(By.XPATH, '//*[@id="form"]/div[1]/div/div[1]/div/label')
terms_2 = browser.find_element(By.XPATH, '//*[@id="form"]/div[1]/div/div[3]/div/label')
terms_1.click()
terms_2.click()
time.sleep(0.5)
btn_continua = browser.find_element(By.XPATH, '//*[@id="form"]/div[2]/div/button')
btn_continua.click()


# form tlgd

time.sleep(2)



nome = browser.find_element(By.NAME, "nom_agente")
nome.send_keys("Orea seca")


paises = browser.find_element(By.XPATH, '//*[@id="form"]/div[4]/div/div/div[1]/button/div')
paises.click()
brasil = browser.find_element(By.XPATH, '//*[@id="form"]/div[4]/div/div/div[1]/div/div[2]/ul/li[29]')
brasil.click()

cep = browser.find_element(By.NAME, "num_cep")
cep.send_keys("60525345", Keys.ENTER)

sexo = browser.find_element(By.NAME, "cod_sexo")
SexoSelect = Select(sexo)
SexoSelect.select_by_value("1")

faixa_etaria = browser.find_element(By.NAME, "cod_faixa_etaria")
FaixaEtariaSelect = Select(faixa_etaria)
FaixaEtariaSelect.select_by_value("2")

email = "desenrolado@gmail.com"
email_input = browser.find_element(By.NAME, "dsc_email")
emailConfirm_input = browser.find_element(By.NAME, "dsc_email_confirma")
email_input.send_keys(email)
emailConfirm_input.send_keys(email)

texto = browser.find_element(By.NAME, "dsc_texto")
texto.send_keys("Olá, sera que o senhor presidente poderia enviar uma foto oficial para mim?")

time.sleep(10)