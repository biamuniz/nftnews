# NFTnews (em desenvolvimento)
## Introdução
Esse repositório contém o site desenvolvido para o trabalho final da disciplina de Algoritmos de Automação do master em Jornalismo de Dados, Automação e Data Storytelling do Insper.

## Proposta
Criar um programa que seja útil e cumpra **pelo menos um** dos seguintes requisitos:
- [ ] Interação via robô no Telegram (usando a API)
- [x] Site com página dinâmica (usando Flask)
- [x] Coleta/modifica dados em planilha do Google Sheets (usando a biblioteca gspread)
- [x] Executa algum script recorrentemente através do Heroku Scheduler

## Sobre o site
O objetivo do NFTnews é coletar, a cada dez minutos, as dez notícias mais recentes com o termo NFT (sigla em inglês para *tokens não-fungíveis*). Essas notícias [alimentam uma planilha](https://docs.google.com/spreadsheets/d/1l6sXZtoAv0I-lY9q3m1rnfq5JMM5h12fDKj4kEIYhU8/edit?usp=sharing), que atualiza automaticamente uma visualização no [flourish](https://public.flourish.studio/visualisation/8189942/). Foi feito o embed dessa visualização no site [nftnews](https://nftnews.herokuapp.com/) — que não está funcionando. *Por enquanto*.

## Instalação
O site **foi feito** para rodar no [Heroku](https://www.heroku.com/) e depende das bibliotecas: `flask`, `gspread`, `googlenews` e outras.


## Tarefas
Ainda não é a versão final do site; o programa cumpre, parcialmente, o exercício proposta. O código para a coleta de notícias e atualização da planilha funciona, quando rodado no [Google Collab](https://colab.research.google.com/drive/1KtUarAJ0cECvEHzSX8ExwptlRhlbOFrl?usp=sharing), o que também atualiza a visualização no flourish; porém, depende de uma interação no notebook. Não há execução recorrente do script, nem a integração com o Heroku e com a página dinâmica 😢. Próximas tarefas:
- [ ] Descobrir quais erros impedem a execução do script, bem como a atualização automática do site/planilha.
