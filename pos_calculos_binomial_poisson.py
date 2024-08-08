import numpy as np
from scipy.stats import binom, poisson, expon

#EXERCÍCIOS     -     B I N O M I A L
#Uma caixa com 12 ovos é selecionada aleatoriamente da gôndola de um supermercado.
x= 2
n= 12
p= 0.05


# A ) Qual a probabilidade de que essa caixa de ovos possua 2 unidades quebradas?
#Distribuição Binomial para o cálculo de
# P(X = x)
alt_a = binom.pmf(x,n,p)
alt_a = alt_a*100
print(f"A) A probabilidade é {alt_a:.2f} %")


# B ) Qual a probabilidade que essa caixa de ovos possua no máximo 2 unidades quebradas?
#Distribuição Binomial para o cálculo de
# P(0 <= X <= x) = P(X <= x)
alt_b = binom.cdf(x,n,p)
alt_b = alt_b*100
print(f"B) A probabilidade é {alt_b:.2f} %")


# C ) Qual a probabilidade que essa caixa de ovos possua no mais de 2 unidades quebradas?
#Distribuição Binomial para o cálculo de
# P(X > x)
alt_c = binom.sf(x,n,p)
alt_c = alt_c*100
print(f"C) A probabilidade é {alt_c:.2f} % \n")










#EXERCÍCIOS     -     P O I S S O N
#Um banco realizou uma coleta de dados, e a partir daí percebeu-se 
#que em um período de uma hora 6 clientes adquirem certo seguro.

x1 = 6
periodo = 1
media = x1/periodo

# A ) A instituição deseja saber qual a probabilidade, no mesmo período de tempo, pelo menos 8 seguros serem vendidos?
#Distribuição Poisson para o cálculo de
# P(X > 7)
x=7 #(como no poisson não há o cálculo de maior ou igual a 8, nesse caso, usamos o cálculo de maior que x, nesse caso será atribuído o valor 7)
a = poisson.sf(x,media)
a = a*100
print(f"A) A probabilidade poisson é {a:.4f} %")


# B ) A instituição deseja saber qual a probabilidade de, no mesmo período, menos de 8 seguros serem vendidos?
#Distribuição Poisson para o cálculo de
# P( X < 8) = P(X <= 7)
x=7 #(como no poisson não há o cálculo de maior ou igual a 8, nesse caso, usamos o cálculo de maior que x, nesse caso será atribuído o valor 7)
b = poisson.cdf(x,media)
b = b*100
print(f"B) A probabilidade poisson é {b:.4f} %")

# C ) A instituição deseja saber qual a probabilidade de, no período de 4 horas, 18 seguros serem vendidos??
#Distribuição Poisson para o cálculo de
# P(X = 18)
z = 18 #nova quantidade de seguros
media_4hrs = media * 4 # média por hora vezes 4
c = poisson.pmf(z,media_4hrs)
c = c*100
print(f"C) A probabilidade poisson é {c:.4f} % \n")










#EXERCÍCIOS     -     E X P O N E N C I A L
#O tempo de espera em uma fila para realizar o pagamento dos produtos 
#adquiridos na loja segue uma distribuição exponencial com parâmetro 1/5 minutos    

# A) Qual a probabilidade de que uma pessoa espere um tempo menor do que a média?
g = 5
h = 0.2
a1 = expon.cdf(g,h)
a1 = a1*100
print(f"A) A probabilidade EXPONENCIAL é {a1:.4f} %")


# B)  Qual a probabilidade de que uma pessoa espere entre 4 e 6  minutos na fila até o atendimento?
h = 500
i= 1000
j= 300
b1 = (expon.cdf(i,h)) - (expon.cdf(j,h))
b1= b1*100
print(f" PROVA B) A probabilidade EXPONENCIAL é {b1:.4f} % \n")



#EXERCÍCIO 2
#Suponha que o tempo de vida de um celular seja modelado pela distribuição exponencial apresentando uma média de 2 anos
# A) Calcule a probabilidade do aparelho durar menos que o tempo de cobertura da garantia 
# estabelecida pela fábrica que é de 01 ano?
# P(X<1)
k=1
l=0.5
a2 = expon.cdf(k,l)
print(f"2A) A probabilidade EXPONENCIAL é {a2:.4f} %")




# B) Sabendo que a garantia aabou de vencer sem que o aparelho apresentasse problema,
#  calcule a probabilidade do aparelho durar pelo menos mais 1 ano
# P(X>1)
m=1
n=0.5
b2 = expon.sf(m,n)
print(f"2B) A probabilidade EXPONENCIAL é {b2:.4f} %")