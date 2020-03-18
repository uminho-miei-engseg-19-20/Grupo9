### Exercício 1 - Assinaturas cegas (Blind signatures) baseadas no Elliptic Curve Discrete Logarithm Problem (ECDLP)

#### Experiência 1.1

* **openssl ecparam -name prime256v1 -genkey -noout -out key.pem**
![image1](Prints/key_pem.png)

* **openssl req -key key.pem -new -x509 -days 365 -out key.crt**
![image2](Prints/key_cert.png)



#### Experiência 1.2

* **Inicialização** - openssl ecparam -name prime256v1 -genkey -noout -out key.pem
![image3](Prints/initSigner-app.png)

* **Ofuscação** - openssl ecparam -name prime256v1 -genkey -noout -out key.pem
![image4](Prints/generateBlindData-app.png)

* **Assinatura** - openssl ecparam -name prime256v1 -genkey -noout -out key.pem
![image5](Prints/generateBlindSignature-app.png)

* **Desofuscação**- openssl ecparam -name prime256v1 -genkey -noout -out key.pem
![image6](Prints/unblindSignature-app.png)

* **Verificação** - openssl ecparam -name prime256v1 -genkey -noout -out key.pem
![image7](Prints/verifySigature-app.png)



### Pergunta 1.1

Assinante:

* [init-app.py](https://github.com/uminho-miei-engseg-19-20/Grupo9/blob/master/Aula3/questao1/P1.1/init-app.py)

* [blindSignature-app.py](https://github.com/uminho-miei-engseg-19-20/Grupo9/blob/master/Aula3/questao1/P1.1/blindSignature-app.py)


Requerente:

* [ofusca-app.py](https://github.com/uminho-miei-engseg-19-20/Grupo9/blob/master/Aula3/questao1/P1.1/ofusca-app.py)

* [desofusca-app.py](https://github.com/uminho-miei-engseg-19-20/Grupo9/blob/master/Aula3/questao1/P1.1/desofusca-app.py)


Verificador:

* [verify-app.py](https://github.com/uminho-miei-engseg-19-20/Grupo9/blob/master/Aula3/questao1/P1.1/verify-app.py)


