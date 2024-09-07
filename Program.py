#Arquivo em python para a segunda fase do processo seletivo da target - Estágio Análise e Desenvolvimento
# Diogo Ramos Fernandes 

import xml.etree.ElementTree as ET
import json

# Função para ler e extrair dados do XML
def parse_xml(file):
    tree = ET.parse(file)
    root = tree.getroot()
    data = {}
    for row in root.findall('row'):
        dia = int(row.find('dia').text)
        valor = float(row.find('valor').text)
        data[dia] = valor
    return data

# Função para ler e extrair dados do JSON
def parse_json(file):
    with open(file, 'r') as f:
        data = json.load(f)
    return {item['dia']: item['valor'] for item in data}

# Função para somar os valores correspondentes dos dois arquivos
def somar_valores(xml_data, json_data):
    soma_total = {}
    for dia in range(1, 31):
        valor_xml = xml_data.get(dia, 0.0)
        valor_json = json_data.get(dia, 0.0)
        soma_total[dia] = valor_xml + valor_json
    return soma_total

# Caminhos para os arquivos
xml_file = 'dados.xml'
json_file = 'dados.json'

# Parse dos arquivos
xml_data = parse_xml(xml_file)
json_data = parse_json(json_file)

# Soma dos valores
soma_total = somar_valores(xml_data, json_data)

# Exibição do resultado
for dia, valor in soma_total.items():
    print(f'Dia {dia}: {valor:.2f}')
