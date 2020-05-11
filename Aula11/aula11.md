### Pergunta 1.1

1. Duas das vulnerabilidades existentes no programa **filetype.c** são:
	* A falta de controlo em relação aos tipos de metacaracteres que podem ser aceites, ou seja, um atacante podia recorrer a injeção de separadores de pastas, também conhecido por *path traversal attack*, para obter controlo de leitura e/ou escrita sobre ficheiros arbitrários.

	* A utilização da função *system()*, função esta que permite executar o programa/comando passado como argumento, com as váriavéis de ambiente do processo-pai, permitindo assim a um atacante utiliza-la para correr comandos não autorizados.


2. Para explorar as vulnerabilidades identificadas na linha anterior, tipos de metacaracteres e função *system()*, podiam ser executados os seguintes comandos: 
	* Tipos de metacaracteres - **./filetype nomeFicheiro; comandoAtacante** -> O qual poderia permitir ao atacante utilizar o programa para correr comandos não autorizados.
  	* Função *system()* - **./filetype "/etc/passwd"** -> O qual poderia permitir ao atacante obter acesso às *passwords* do sistema.
     

3. Caso o programa tivesse permissões setuid root todo o sistema ficaria comprometido, pois, isto significaria que qualquer utilizador executaria o programa como se fossem root. Ou seja, executar programas malignos ou visualizar apagar ou encriptar qualquer ficheiro passaria a ser possível, comprometendo desta forma a integridade, confidencialidade e disponibilidade do sistema.


### Pergunta 1.2

Resolução da pergunta 1.2 encontra-se em [aula11.py](https://github.com/uminho-miei-engseg-19-20/Grupo9/blob/master/Aula11/aula11.py).
