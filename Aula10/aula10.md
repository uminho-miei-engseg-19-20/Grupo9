## P1.1

### 1

 Caso os valores sejam demasiado pequenos ou demasiado grandes, podem levar a quebra de segurança. Como x e y são d tipo size_t (unsigned int) caso o valor passado seja demasiado grande podemos obter integer overflow. Isto pode permitir a escrita em zonas de memória não alocadas para o efeito. 


### 2

```C
int main() {
    char* qualquercoisa;
    vulneravel(qualquercoisa, 11111111111111, 11111111111111, 0);

}

```

### 3

  Obteremos um segmentation Fault a dizer que a alocação nessa zona de memória  não é permitida.


## P1.2

### 1

	
  Esta vúlnerabilidade é de integer underflow. Significa que existe perigo por o inteiro ser ter um valor mais baixo do que o permitido.
  Por exemplo se definirmos o valor como 0 então o tamanho_real terá valor negativo. Como o tipo size_t não representa valores negativos temos a falha. 
  
  
### 2

```C
int main(){
    char* falha = “vamos rebentar\n”;
    vulneravel(falha,0);  
}
```


### 3

  O erro é: Segmentation Fault.


### 4
 As mudanças feitas ao código são:  
 
 - Adicionar a definição: const int MIN_SIZE = 0;  

 -Adicionar a seguinte condição ao if na função vulneravel(): tamanho > MIN_SIZE 
