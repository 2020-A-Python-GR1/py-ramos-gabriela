Srapy
Scrapy instalacion
Ejecutar dentro del Anaconda prompt.

$ pip install scrapy
Comandos generales
Da las caracteristicas para poder hacer Web Scraping o Web Crawling de ese computador

$ scrapy bench
Visualizar las configuraciones extra

$ scrapy settings
Visualizamos la version de Scrapy

$ scrapy version
scrapy view url
Visualizar el contenido como lo ve el Scrapy

Si se ve el contenido

$ scrapy view https://www.pluralsight.com/authors
No se ve el contenido

$ scrapy view https://srienlinea.sri.gob.ec/sri-en-linea/inicio/NAT
scrapy shell url
Permite interactuar con la respuesta del scrapy mediante un shell

$ scrapy shell http://quotes.toscrape.com/
$ response.css('title')
$ response.css('title').extract()
$ response.css('title::text').extract()
$ response.css('.author').extract()
$ response.css('.author::text').extract()
$ type(response.css('.author::text'))
$ type(response.css('.author::text')[0])
$ response.css('.author').extract_first()
$ response.css('a::attr(href)').extract_first()
$ response.css('.row > div > div:nth-child(2) > .text::text').extract()

$ response.xpath('/html/head/title').extract()
$ response.xpath('//title').extract()
$ response.xpath('/html/body/div/div[2]/div[2]/h2').extract()
$ response.xpath('/html/body/div/div[2]/div[2]/h2').extract()
$ response.xpath("//div[@class='quote']/span[@class='text']").extract_first()
$ response.xpath("//div[@class='quote']/span[@class='text']/text()").extract_first()
$ //div[@class='quote']/span/a/@href").extract_first()

scrapy startproject nombre_proyecto
$ scrapy startproject arania_basica

correr arania 
# scrapy crawl nombre_arania


>>> response .xpath('/html/body/title').extract()
[]
>>> response .xpath('/html/head/title').extract()
['<title>Quotes to Scrape</title>']
>>> response .xpath('/html/head/title').extract()
['<title>Quotes to Scrape</title>']
>>> response .xpath('/html/head/title/text()').extract()

BUSCAR TODAS LAS OCURREARNCIAS DE LA ETIQUETA ( QUE TENGA TITLE)

>>> response .xpath('//title/text()').extract()
['Quotes to Scrape']


ACCEDER A CLASES QUE TENGAN UN NOMBRE (DIV[TAG] la clase se llamada tag)

response .xpath("//div[@class='tag']/text()").extract()
[]

PERO SOLO HAY ANCORES

>>> response .xpath("//a[@class='tag']/text()").extract()
['change', 'deep-thoughts', 'thinking', 'world', 'abilities', 'choices', 'inspirational', 'life', 'live', 'miracle', 'miracles', 'aliteracy', 'books', 'classic', 'humor', 'be-yourself', 'inspirational', 'adulthood', 'success', 'value', 'life', 'love', 'edison', 'failure', 'inspirational', 'paraphrased', 'misattributed-eleanor-roosevelt', 'humor', 'obvious', 'simile', 'love', 'inspirational', 'life', 'humor', 'books', 'reading', 'friendship', 'friends', 'truth', 'simile']
>>>


LINKS PARA VISITAR AUTORES CON CSS
response.css('div.quote span a::attr(href)').extract()


CON XPATH
response.xpath("//div[@class='quote']/span/a/@href").extract()

