# Pergunta 1.1

As PETs (Privacy-Enchancing Technologies) são usadas para implementar padrões de design para "gerar" privacidade no software. Um exemplo de um PET poderia ser o Onion Routing que anonimiza o utilizador.

As seguintes 8 estrategias sugeridas pela ENISA podem ser dividas em duas classes:

- Data Oriented Strategies
- Process Oriented Strategies

As quatro primeiras correspondem a Data Oriented Strategies e as outras quatro são Process Oriented strategies:

- MINIMISE - Esta estrategia básica limita-se a, seja na altura de design ou no Run Time, minimizar a quantidade de informação pessoal que recolhe do utilizador. Recolhendo só a informação estritamente necessário para o funcionamento do software. Ex: 'Select before you collect' , 'anonymisation and use pseudonyms'.

- HIDE - O design pattern tem como objetivo esconder a informação privada/pessoal do utilizador como as relações entre elas. O que se deve esconder e de quem depende das informações tratadas e o contexto onde esta estrategia é aplicada. Por exemplo, pode-se esconder a informação coletada de outras entidades mas manter pública dentro da entidada que a recolheu e esconder toda a informação gerado durante comunicações entre Hosts, assim, garantindo confidencialidade e Unlinkability. Este último referindo à impossibilidade de relacionar dois eventos. Este pattern pode ser conseguido através de mix Networks, attribute based credentials e usando encriptação dos dados.

- SEPARATE - Diferentes tipos de dados pessoais devem ser processados e, se possível, guardados em localizações diferentes. Utiliza-se este design para impedir profilling do utilizador ao recolher vários dados pessoais sobre o mesmo utilizador. Este tipo de estrategia implementa-se em soluções distribuidas para que os dados sejam separados por diversas base de dados e processados em diversos locais. E as rows das bases dados devem usar pseudonimos para dificultar o processo de relacionar dados dentro da base de dados.

- AGGREGATE - Os dados pessoais de várias pessoas devem ser agrupados tornando-os genericos, isto é, tornando-os possíveis dados para diversos utilizadores desde que o grupo seja grande o suficiente. Alguns exemplos de este design posto em prática são: Aggregation over time, k-anonimity e outras técnicas de anonimização.

- INFORM - O processamento de dados, o porquê, quais dados e para que propósito deve ser esclarecido ao utilizador. Também deve ser informado de como é que os dados são protegidos de maneira transparente. Alguns exemplos: P3P ( Platform for Privacy Preferences) e notificações de Data Breaches.

- CONTROL - Funciona como um complento a estrategia INFORM e o contrário também se verifica. O que se pretende é dar controlo ao utilizador de que dados este dá consentimento de ser usados. E,se permite que outros sistemas usem esses mesmos dados. É importante que se faça o design user-friendly para configurar estes consentimentos para o processo ser transparente. Exemplos: Sistema de gestão da identidade de utilzador.

- ENFORCE - O design pretende forçar a implementação de politicas de privacidade compativeis com requisitos legais. No minimo, tem que existir mecanismos que impeçam a "violação" das politicas de privacidade definidas. Ainda em conjunto deve existir estruturas governamentais que também pressionem as empresas a implementar essas politicas. Exemplo: Controles de Acesso e um sistema de gestão dos diretios de privacidade.

- DEMONSTRATE - Esta estrategia mais forte que a anterior pretende que seja possível demonstrar que o sistema está de acordo com as politicas de privacidade como também os requisitos legais da mesma. Ou seja, o sistema tem que demonstrar como é que realmente a politica de privacidade está implementada. Exemplo: Um sistema de Logging e Auditing.

# Pergunta 1.2

O use case que vai ser analisado seguindo a metodologia definida pelo *HandBook on Security of Personal Data Processing* da ENISA é o do processo de avaliação de empregados. Primeiramente, apresentar-se-á a metodologia, seguidamente o use case que está descrito no mesmo documento e aplicação da metodologia. Concluindo com algumas medidas que poderiam ser utilizados no problema em questão retirados dos Anexos do mesmo documento.

A metodologia descrita pela ENISA segue quatro passos para avaliação do risco:

- Definição do processo da operação em questão como o seu contexto

- Comprensão e avaliação do Impacto

- Definação das possíveis ameaças e a sua probabilidade de ocorrência

- Avaliação do risco (Risco = probabilidade de Ocorrencia * Impacto , por exemplo)

Seguidamente, o data controller propõe medidas de segurança retiradas da lista proposta em anexo segundo o nível de risco.

## Definição do processo da operação em questão como o seu contexto

Neste passo responde-se a uma série de questões para perceber quais os tipos de dados processados, qual o próposito dos mesmos, que tipos de dados, a localização do processamento dos dados, etc. Assim, percebendo o contexto do processo em qualquer das fases do processamento de dados (recolha,armazenamento,uso,transferência,etc.)

## Comprensão e avaliação do Impacto

Neste segundo passo avalia-se o impacto que as várias fases do processamento de dados. Classificando-as com um dos seguintes níveis: Low, Medium, High, Very High. Durante esta classificação deve-se ter em contas diferentes aspetos como o tipo de dados, volúme de dados, criticidade da operação, etc. O próprio documento fornece uma tabela para "ajudar" neste processo.

## Definação das possíveis ameaças e a sua probabilidade de ocorrência

O data controller tem que perceber quais as ameaças relativas ao processamento de dados como a sua probabilidade de ocorrência. Para tal, analisa-se em quatro dimensôes:

- Recursos técnicos e rede
- Processos/Procedimentos relacionados ao processemanto de dados
- Grupos de pessoas como individuos involvidos no processamento de dados
- Setor de negócio e escalo do processamento (volúme de dados)

Analisando o processo segundo estas dimensões deve-se chegar uma conclusão sobre a probabilidade de ocorrẽncia. O documento providencia com uma tabela que usa um Score System atribuido através de perguntas. Ao sumar os vários resultados das perguntas chega-se a um resultado que mapeia para um nivel de probabilidade de ocorrência da ameaça (Low,Medium,High).

## Avaliação do risco

Neste passo deve-se cruzar a avaliação de impacto como a probabilidade de ocorrência para chegar ao nível de risco. O documento disponibiliza-se uma tabela que tem este próposito. Ainda o data controller pode ajustar o nível de risco desde que devidamente justificado. Este caso pode acontecer por caracteristicas especiais do processamento de dados e do seu contexto.

## Medidas de Segurança

As medidas de segurança propostas dependem dos níveis de risco associado ao use case. Estas podem ser primeramente divididas em duas categórias: medidas técnicas, medidas Orgazacionais. Dentro destas ainda podem ser dividas em quatro subcategorias e como divisão final pelo nivel de risco que propõem solucionar.

## Avaliação de Empregados

No documento faz-se uma analise da avaliação anual de empregados. Estes são avaliados segundos medidas predefinadas e acordadas com entre o empregador e o empregado. Estes dados são processados por um officer dos recursos humanos através de documentação em papel como eletronica. O report é discutido com o empregado e a versão final assinada e submetida eletronicamente nos recursos humanos junto com as conclusões do report.

No texto apresentado mais a imagem presente no documento na seção 3.3.1 define-se o contexto e o processo para avaliação de empregados. Note-se que na imagem ainda diz adicionalmente a informação realmente processada (Primeiro e ultimo nome, data de inicio de contrato, skills técnicas, conhecimento, avaliação do trabalho,etc.). Esta tabela/imagem é uma forma sucinta de apresentar as respostas as perguntas definidas na metodologia para esta fase

A avaliação do impacto pode ser feita como é dito na metodologia avaliando três fatores:

- Perda da confidencialidade - Diversas informações são processadas pelas avaliações relativas a qualidade/quantidade de trabalho. Algumas informações sensiveis podem surgir no meio do processo. E, ainda segundo o documento, a perda da confidencialidade destas informações pode causar algum desconforto para o empregado. Classificando-o como Medium.

- Perda da Integridade - A perda desta propriedade pode ser considera Medium já que podem ocorrer inconvenientes das avaliações serem modificadas para bem ou para mal.

- Perda da Disponibilidade - A perda de disponibilidade não resulta em muitos problemas por isso pode ser considerada Low.

O impacto pode ser classificado como o maior das classificações, ou seja, Medium. Ainda alguns casos pode ser classificados como niveis mais altos.

No que diz respeito, a probabilidade de ocorrência de ameaças cada dimensão pode classificada da seguinte forma:

- Recursos técnicos e Rede - O sistema não está conetado a internet e não pode ser acedido pela rede o que implica que deve ser considerado Low.

- Processos/Procedimentos relacionados com o processamento de dados pessoais - Classificado como Medium visto que a politica de uso não está devidamente definida e a informação não esta limitada as zonas da organização.

- Grupos de pessoas como individuos envolvidos no processamento de dados - A probabilidade de ocorrência de ameaça é Medium e é assumido que não existem politicas para armazenamento e deletion dos dados.

- Setor de negócio e escala de processamento - Classificado como Low já que este não é considerado um setor que seja propenso a cyber attacks.

Sumando essas classificações dá um valor total de 6 classificando-o como Medium.

Finalmente falta avaliar o risco que vendo a tabela sugerida pelo documento pode ser considerado também como Medium. 

As medidas de segurança que podem sugeridas são:

- Physical Security -  T.2 - Através de identificação de forma a controlar as entradas e saidas da organização impedindo que os documentos sejam acedidos por individuos não autorizados.

- Data Deletion/Disposal - S.3 - Utilizando esta medida impede-se que as avaliações sejam apagadas sem autorização.

- Data processors - F.5 - Os empregados dos recursos humanos que processam avaliação pessoal devem ser sujeitos a agreements para non-disclosure.


