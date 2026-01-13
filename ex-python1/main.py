import pyautogui as pygui
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://g1.globo.com/")

elementos = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "a.gui-color-primary")
    )
)

lista_noticias = []
for e in elementos:
    texto = e.text.strip()
    if texto != '':
        lista_noticias.append(texto)
    
driver.quit()
df = pd.DataFrame(lista_noticias, columns=['Noticia'])
df.to_excel("noticia.xlsx", index=False)
#pygui.click(x=20, y=170)
#pygui.write('03951572000')
#pygui.press('tab')
#pygui.press('enter')


