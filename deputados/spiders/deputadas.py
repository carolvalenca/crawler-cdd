import scrapy
from scrapy.selector import Selector


class DeputadosSpider(scrapy.Spider):
    name = "deputadas"

    def start_requests(self):
        urls = [
            "https://www.camara.leg.br/deputados/204528",
            "https://www.camara.leg.br/deputados/204545",
            "https://www.camara.leg.br/deputados/74057",
            "https://www.camara.leg.br/deputados/204353",
            "https://www.camara.leg.br/deputados/204400",
            "https://www.camara.leg.br/deputados/73696",
            "https://www.camara.leg.br/deputados/123756",
            "https://www.camara.leg.br/deputados/204509",
            "https://www.camara.leg.br/deputados/73701",
            "https://www.camara.leg.br/deputados/204374",
            "https://www.camara.leg.br/deputados/160589",
            "https://www.camara.leg.br/deputados/213762",
            "https://www.camara.leg.br/deputados/204507",
            "https://www.camara.leg.br/deputados/164360",
            "https://www.camara.leg.br/deputados/204369",
            "https://www.camara.leg.br/deputados/204380",
            "https://www.camara.leg.br/deputados/204462",
            "https://www.camara.leg.br/deputados/178928",
            "https://www.camara.leg.br/deputados/178939",
            "https://www.camara.leg.br/deputados/204459",
            "https://www.camara.leg.br/deputados/81297",
            "https://www.camara.leg.br/deputados/204434",
            "https://www.camara.leg.br/deputados/178994",
            "https://www.camara.leg.br/deputados/204421",
            "https://www.camara.leg.br/deputados/178989",
            "https://www.camara.leg.br/deputados/204525",
            "https://www.camara.leg.br/deputados/178945",
            "https://www.camara.leg.br/deputados/204357",
            "https://www.camara.leg.br/deputados/204535",
            "https://www.camara.leg.br/deputados/178961",
            "https://www.camara.leg.br/deputados/204360",
            "https://www.camara.leg.br/deputados/178946",
            "https://www.camara.leg.br/deputados/204534",
            "https://www.camara.leg.br/deputados/204464",
            "https://www.camara.leg.br/deputados/178901",
            "https://www.camara.leg.br/deputados/204466",
            "https://www.camara.leg.br/deputados/215044",
            "https://www.camara.leg.br/deputados/74784",
            "https://www.camara.leg.br/deputados/178866",
            "https://www.camara.leg.br/deputados/166402",
            "https://www.camara.leg.br/deputados/204458",
            "https://www.camara.leg.br/deputados/204471",
            "https://www.camara.leg.br/deputados/204430",
            "https://www.camara.leg.br/deputados/74398",
            "https://www.camara.leg.br/deputados/204540",
            "https://www.camara.leg.br/deputados/178956",
            "https://www.camara.leg.br/deputados/204428",
            "https://www.camara.leg.br/deputados/204432",
            "https://www.camara.leg.br/deputados/204453",
            "https://www.camara.leg.br/deputados/66179",
            "https://www.camara.leg.br/deputados/205535",
            "https://www.camara.leg.br/deputados/204377",
            "https://www.camara.leg.br/deputados/73943",
            "https://www.camara.leg.br/deputados/204529",
            "https://www.camara.leg.br/deputados/204565",
            "https://www.camara.leg.br/deputados/160639",
            "https://www.camara.leg.br/deputados/160641",
            "https://www.camara.leg.br/deputados/204467",
            "https://www.camara.leg.br/deputados/178925",
            "https://www.camara.leg.br/deputados/74075",
            "https://www.camara.leg.br/deputados/220008",
            "https://www.camara.leg.br/deputados/160575",
            "https://www.camara.leg.br/deputados/204407",
            "https://www.camara.leg.br/deputados/204354",
            "https://www.camara.leg.br/deputados/160598",
            "https://www.camara.leg.br/deputados/178966",
            "https://www.camara.leg.br/deputados/107283",
            "https://www.camara.leg.br/deputados/198197",
            "https://www.camara.leg.br/deputados/67138",
            "https://www.camara.leg.br/deputados/74848",
            "https://www.camara.leg.br/deputados/108338",
            "https://www.camara.leg.br/deputados/178839",
            "https://www.camara.leg.br/deputados/204468",
            "https://www.camara.leg.br/deputados/204546",
            "https://www.camara.leg.br/deputados/160534",
            "https://www.camara.leg.br/deputados/178832",
            "https://www.camara.leg.br/deputados/204375",
            "https://www.camara.leg.br/deputados/139285",
            "https://www.camara.leg.br/deputados/204405",
            "https://www.camara.leg.br/deputados/204410",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        info_dep = response.css('ul.informacoes-deputado li').getall()
        for item in info_dep: 
            body = item
            aux = Selector(text=body).xpath('//span/text()').get()
            if aux == 'Nome Civil:':
                nome = Selector(text=body).xpath('//li/text()').get().strip()
            if aux == 'Data de Nascimento:':
                data_nascimento = Selector(text=body).xpath('//li/text()').get().strip()
        
        print(nome)
        print(data_nascimento)

        presenca = response.css('ul.list-table__content li').getall()
        presencas_plenario = Selector(text=presenca[0]).xpath('//dd/text()').getall()
        presencas_comissoes = Selector(text=presenca[1]).xpath('//dd/text()').getall()

        presencas_plenario_dict = {
            'presenca_plenario': presencas_plenario[0].strip().split(' ')[0],
            'ausencia_justificada_plenario': presencas_plenario[1].strip().split(' ')[0],
            'ausencia_plenario': presencas_plenario[2].strip().split(' ')[0]
        }

        presencas_comissoes_dict = {
            'presenca_comissao': presencas_comissoes[0].strip().split(' ')[0],
            'ausencia_justificada_comissao': presencas_comissoes[1].strip().split(' ')[0],
            'ausencia_comissao': presencas_comissoes[2].strip().split(' ')[0]
        }

        gastos_cota_parlamentar = response.css('table#gastomensalcotaparlamentar tbody tr').getall()
        lista_mes_par = []
        lista_valor_par = []
        for item in gastos_cota_parlamentar:
            body = item
            mes = Selector(text=body).xpath('//td[position()=1]/text()').get().lower()
            valor = Selector(text=body).xpath('//td[position()=2]/text()').get()

            lista_mes_par.append('gasto_' + mes + '_par')
            lista_valor_par.append(valor)
        
        par_dictionary = dict(zip(lista_mes_par, lista_valor_par))

        
        gastos_verba_gabinete = response.css('table#gastomensalverbagabinete tbody tr').getall()
        lista_mes_gab = []
        lista_valor_gab = []
        for item in gastos_verba_gabinete:
            body = item
            mes = Selector(text=body).xpath('//td[position()=1]/text()').get().lower()
            valor = Selector(text=body).xpath('//td[position()=2]/text()').get()

            lista_mes_gab.append('gasto_' + mes + '_gab')
            lista_valor_gab.append(valor)

        gab_dictionary = dict(zip(lista_mes_gab, lista_valor_gab))


        beneficios = response.css('div.beneficio').getall()
        for item in beneficios:
            body = item
            aux = Selector(text=body).xpath('//h3/text()').get().strip()
            print(aux)
            if aux == 'Salário mensal bruto':
                salario_bruto = Selector(text=body).xpath('//a[@class="beneficio__info"]/text()').get().strip().split(' ')
                salario_bruto = salario_bruto[len(salario_bruto) - 1]
            if aux == 'Viagens em missão oficial':
                quant_viagem = Selector(text=body).xpath('//span[@class="beneficio__info"]/text()').get()
                if quant_viagem == None:
                    quant_viagem = Selector(text=body).xpath('//a[@class="beneficio__info"]/text()').get()
        print(salario_bruto)
        print(quant_viagem)

        dict_total = {
            'nome': nome,
            'data_nascimento': data_nascimento,
            'genero': 'F',
            'salario_bruto': salario_bruto,
            'quant_viagem': quant_viagem
        }
        dict_total.update(presencas_plenario_dict)
        dict_total.update(presencas_comissoes_dict)
        dict_total.update(par_dictionary)
        dict_total.update(gab_dictionary)

        print(dict_total)

        yield dict_total