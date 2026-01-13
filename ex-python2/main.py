from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


driver = webdriver.Chrome()
driver.get('https://quotes.toscrape.com/')


quotes = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "quote"))
)
lista = []
for quote in quotes:
    text = quote.find_element(By.CLASS_NAME, 'text').text
    author = quote.find_element(By.CLASS_NAME, 'author').text
    tags = quote.find_elements(By.CLASS_NAME, 'tag')
    tags_text = ', '.join([tag.text for tag in tags])
    lista.append(
        {'Texto da Citação': text, 'Autor': author, 'Tags': tags_text}
                 )

print(lista)

df = pd.DataFrame(lista)

df.to_excel('citações.xlsx', index=False)