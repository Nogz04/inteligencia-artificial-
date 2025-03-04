# Modelar os problemas

## Problema dos Missionários e Canibais

Há 3 missionários e 3 canibais. Há também um barco que vai da margem 
esquerda para a margem direita e vice-versa, sempre levando um ou duas
pessoas. Todas as pessoas estão na margem esquerda e precisam ir para a margem direita.
Porém, há restrições: em momento algum pode ficar mais canibais do que missionários
em uma das margens.

<h1>Resolução</h1>

C = Canibais <br>
M = Missionários

1. **(2 pessoas vão para a direita)** → 2 canibais atravessam.
   > - **Margem Esquerda:** 3M, 1C
   > - **Margem Direita:** 2C
   > - **Barco:** Volta com 1 canibal

2. **(1 pessoa volta para a esquerda)** → 1 canibal retorna.
   > - **Margem Esquerda:** 3M, 2C
   > - **Margem Direita:** 1C
   > - **Barco:** Vazio

3. **(2 pessoas vão para a direita)** → 2 canibais atravessam.
   > - **Margem Esquerda:** 3M
   > - **Margem Direita:** 3C
   > - **Barco:** Volta com 1 canibal

4. **(1 pessoa volta para a esquerda)** → 1 canibal retorna.
   > - **Margem Esquerda:** 3M, 1C
   > - **Margem Direita:** 2C
   > - **Barco:** Vazio

5. **(2 pessoas vão para a direita)** → 2 missionários atravessam.
   > - **Margem Esquerda:** 1M, 1C
   > - **Margem Direita:** 2M, 2C
   > - **Barco:** Volta com 1 canibal e 1 missionário

6. **(2 pessoas voltam para a esquerda)** → 1 missionário e 1 canibal retornam.
   > - **Margem Esquerda:** 2M, 2C
   > - **Margem Direita:** 1M, 1C
   > - **Barco:** Vazio

7. **(2 pessoas vão para a direita)** → 2 missionários atravessam.
   > - **Margem Esquerda:** 0M, 2C
   > - **Margem Direita:** 3M, 1C
   > - **Barco:** Volta com 1 canibal

8. **(1 pessoa volta para a esquerda)** → 1 canibal retorna.
   > - **Margem Esquerda:** 1C
   > - **Margem Direita:** 3M, 2C
   > - **Barco:** Vazio

9. **(2 pessoas vão para a direita)** → Os 2 canibais atravessam.
   > - **Margem Esquerda:** 0
   > - **Margem Direita:** 3M, 3C


<br><br>**Desenho ilustrativo que fiz para representar graficamente:** <br> <br>
![image](https://github.com/user-attachments/assets/2c008358-75a3-4a29-b893-7f477db9bfc6)







   
  
