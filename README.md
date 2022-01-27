# NFTnews
## Introdução
Esse repositório contém o site desenvolvido para o trabalho final da disciplina de Algoritmos de Automação do master em Jornalismo de Dados, Automação e Data Storytelling do Insper.

## Proposta
Criar um programa que seja útil e cumpra **pelo menos um** dos seguintes requisitos:
- [ ] Interação via robô no Telegram (usando a API)
- [x] Site com página dinâmica (usando Flask)
- [x] Coleta/modifica dados em planilha do Google Sheets (usando a biblioteca gspread)
- [x] Executa algum script recorrentemente através do Heroku Scheduler

## Sobre o site
O objetivo do NFTnews é coletar, a acada uma hora, as dez notícias mais recentes com o termo NFT (sigla em inglês para *tokens não-fungíveis*). Essas notícias [alimentam uma planilha](https://docs.google.com/spreadsheets/d/1l6sXZtoAv0I-lY9q3m1rnfq5JMM5h12fDKj4kEIYhU8/edit?usp=sharing), que atualiza automaticamente uma visualização no [flourish](https://public.flourish.studio/visualisation/8189942/). Foi feito o embed dessa visualização no site [nftnews](https://nftnews.herokuapp.com/).

## Instalação
O site foi feito para rodar no [Heroku](https://www.heroku.com/) e depende das bibliotecas: `flask`, `gspread`, `googlenews` e outras.
