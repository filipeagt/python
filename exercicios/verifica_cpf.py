cpf=list(input("Digite o cpf: "))
print(cpf)

acc1=0
acc2=0

for num in range(9):
	acc1+=int(cpf[num])*(num+1)
for num in range(10):
	acc2+=int(cpf[num])*num

#print(acc1)
#print(acc2)
verifica1=acc1%11
verifica2=acc2%11

if(verifica1==int(cpf[-2]) and verifica2==int(cpf[-1])):
	print("CPF valido!")
else:
	print("CPF INVALIDO!")