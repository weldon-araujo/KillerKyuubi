<h1 align="center" >Hunting IOC</h1>

<p align="center">

  ![Imgur](https://i.imgur.com/HctvKhE.png)
  
</p>

<h4 align="center">
  
<!-- aqui é onde é colocados os budgets-->

![GitHub commit activity (main)](https://img.shields.io/github/commit-activity/w/weldon-araujo/Hunting_IOC)
![GitHub issues](https://img.shields.io/github/issues/weldon-araujo/Hunting_IOC)
![Badge em Desenvolvimento](https://img.shields.io/static/v1?label=status&message=em%20desenvolvimento&color=GREEN)
![GitHub Org's stars](https://img.shields.io/github/stars/weldon-araujo?style=social)

</h4>


<h1></h1>

* [Índice](#índice)
* [Descrição do Projeto](#descrição-do-projeto)
* [Status do Projeto](#status-do-Projeto)
* [Funcionalidades e Demonstração da Aplicação](#funcionalidades-e-demonstração-da-aplicação)
* [Tecnologias utilizadas](#tecnologias-utilizadas)
* [Pessoas Desenvolvedoras do Projeto](#pessoas-desenvolvedoras)
* [Conclusão](#conclusão)

<!-- Parte de descrição do projeto -->

<h1>Descrição do projeto</h1>

Essa ferramenta foi pensada para em auxiliar no processo de Cyber Threat Hunting, é comum que aliado a um processo de Cyber Threat Intell manual seja necessário tomar como parte do Cyber Threat Hunting uma grande quantidade de IOCs muitas vezes derivadas do processo de Cyber Threat Intell com intuiti de enriquecer o Cyber Threat Hunting ou mesmo validação de hipotese, conforme descreve a metodologia <a href="https://www.betaalvereniging.nl/wp-content/uploads/DEF-TaHiTI-Threat-Hunting-Methodology.pdf" target= "_blank" rel="noreferrer noopener nofollow">Tahiti</a>

 para validação de determinadas hipóteses, a separação ou organização desses IOCs de maneira manual torna-se um processo um tanto massivo e custoso, em uma primeira versão essa ferramenta se pré dispões em receber todos esses IOCs independentes da forma que estejam organizados e extraia essas informações, a nível de hard code, possobilitando extrair hashes MD5, SHA1 e SHA256, IPs, URLs e URIs.

Pensando em somar no processo na grande maioria das vezes essas extrações de IOCs tem a finalidade de servirem com insumo de buscas nas plataformas de SIENs, então por hora é possível escolher a forma de saida cobrindo atualmente saidas para o SIEM IBM Qradar ou Graylog.

<h3></h3>

<h4 align="center">
  
   :construction: Projeto em construção:construction:

</h4>

<h3></h3>

<!-- Modo de uso-->


<h1>Modo de uso</h1>

Para visualizar ajuda e verificar os parâmetros necessários.

```
python3 HuntingIOC.py -h
```



<!-- Parte de descrição de funcionalidades-->

# :hammer: Funcionalidades do projeto

- `Funcionalidade 1`: descrição da funcionalidade 1
