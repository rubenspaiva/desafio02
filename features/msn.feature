# language: pt
Funcionalidade: Acessar uma notícia

  Cenario: ver uma notícia no site do msn
    Dado que eu acesso o site do msn
    Quando clico em uma notícia diferente da primeira
    E verifico que é a notícia certa
    Então fecho o navegador