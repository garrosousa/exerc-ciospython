#exercicio1
x1 = (int(input("primeiro:")))
x2= (int(input("segundo:")))
area = x1 * x2
perímetro = 2 * (x1 + x2)
print("a área é", area)
print("o perímetro é", perímetro)

#exercicio2
salAtual=float(input("digite seu salario="))
salComissão = (salAtual/100) * 5
print("sua comissão é", salComissão)
print("assim ficando", salComissão + salAtual)

#exercicio3
distancia= int(input("distancia="))
tempo= int(input("tempo="))
print("velocidade média=", distancia/tempo)

#exercicio4
a= float(input("valor de a="))
b= float(input("valor de b="))
c= float(input("valor de c="))
delta = b**2 - 4*a*c
x1 = (-b-(delta**0.5)/(2*a))
x2 = (-b+(delta**0.5)/(2*a))
