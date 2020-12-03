from selenium import webdriver

#1. abra o navegador
navegador = webdriver.Chrome()

#2. acesse o msn.com
navegador.get('https://www.msn.com')

#3. acesse uma notícia da área de destaques (diferente da primeira)
noticia = navegador.find_element_by_xpath('//*[@id="main"]/div[6]/ul/li[3]/a/div/span[1]')
titulo = navegador.find_element_by_xpath('//*[@id="main"]/div[6]/ul/li[3]/a/div/span[1]').text
noticia.click()

#4. verifique se é mostrada a página esperada
assert (titulo in navegador.page_source) 

#5. feche o navegador
navegador.quit()
