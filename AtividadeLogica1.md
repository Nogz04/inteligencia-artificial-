# Modelar os problemas

## 1 - Problema dos Missionários e Canibais

Há 3 missionários e 3 canibais. Há também um barco que vai da margem 
esquerda para a margem direita e vice-versa, sempre levando um ou duas
pessoas. Todas as pessoas estão na margem esquerda e precisam ir para a margem direita.
Porém, há restrições: em momento algum pode ficar mais canibais do que missionários
em uma das margens.

<br> 

![image](https://github.com/user-attachments/assets/f9ce4f7d-0e41-4f32-9310-032547897848)



<h2>Resolução</h2>

**C = Canibais** <br>
**M = Missionários**

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
   > - FIM. ✔️
  
<br> 

## 2- Problema da travesia da ponte

Há 4 pessoas: cientista, zelador, professora e aluno. Que precisam passar pela ponte.

Cada um tem um tempo de travessia:
  - aluno: leva 1 minuto para cruzar a ponte
  - professora: leva 2 minutos
  - zelador: 5 minutos
  - cientista: 10 minutos

O problema é qual a sequência de travessia para que o tempo total seja no máximo de 17 minutos.

Contudo, para cruzar a ponte é preciso usar uma lanterna e no máximo duas pessoas podem cruzar a ponte. Qualquer pessoa cruzando a ponte precisa segurar a lanterna.

<h2>Resolução</h2>

1. **Aluno e Professora atravessam juntos** → (2 minutos)
     > - **Lado Inicial:** Zelador, Cientista
     > - **Lado Final:** Aluno, Professora
     > - **Lanterna:** Lado Final

2. **Aluno retorna com a lanterna** → (1 minuto)
     > - **Lado Inicial:** Zelador, Cientista, Aluno
     > - **Lado Final:** Professora
     > - **Lanterna:** Lado Inicial

3. **Cientista e Zelador atravessam juntos** → (10 minutos)
     > - **Lado Inicial:** Aluno
     > - **Lado Final:** Professora, Zelador, Cientista
     > - **Lanterna:** Lado Final

4. **Professora retorna com a lanterna** → (2 minutos)
     > - **Lado Inicial:** Aluno, Professora
     > - **Lado Final:** Zelador, Cientista
     > - **Lanterna:** Lado Inicial

5. **Aluno e Professora atravessam juntos novamente** → (2 minutos)
     > - **Lado Inicial:** (vazio)
     > - **Lado Final:** Aluno, Professora, Zelador, Cientista
     > - FIM. ✔️
     
     
   





   
  
