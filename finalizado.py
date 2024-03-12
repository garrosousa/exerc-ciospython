#exercicio1 "área e perímetro de um triangulo"

x1 = (int(input("primeiro:")))

x2= (int(input("segundo:")))

area = x1 * x2

perímetro = 2 * (x1 + x2)

print("a área é", area)

print("o perímetro é", perímetro)



#exercicio2 "somar comissão"

salAtual=(float(input ("seu salário=")

salComissão = (salAtual/100) * 5

print ("sua comissão é", salComissão )

print ("assim ficando",salComissão+salAtual )



#exercicio3 "calculo velocidade média"

distancia= int(input("distancia="))

tempo= int(input("tempo="))

print("velocidade média=", distancia/tempo)



#exercicio4 "bhaskara"

a=int(input("valor de a="))

b=int(input("valor de b="))

c=int(input("valor de c="))

delta=b**2-4*a*c

x1=((-b)+delta**(1/2))/(2*a)

x2=((-b)-delta**(1/2))/(2*a)

print(x1)

print(x2)



#exercicio5 "conversão do dólar para o real"

dolar=int(input("dólar americano:"))

real=(dolar*(49824/10000))

print("U$",dolar,"equivale a R$",real)



#exercicio6 "porcentagem do garçom"

valorGasto=int(input("gastou R$"))

porcentagemGarçom=(valorGasto/100)

valorTotal=(valorGasto+(porcentagemGarçom*10))

print("valor total= R$",valorTotal)



#exercicio7 "temperatura em celsius, fahrenheit e kelvin"

tc=int(input("temperatura em graus celsius= "))

tf=(18/10)*tc+32

tk=tc+273

print(tc,"Celsius,",tf,"Fahrenheit,",tk,"Kelvin.")
