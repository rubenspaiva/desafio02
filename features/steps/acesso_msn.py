from behave import given, when, then
from selenium.webdriver import Chrome

@given('que eu acesso o site do msn')
def acessar_pagina(context):
    context.browser = Chrome()
    context.browser.get('https://www.msn.com.br')

@when('clico em uma notícia diferente da primeira')
def clicar_noticia(context):
    context.noticia = context.browser.find_element_by_xpath('//*[@id="main"]/div[5]/ul/li[3]/a/div/span[1]')
    context.texto = context.browser.find_element_by_xpath('//*[@id="main"]/div[5]/ul/li[3]/a/div/span[1]').text
    context.noticia.click()

@then('verifico que é a notícia certa e fecho o navegador')
def verificar_noticia_e_fechar_navegador(context):
    assert (context.texto in context.browser.page_source)
    context.browser.close()
