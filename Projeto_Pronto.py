
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

def cria_relatorio(link):
	#baixar chromedriver para windows
	#extrair chromedriver.exe para Área de Trabalho
	#instalar o selenium com o pip:
	#	pip install selenium
	from selenium import webdriver

	driver = webdriver.Chrome()
	driver.get(link)

	from bs4 import BeautifulSoup

	soup = BeautifulSoup(driver.page_source, 'html.parser')
	driver.quit()

	blocos = soup.find_all('div', class_ = 'g')

	relatorio = ''
	for bloco in blocos:
		noticias = bloco.find_all('a', class_ = 'lLrAF') + bloco.find_all('a', class_ = 'RTNUJf')
		fontes = bloco.find_all('span', class_ = 'xQ82C')
		# print(noticia)
		# link = noticias['href']
		links = list(map(lambda noticia: noticia['href'], noticias))
		titles = list(map(lambda noticia: noticia.get_text(), noticias))
		sources = list(map(lambda fonte: fonte.get_text(), fontes))
		for i in range(len(links)):
			# print(links[i])
			# print(titles[i])
			# print(sources[i])
			# print()
			relatorio += "{}\n{}\n{}\n\n".format(links[i], titles[i], sources[i])
		# print('-'*50)
		relatorio += ('-'*50) + '\n'
	print(relatorio)
	return relatorio

def email(texto):
	import smtplib
	import getpass

	my_email = 'flavio.moraes.lc@gmail.com'
	password = getpass.getpass('digite sua senha: ')
	# password = senha
	destinatario = 'ffllaa@gmail.com'
	assunto = 'Noticias Diarias'

	msg = 'Subject: {}\n\n{}'.format(assunto,texto)

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.connect('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(my_email,password)
	server.sendmail(my_email,destinatario,msg.encode('utf-8'))
	server.quit()


link = cria_link('Bolsonaro', False, 'pt', 'dia')
relatorio = cria_relatorio(link)


email(relatorio)
