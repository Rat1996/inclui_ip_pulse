from selenium import webdriver
import time
import csv
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pprint import pprint

#=====================================Funçoes

#Aguarda tela carregar

def aguardarCarregamento(driver: webdriver):
    WebDriverWait(driver=driver, timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )

#inicia o navegador

def iniciarNavegador(url: str = "http://IP_SIP_PULSE:8080/SipPulseAdmin/pages/login/login.jsf"):
    # Iniciar Chrome
    driver = webdriver.Chrome("chromedriver")

    # Ler página  de login
    driver.get(url)
    return driver

#Faz o login na pulse

def fazerLogin(username: str, password: str, driver: webdriver):
    # Encontrar elemento 'username' e inserir texto
    driver.find_element(By.NAME, "j_username").send_keys(username)

    # Encontrar elemento 'password' e inserir texto
    driver.find_element(By.NAME, "j_password").send_keys(password)

    # Clicar em login utilizando o classe como referência
    driver.find_element(By.XPATH, "/html/body/table/tbody/tr[3]/td/form/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[5]/td/div/input").click()

    # Aguardar login terminar de submeter
    aguardarCarregamento(driver)

    return True

def salvarPagina(driver: webdriver):
    driver.find_element(By.ID, "frmSubscriber:j_id1078").click()
    time.sleep(3)
    driver.find_element(By.ID, "frmSubscriber:j_id1072").click()
    aguardarCarregamento(driver)
    return True

def banner():
    banner = """
          _____ _____  
    _    |_   _|  __ \ 
  _| |_    | | | |__) |
 |_   _|   | | |  ___/ 
   |_|    _| |_| |     
         |_____|_|     
                       
                       
                        1.0 por Carlos              

    """
    print(banner)


def clickAutenticaIP(el:str, by:str, driver: webdriver):
    driver.find_element(By.XPATH, "/html/body/table/tbody/tr[6]/td/form/center/table/tbody/tr[1]/td[2]/table/tbody/tr[5]/td/a").click()
    aguardarCarregamento(driver)
    return True

def clickNewAutenticaIP(driver: webdriver):
    driver.find_element(By.XPATH, "/html/body/table/tbody/tr[6]/td/form[1]/div[2]/input[3]").click()
    aguardarCarregamento(driver)
    return True

def clickPesquisaSub(assinante:str, driver: webdriver):
    driver.find_element(By.XPATH, "/html/body/table/tbody/tr[6]/td/form/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/a/img").click()
    driver.find_element(By.XPATH, '//*[@id="FromLovSubscriber:filterData"]').send_keys(assinante)
    driver.find_element(By.XPATH, '//*[@id="FromLovSubscriber:j_id258"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="FromLovSubscriber:listSubscribers:0:linkSelectSubscriber"]').click()
    aguardarCarregamento(driver)
    return True

def fillAutenticaIP(ip:str, driver:webdriver):
    driver.find_element(By.XPATH, '//*[@id="frmAddress:ip"]').send_keys(ip)
    driver.find_element(By.XPATH, '//*[@id="frmAddress:port"]').send_keys('0')
    driver.find_element(By.XPATH, '//*[@id="frmAddress:mask"]').send_keys('32')
    driver.find_element(By.XPATH, '//*[@id="frmAddress:group"]').clear()
    driver.find_element(By.XPATH, '//*[@id="frmAddress:group"]').send_keys('0')
    aguardarCarregamento(driver)
    return True

def selectMetodo(driver:webdriver):
    driver.find_element(By.XPATH, "/html/body/table/tbody/tr[6]/td/form/div[1]/div[2]/table/tbody/tr[2]/td[4]/div/select/option[2]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="frmAddress:techprefix"]').send_keys(assinante)
    aguardarCarregamento(driver)
    return True

def salvarPagina(driver: webdriver):
    driver.find_element(By.ID, "frmAddress:j_id241").click()
    time.sleep(3)
    driver.find_element(By.ID, "frmAddress:j_id235").click()
    aguardarCarregamento(driver)
    return True

banner()

assinante = input ("Tech do cliente: ")
ip = input ("IP: ")


driver = iniciarNavegador()
fazerLogin('USUARIO', 'SENHA', driver)
clickAutenticaIP('Subscriber', 'Subscriber', driver)
clickNewAutenticaIP(driver)
clickPesquisaSub(assinante, driver)
fillAutenticaIP(ip, driver)
selectMetodo(driver)
salvarPagina(driver)
time.sleep(2)

#====================Altera os numeros e salva pagina=============================


#=================================================
#clickEmUmElemento()
aguardarCarregamento(driver)
#lerTabelaUsuariosCDR(driver)
# encerrarConexaoDrive(driver)
exit()
