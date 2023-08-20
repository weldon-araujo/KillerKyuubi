<h1>Intuito da ferramenta</h1>

<p>Esta ferramenta tem o intuito de auxiliar no processo de Cyber Threat Hunting, principalmente na fase 2 da metodologia [Tahiti](https://www.betaalvereniging.nl/en/safety/tahiti/)</p> Realizar extração de IOCs de quantidades de grandes de dados é o principal intuito, podendo então nas versão até o momento presente extrair IOCs de URLs, URIs, IPs, Hashes MD5, SHA1 e SHA256.

<h2>Saidas de dados</h2>

<p>Inicialemnte a ferramenta busca modelar a saida pra 2 SIEMs IBM Qradar e Graylog e tambem em formato de saida padrão de terminal</p>

<h2>Modo de usar</h2>

A ferramenta segue o padrão **hard code** podendo pegar todo os dados que você planeja extrair e colocando no valor da variavel **ioc** depois basta executar o script em command line

`python3 HuntingIOC.py --help`
 