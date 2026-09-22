largura = float(input("Qual a largura da parede? "))
altura = float(input("Qual a altura da parede? "))
area = largura * altura
print(f'Sua parede tem a dimensão de:', largura, 'x' , altura,  'e uma área de:' ,area, 'm²')


quantidadedetinta = area / 2

print(f'A quantidade de tinta necessária é de' , quantidadedetinta, 'litros')
