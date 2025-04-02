# Algoritmos Genéticos (AGs)

## 📌 O que são?
Algoritmos Genéticos são métodos de **otimização e busca** inspirados na **evolução natural** (seleção, mutação e crossover). Simulam a "sobrevivência do mais apto" para encontrar soluções em problemas complexos.

---

## 🎯 Para que servem?
Resolvem problemas onde:
- Espaço de busca é **grande/não linear**.
- Métodos tradicionais (como gradientes) falham.
- Soluções são **combinatórias** ou **não diferenciáveis**.

---

## 🔍 Tipos de Problemas que Resolvem
1. **Projetar coisas**: Aviões, prédios, chips eletrônicos.  
2. **Otimizar rotas**: Entregas, tráfego, logística.  
3. **Criar arte**: Música, pinturas, designs únicos.  
4. **Jogos**: Achar a melhor estratégia automaticamente.    

---

## � Aplicações Práticas
- **Logística**: Rotas de entrega (UPS, Amazon).  
- **Robótica**: Controle de movimentos.  
- **Finanças**: Otimização de carteiras.  
- **Saúde**: Planejamento de radioterapia.  
- **Arte**: Design generativo/música algorítmica.  

---

## ✅ Vantagens
- Não requer derivadas.  
- Foge de mínimos locais.  
- Paralelizável.  

## ❌ Limitações
- Custo computacional alto.  
- Não garante ótimo global.  

<h1>Explicação mais didática:</h1>

## 🔍 **Como Funciona? (Passo a Passo Simples)**  

1. **População Inicial (Bichos Virtuais)**  
   - Cria-se um monte de "indivíduos" (soluções aleatórias). Ex: 100 robôs com formas diferentes.  

2. **Avaliação (Quem é o Melhor?)**  
   - Cada robô é testado (ex: anda 10m). Quem anda mais longe ganha uma **nota alta (fitness)**.  

3. **Seleção (Os Mais Fortes Sobrevivem)**  
   - Só os melhores robôs (20% com maior nota) podem "ter filhos".  

4. **Crossover (Misturinha Genética)**  
   - Dois robôs bons trocam partes (ex: pernas de um + braços de outro) para gerar **filhos melhores**.  

5. **Mutação (Um Toque de Sorte)**  
   - Alguns filhos ganham mudanças aleatórias (ex: perna mais longa). Isso evita soluções repetidas!  

6. **Nova Geração (Repete Tudo!)**  
   - Os filhos substituem os pais ruins, e o ciclo recomeça. Depois de 100 gerações... **nasce um robô incrível!**  

---

## 🧩 **Peças do Quebra-Cabeça (Termos Técnicos Simples)**  

| **Termo**          | **Significado**                               |         **Exemplo**              |  
|--------------------|-----------------------------------------------|----------------------------------|  
| **Indivíduo**      | Uma solução candidata (um "bicho virtual").   | Um robô com pernas curtas.       |  
| **Fitness**        | Nota que diz quão bom o indivíduo é.          | Robô andou 5m → Fitness = 5.     |  
| **Seleção**        | Escolher os melhores para reproduzir.         | Top 10% dos robôs.              |  
| **Crossover**      | Misturar partes de dois bons indivíduos.      | Perna do Pai + Braço da Mãe.     |  
| **Mutação**        | Mudança aleatória para inovar.                | Perda aleatoriamente mais longa. |  

---

## 🌟 **Exemplo Real: Otimizando um Avião**  
1. **População Inicial**: 100 modelos de asas (gerados aleatoriamente).  
2. **Fitness**: Quanto menos combustível o avião gastar, melhor.  
3. **Seleção + Crossover**: As melhores asas são combinadas.  
4. **Mutação**: Algumas ganham formatos inusitados.  
5. **Resultado**: Depois de 500 gerações, nasce a **asa perfeita**!  

---

## ❓ **Dúvidas**   

### 1. **É Igual a IA Normal?**  
   - Não! IA tradicional "aprende", AGs "evoluem" por tentativa e erro.  

---
