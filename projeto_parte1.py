def cria_link(busca, ord_data, lingua = '', periodo = '', minimo = '', maximo = ''):
	url = 'https://www.google.com/search?q={}&tbm=nws'.format(busca)
	if lingua != '':	
		url += '&lr=lang_{}'.format(lingua)

	if periodo != '' or ord_data == True:
		url += '&tbs='
		if ord_data == True:
			url += 'sbd:1,'
		if periodo != '':
			if periodo == 'hora':
				url += 'qdr:h'
			elif periodo == 'dia':
				url += 'qdr:d'
			elif periodo == 'semana':
				url += 'qdr:w'
			elif periodo == 'mês':
				url += 'qdr:m'
			elif periodo == 'ano':
				url += 'qdr:y'
			else:
				url += 'dqr:1'
				if minimo != '':
					url += ',cd_min:{}'.format(minimo)
				if maximo != '':
					url += ',cd_max:{}'.format(maximo)
	return url

link = cria_link('Trump', False, 'ch', 'dia')
print(link)