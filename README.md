# TDE_Ciber
Trabalho final de Performance em Sistemas Ciberfísicos 
## 📜 Descrição do Trabalho
- Não vamos pensar em implementação da memória principal (apenas usá-la)
- Nos preocuparemos com o endereçamento na cache – testando endereços na cache a
princípio vazia e somente fazendo as comparações ditadas pelo método estudado.
- Vamos trabalhar com linhas da cache, não importando o tamanho do
bloco.
## 🗺️ Mapeamento direto
- Nesse mapeamento, temos a associação de cada endereço da memória principal
em um correspondente específico na cache.
- Vamos utilizar a operação “mod” ou % que retorna o resto de uma divisão – entre a
posição desejada e o número de linhas.
### Exemplo
`O processador pede a posição 23 e o tamanho da cache são 10 linhas`
- 23 mod 10 = 3 (O endereço 23 da memória principal está mapeado no 3 da cache).
- Prova: 2*10 + 3 , ou seja, cabem 2 inteiros de 10 no número 23 e sobram 3
  
`O processador pede a posição 7 e o tamanho da cache são 10 linhas`
- 7 mod 10 = 7 ( O endereço 7 da memória principal está mapeado no 7 da cache).
- Prova: 7 = 7*0 + 7 (na divisão não temos nenhum inteiro, mas só temos resto, ou
seja, o resultado é 7)
## 🎯 Objetivo
- Queremos analisar o passo-a-passo de acesso no mapeamento direto. Ou seja, enxergar qual posição está sendo disputada
nesse mapeamento e como é realizada a troca.
- Queremos analisar a quantidade de hits (acertos) e misses (falhas) de acordo com as posições
solicitadas pelo processador.
