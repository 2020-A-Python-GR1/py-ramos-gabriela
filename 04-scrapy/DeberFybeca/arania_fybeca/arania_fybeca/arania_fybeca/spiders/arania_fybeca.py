import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
#sacar los titulos de todos los productos del BELLEZA
# CUANTO ME AHORRO SI SOY AFILIADO O NO 
#https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=446&s=0&pp=25
class AraniaFybeca(CrawlSpider):
    name = 'fybeca' # Heredado

    allowed_domains = [ # Heredado
        'fybeca.com'
    ]
    start_urls = [
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=446&s=0&pp=2000',
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=537&s=0&pp=2000',
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=627&s=0&pp=2000',
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=558&s=0&pp=2000',
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=489&s=0&pp=2000',
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=562&s=0&pp=2000'
     
    ]   


    regla_uno = (
        Rule(
            LinkExtractor(),
            callback = 'parse_page' # Nombre funcion a ejecutar para parsear 
        ),
        # segundo parametro vacio
    )
    segmentos_url_permitidos = (
        'cat=446&s',
        'cat=537&s',
        'cat=627&s',
        'cat=558&s',
        'cat=489&s',
        'cat=562&s'

    )

    regla_dos = (
        Rule(
            LinkExtractor(
                allow_domains = allowed_domains,
                allow = segmentos_url_permitidos
            ), callback='parse_page'
        ),
        # Parametro Vacio
    )

   
    rules = regla_dos # Heredada

   

    def parse_page(self, response):
        tipo= response.css('div.breadcrumb>a::Text')[1].extract()
        with open('fybeca2.txt', 'a+', encoding = 'utf-8') as archivo:
                   archivo.write("*********************"+tipo+ "*************************" +"\n" )
                   print("*********************"+tipo+ "*************************" +"\n")
        lista_nombres = response.css('div.product-tile-inner> a.name::text').extract()
        normal_price = response.css('div.product-tile-inner> div.detail > div.side > div.price::attr(data-bind)').extract()
        precios_final = [b.replace("text:'$' + (", '').replace(").formatMoney(2, '.', ',')", '') for b in normal_price] 
        afiliado_price = response.css('div.product-tile-inner> div.detail > div.side > div.price-member > div::attr(data-bind)').extract()
        precios_afiliado = [b.replace("text:'$' + (", '').replace(").formatMoney(2, '.', ',')", '') for b in afiliado_price]
       
        for (producto, precio_normal, precio_afiliado) in zip(lista_nombres, precios_final, precios_afiliado):
            #    for precioAf in precios_afiliado:
                 with open('fybeca2.txt', 'a+', encoding = 'utf-8') as archivo:
                   archivo.write(producto + " Precio Normal: " + precio_normal + " Precio Afiliado: "+ precio_afiliado +"\n" )
                    
    

  
   


             #   precio_normal = response.css(  'div.product-tile-inner> div.detail > div.side > div.price::attr(data-bind)').extract()
     #   precio_afiliado = response.css( 'div.product-tile-inner> div.detail > div.side > div.price-member > div::attr(data-bind)').extract()

    #    precio_normal = list(
    #        map(
    #            AraniaFybeca.transform_price,
    #            precio_normal
    #        )
    #    )
       
    #    precio_afiliado = list(
    #        map(
    #            AraniaFybeca.transform_price,
    #            precio_afiliado
    #        )
    #    )
      

    #    normal_price_min = min(precio_normal)
    #    normal_price_max = max(precio_normal)

    #    member_price_min = min(precio_afiliado)
    #    member_price_max = max(precio_afiliado)

    #    sum_normal_price = sum(precio_normal)
    #    sum_member_price = sum(precio_afiliado)

     
    #    print("Menor de precio normal: {0}, Máximo de precio normal: {1}".format(normal_price_min, normal_price_max))
    #    print("Menor de precio miembro: {0}, Máximo de precio miembro: {1}".format(member_price_min, member_price_max))
    #    print("Normal pago: {0}, Si soy miembro pago: {1} y ahorro: {2}\n".format(sum_normal_price.__round__(2), sum_member_price.__round__(2), (sum_normal_price-sum_member_price).__round__(2)))

