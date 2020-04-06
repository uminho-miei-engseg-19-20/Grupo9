# Pergunta 1.1

## Rank 1 -  CWE-119 - Improper Restriction of Operations within the Bound of a Memory Buffer

O software executa operações num buffer de memória mas existe a possibilidade de ler ou escrever fora dos limites definidos para o mesmo.

Por exemplo, existem linguagens de programação que permitem aceder a endereços de memória que estão fora do buffer mas que podem estar associados com outras estruturas, variaveis ou mesmo parte do programa.

Um atacante poderia alterar endereços de memória a partir de um buffer para executar código a sua escolha ou ainda alterar valores relativos a segurança da própria aplicação.

Este tipo de Problemas pode ser introduzidos tanto na fase de Design e Arquitetura como na fase de implementação. As linguagens de programação que costumam ter este tipo de Weakness são as de nivel baixo, isto é, C C++ e Assembly.

As consequências mais comuns deste tipo de Weakness são as seguintes:

- Compromete: Confidencialidade Integridade Disponibilidade - Caso o atacante tenha acesso a function pointer pode redirecionar o programa  para o código que este pretender executar. Ainda pode alterar valores que dizem respeito a segurança como a flag que diga se o utilizador logado é administrador.

- Compromete: Confidencialidade Disponibilidade - Acesso a memória fora dos limites pode causar corrupção do programa causando em Crash ou num loop infinito.

- Compromete: Confidencialidade - No caso de uma leitura fora do limites de memória pretendidos pode permitir acesso a memória confidencial do sistema ou do utilizador. Alguma dessa informação pode servir para permitir futuros ataques ao sistema caso esta revele detalhes do sistema.

## Rank 2 - CWE-79 - Improper Neutralization of Input During Web Page Generation (XSS)

O input que pode ser controlado pelo utilizador não é corretamente neutralizado antes de ser posto como web page para outros utilizadores.

Existem várias ocasiões onde podem ocorrer este tipo de vulnerabilidade:

- Untrusted data entrar para uma aplicação web

- Web application gera dinamicamente web page com unstrusted data

- Script vem da pagina web em si, quando chega ao browser é executado no contexto do dominio do web server.

- Ainda há mais exemplos contidos na pagina do CWE.

Estes ataques de XSS podem ser classificados como:

- Type 1: Reflected XSS - O servidro lê dados diretamente do request do atacante e reflete uma resposta como tal. Obrigando o utilzador a visitar ou clicar num URL que tenha o conteudo malicioso no mesmo para fornece-lo a um aplicação web vulneravel.

- Type 2: Stored XSS - Dados "perigosos" são guardados na base de dados da aplicação permitindo, mais tarde, serem lidos de volta para a aplicação. Normalmente, estes são direcionados para utilizadores com privelegios maiores sobre a aplicação como administradores. Por exemplo, para executar comandos ao nivel do administrador ou aceder a dados confidenciais.

- Type 0: DOM-Based XSS - Neste tipo de ataque de XSS a injeção de código é feita pelo cliente invés do servidor. Por exemplo, o utilizador poderia inserir certos parametros no Script que o server enviou para a página, de forma, a conseguir alguns resultados pretendidos.

Depois de o ataque ter sucesso existem muitos tipos de atividades possíveis pelo atacante. Entre estas encontra-se roubo de informação pessoal, ganhar privelegios de administrador. Neste tipo de ataques também encontram-se os Phishing Attacks que tomam várias formas em que uma delas seria emular um site de confiança para enganar o utilizador a inserir a sua password.

Este tipo de ataques é independente do tipo de linguagens de programação utilizado sendo mais prevalente em tecnologias que são Web based. Para além dos possiveis ataques já mencionados acima ainda:

- Compromete: Integridade Confidencialidade Disponibilidade - Existe a possibilidade de executar código pretendido pelo atacante.

- Compromete: Controlo de Acesso Confidencialidade - A partir de um script criado pelo Cliente ter acesso a informação que náo deveria ser possível ser acedida por esse utilizador. Por exemplo, enviar para o e-mail todos os Cookies do website.

## Rank 3 - CWE-20 - Improper Input Validation

O input enviado pelo utilizador para o software não é corretamente validado podendo alterar o flow do programa, executar código injetado pelo utilizador, acesso a recursos de outra forma protegidos.

Esta Weakness pode ser introduzida na dase de Architecture and Design em que não se teve em conta que era necessário realizar a devida validação do input e na Implementação do mesmo. Caso o programador assuma premissas erradas enquanto o que o atacante pode fazer. Qualquer platforma e qualquer software criado com diferentes linguagens de programação pode ser afetado por esta vulnerabilidade visto que depende da própria implementação e não da tecnologia usada.

Algumas consequências deste tipo de ataque:

- Compromete: Disponibilidade - O atacante pode prover valores não esperados pela aplicação causando um crash ou consumo excessivo de recursos

- Compromete: Confidencialidade - O atacante poderia ter acesso a informação confidencial do sisteme ou de outros utilizadores.

- Compromete : Confidencialidade Integridade Disponibilidade -  O atacante através de certo input poderia alterar o flow do programa "saltando" alguns aspetos de segurança ou para executar código pretendido para seu beneficio.

## Rank 12 ( Grupo 9 + 3) - CWE-787 - Out-of-bounds Write

Esta Weakness refere-se a escrita de dados depois do fim ou antes do inicio do buffer em questão. Resulta em corrupção de dados, crash ou execução de código.

Este tipo de Weakness é mais comum em linguagens de baixo nivel como C, C++ e Assembly visto que estas não tem na própria linguagens mecanismos para fazer check ou levantar excepções nestes casos. E, como já foi indicado acima algumas das consequências possiveis são:

- Compromete: Integridade Disponibilidade - DoS, Crash, Restart, execução de código escolhido pelo atacante.

O exemplo de código demonstra um caso onde esta vulnerabilidade acontece. O código aloca um buffer de 64 para guardar o nome do Hostname que corresponde a determindao address IP. No entanto não sabe ao certo o tamanho do mesmo podendo ser maior que 64 bytes podendo apagar informação que esteja a seguir do buffer ou de alguma forma o atacante alterar os endereços de memorias seguintes para alterar o fluxo do programa.

```
void host_lookup(char *user_supplied_addr)
{
	struct hostent *hp;
	in_addr_t *addr;
	char hostname[64];
	in_addr_t inet_addr(const char *cp);

	/*routine that ensures user_supplied_addr is in the right format for conversion */

	validate_addr_form(user_supplied_addr);
	addr = inet_addr(user_supplied_addr);
	hp = gethostbyaddr( addr, sizeof(struct in_addr), AF_INET);
	strcpy(hostname, hp->h_name);
}
```

A vulnerabilidade indicada nesta seção ja foi encontrada e registada num produto no CVE-2019-8001. As versões 19.1.8 e anteriores como as versões 20.0.5 e anteriores do Adobe Photoshop CC tem esta weakness (Se explorada levando a execução arbitraria de código). Segundo o site cvedetails.com com Score 10 (CVSS) afetando as três principais propriedades de segurança CIA, com uma complexidade de acesso baixa e não requerendo autentificação.

Nota: Foi confirmada pela pŕopria adobe - https://helpx.adobe.com/security/products/photoshop/apsb19-44.html

# Pergunta 1.2


 


