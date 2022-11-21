from wsgiref import headers
import scrapy
from bs4 import BeautifulSoup
from scrapy.selector import Selector


lista_deputadas = []
class QuotesSpider(scrapy.Spider):
    name = "links_deputados"

    def start_requests(self):
        urls = [
            'https://www.camara.leg.br/deputados/quem-sao/resultado?search=&partido=&uf=&legislatura=56&sexo=M&pagina=1',
            'https://www.camara.leg.br/deputados/quem-sao/resultado?search=&partido=&uf=&legislatura=56&sexo=M&pagina=2',
            'https://www.camara.leg.br/deputados/quem-sao/resultado?search=&partido=&uf=&legislatura=56&sexo=M&pagina=3',
            'https://www.camara.leg.br/deputados/quem-sao/resultado?search=&partido=&uf=&legislatura=56&sexo=M&pagina=4',
            'https://www.camara.leg.br/deputados/quem-sao/resultado?search=&partido=&uf=&legislatura=56&sexo=M&pagina=5',
            'https://www.camara.leg.br/deputados/quem-sao/resultado?search=&partido=&uf=&legislatura=56&sexo=M&pagina=6',
            'https://www.camara.leg.br/deputados/quem-sao/resultado?search=&partido=&uf=&legislatura=56&sexo=M&pagina=7',
            'https://www.camara.leg.br/deputados/quem-sao/resultado?search=&partido=&uf=&legislatura=56&sexo=M&pagina=8'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
       
        filename = f'links_deputados.html'
        dep =  response.css('h3.lista-resultados__cabecalho').getall()
        for i in dep:
            body = i
            aux = Selector(text=body).xpath('//a/@href').get()
            print(aux)
            lista_deputadas.append(aux)
        
        # Salva o html da pagina
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

        # Salva os links em txt
        file=open('lista_deputados.txt','w')
        for items in lista_deputadas:
            file.writelines(items+'\n')

        file.close()