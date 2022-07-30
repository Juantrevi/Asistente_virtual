import pandas
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def descargar_historias():
    excel_credenciales = r'C:\Users\Juan Manuel\Desktop\opc\opc.xlsx'

    df = pandas.read_excel(excel_credenciales)

    # user = df['usuario'][0]
    # psw = df['contraseña'][0]
    user = 'juan.treviranus'
    psw = '34813589jmt'

    url = 'https://gomedisys.welii.com/'
    cont = int(0)
    #SELECTORES:

    selector_usuario = '#uiUserName'
    selector_contraseña = '#uiUserPwd'
    selector_gp = '#uiPerfiles'
    boton_login = '#btSubmit'
    historias = 'https://gomedisys.welii.com/ExportArea/Export'
    ordenar_por_posicion = '#radioByPosition'
    filtro_historia = '//*[@id="accordionHistory"]/a'
    actividades = '//*[@id="accordionFilterHistory"]/div[1]/div[3]/div/div'
    # filtro_actividad = f'//*[@id="ddActivity_listbox"]/li[{cont}]'
    aniadir_arch_adj = '#isAddPdfFiles'
    filtros_por_egreso = '//*[@id="accordionEgress"]/a'
    desde = '#ddSearchStartEgress'
    hasta = '#ddSearchEndEgress'
    buscar_historias = '//*[@id="btnSearchRecord"]'
    generar_historias = '//*[@id="dvPatientActivitiesPast"]/div[2]/a[2]'
    consulta = '//*[@id="tabEncounters"]/ul/li[2]/a'
    nombre_altas = '#zipFileName'
    generar = '//*[@id="btndohc"]'
    his_desde = '#dateRequestStart'
    his_hasta = '#dateRequestEnd'
    consultar = '//*[@id="EHRExportConsultTab"]/div[1]/div[6]/a'

    #Abrir el navegador

    driver = webdriver.Chrome(executable_path = r'C:\Users\Juan Manuel\Documents\ChromeDriver\chromedriver')
    #Maximizar pantalla
    driver.maximize_window()
    driver.get(url)
    #Acciones
    driver.find_element(By.CSS_SELECTOR, selector_usuario).send_keys(user)
    driver.find_element(By.CSS_SELECTOR, selector_contraseña).send_keys(psw)
    driver.find_element(By.CSS_SELECTOR, selector_gp).click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, boton_login).click()
    time.sleep(1)
    driver.get(historias)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ordenar_por_posicion).click()
    time.sleep(1)
    driver.find_element(By.XPATH, filtro_historia).click()
    time.sleep(1)
    driver.find_element(By.XPATH, actividades).click()
    time.sleep(1)

    for n in range(0, 172):
        cont += 1
        if cont != 162 and cont != 163 and cont != 166 and cont != 167 and cont != 171 and cont != 170 and cont != 172:
            driver.find_element(By.XPATH, f'//*[@id="ddActivity_listbox"]/li[{cont}]').click()
            time.sleep(0.05)




    time.sleep(1)
    driver.find_element(By.XPATH, filtros_por_egreso).click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, aniadir_arch_adj).click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, desde).send_keys('21/7/2022')
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, hasta).send_keys('22/7/2022')
    time.sleep(1)
    driver.find_element(By.XPATH, buscar_historias).click()
    time.sleep(1)
    driver.find_element(By.XPATH, generar_historias).click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, hasta).send_keys('Altas')
    time.sleep(1)
    driver.find_element(By.XPATH, generar).click()
    time.sleep(1)
    driver.find_element(By.XPATH, consulta).click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, his_desde).send_keys('25/7/2022')
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, his_hasta).send_keys('25/7/2022')
    time.sleep(1)
    driver.find_element(By.XPATH, consultar).click()




    #Mas acciones dentro de la pagina


    time.sleep(7)

    #Cerrar
    driver.quit()

