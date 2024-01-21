<h1 align="center" >Killer Kyuubi</h1>

<h4 align="center">

  ![Imgur](https://i.imgur.com/HctvKhE.png)
  
</h4>

<h4 align="center">
  
<!-- aqui é onde é colocados os budgets-->

![GitHub commit activity (main)](https://img.shields.io/github/commit-activity/w/weldon-araujo/Hunting_IOC)
![GitHub issues](https://img.shields.io/github/issues/weldon-araujo/Hunting_IOC)
![Badge em Desenvolvimento](https://img.shields.io/static/v1?label=status&message=em%20desenvolvimento&color=GREEN)
![GitHub Org's stars](https://img.shields.io/github/stars/weldon-araujo?style=social)

</h4>


<h1></h1>

<!-- Parte de descrição do projeto -->

<h1>Descrição do projeto</h1>

Essa ferramenta foi pensada para em auxiliar no processo de Cyber Threat Hunting, é comum que aliado a um processo de Cyber Threat Intell manual seja necessário tomar como parte do Cyber Threat Hunting uma grande quantidade de IOCs muitas vezes derivados do processo de Cyber Threat Intell com intuito de enriquecer o Cyber Threat Hunting ou mesmo validar hipoteses, conforme descreve a metodologia de Cyber Threat Hunting <a href="https://www.betaalvereniging.nl/wp-content/uploads/DEF-TaHiTI-Threat-Hunting-Methodology.pdf" target="_blank">Tahiti</a>, a ferramenta tem 2 propósitos iniciais, a extração e e tratamentos de certa quantidade de IOCs sendo IOCs que podem ou não fazer parte de um feed de inteligência.
A separação ou organização desses IOCs de maneira manual torna-se um processo um tanto quanto massante e custoso, essa ferramenta na versão atual se predispõe em receber todos esses IOCs independentes da forma que estejam organizados e tentar extrair essas informações, possobilitando extrair hashes MD5, SHA1 e SHA256, IPs, URLs e URIs.

Pensando em somar no processo na grande maioria das vezes essas extrações de IOCs tem a finalidade de servirem com insumo de buscas nas plataformas de SIENs, então por hora é possível escolher a forma de saida cobrindo saida em formato lista ou saida padrão.

<h3></h3>


<h4 align="center">
  
   :construction: Projeto em construção:construction:

</h4>

<h3></h3>

<!-- Modo de uso-->


<h1>Modo de uso</h1>

* Para visualizar ajuda e verificar os parâmetros necessários ou caso execute o script sem parâmetros.

```
python3 main.py -h
```
<h4 align="center">
  
![Imgur](https://i.imgur.com/8M0j8N7.png)

</h4>

* Os dados precisam ser copiados e colados a nivel de hard code no objeto "ioc" e após isso pode executar o script, neste exemplo iremos usar os IOCs disponibilizados no repositório do <a href="https://github.com/carbonblack/active_c2_ioc_public/blob/main/cobaltstrike/actor-specific/cobaltstrike_luckymouse_ta428.csv#L1" target="_blank">Carbonblack</a>

<h4 align="center">
  
  ![Imgur](https://i.imgur.com/NFDYt6C.png)

</h4>

<!-- Parte de descrição de funcionalidades-->

# :hammer: Funcionalidades do projeto

- `Funcionalidades ` De acordo com o parâmetro escolhido vai ser possível extrair as informações

<h4 align="center">

  ![Imgur](https://i.imgur.com/zXYlmqE.png)
  
</h4>

Após esse procedimentos os dados podemo ser utilizados nos processos de Cyber Threat Hunting como prefererir



