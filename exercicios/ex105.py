def notas(* notas, sit=False):
	"""
	=> Função para analisar notas e situações de vários alunos.
	:param notas: uma ou mais notas dos alunos (aceita várias).
	:param sit: valor opcional, indicando se deve ou não adicionar a situação.
	:return: dicionário com várias informações sobre a situação da turma.
	"""
	info = {}
	info['quantidade'] = len(notas)
	info['maior'] = max(notas)
	info['menor'] = min(notas)
	info['média'] = sum(notas) / info['quantidade']
	if sit:
		if info['média'] >= 7:
			info['situação'] = 'BOA'
		elif info['média'] >= 5:
			info['situação'] = 'RAZOÁVEL'
		else:
			info['situação'] = 'RUIM'
	return info
	

#Programa Principal	
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)
