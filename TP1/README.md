# Website de Reviews Com Análise de Sentimento
## Introdução
Este projeto consistiu na exploração de três módulos de *Python* - NLTK, Flask
e PyMongo - e no desenvolvimento de uma aplicação que os conjuga. Esta trata-se
de um *webserver* simples que permite visualizar, editar e remover *reviews*,
bem como realizar uma análise de sentimento às mesmas.

## Módulos utilizados
- NLTK: Processamento de linguagem e análise de sentimento
- Flask: Servidor web
- Pymongo: Base de dados

## NLTK
O NLTK (*Natural Language ToolKit*) é um conjunto de módulos *Python*
relacionados com o processamento de linguagem natural.

Neste projeto, o NLTK foi utilizado para realizar a análise de sentimento. Esta
análise foi realizada utilizando o módulo _VADER_ [1](#1).

O _VADER_ é um analisador simples, que funciona à base de palavras individuais.
Cada palavra ou modificador tem um peso negativo ou positivo associado, que são
combinados para gerar pontuações positivas e negativas no final.

Esta análise de sentimentos é bastante falível, sendo que tem dificuldade a
identificar a polaridade de textos mais complexos, bastando apenas utilizar
palavras mais positivas para expressar uma opinião negativa (ou vice-versa)
para obter um resultado errado. Por exemplo:

- _Almost anything is better than this movie._ - Avaliado como positivo
- _This movie does not deserve all the hate it gets._ - Avaliado como negativo

De modo a simplificar o texto para a análise de sentimento, é feito um
pré-processamento simples, que remove as _stop words_ e lematiza todas as
palavras restantes. As frases acima, após serem processadas, geram o seguinte
texto:

- _almost anything better movie ._
- _movie deserve hate get ._

Como podemos ver, o pré-processamento não é infalível, sendo até que no segundo
caso inverteu o significado da frase, removendo o qualificador negativo ("does
not").

## Flask
Flask é uma *framework web* simples e *lightweight*, sendo até considerada uma
*microframework*. O seu principal objetivo é facilidade de utilização e de
escalar para aplicações mais complexas.

Neste projeto, esta ferramenta foi utilizada para realizar *routing*
relativamente básico, maioritariamente permitindo responder a pedidos *GET* e
*POST*. A utilização do *template engine default* do Flask, Jinja, tornou mais
agradável e fácil a geração das páginas *web*.

## PyMongo
O PyMongo permitiu-nos facilmente aceder e manipular uma coleção de *reviews*
da nossa base de dados no *MongoDB* do projeto. Permite-nos fazer *queries* à
base de dados de uma forma intuitivamente semelhante à *shell* oficial do
*MongoDB*. Utilizamo-la para obter, remover, adicionar e modificar _reviews_.

## Conclusão
Utilizando um conjunto de módulos simples de python, foi-nos possível criar uma
webapp interessante rapidamente. Como constatado, a webapp não é perfeita
devido ao uso de ferramentas de análise algo rudimentares, mas estamos de
qualquer forma satisfeitos com o trabalho realizado dada a escala do âmbito do
projeto.

# Bibliografia
<a id="1">[1]</a>
Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for
Sentiment Analysis of Social Media Text. Eighth International Conference on
Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.

<a id="2">[2]</a>
https://flask.palletsprojects.com/en/2.2.x/

<a id="3">[3]</a>
https://pymongo.readthedocs.io/en/stable/
