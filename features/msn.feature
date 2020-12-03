# language: pt
Funcionalidade: Acessar uma notícia

  Cenario: ver uma notícia no site do msn
    Dado que eu acesso o site do msn
    Quando clico em uma notícia diferente da primeira
    Então verifico que é a notícia certa e fecho o navegador
