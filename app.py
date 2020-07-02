from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data():

    #Recebendo dataframe da função readData
    df_sanca = readData()

    #Convertendo para dicionário
    data = df_sanca.to_dict(orient='index')

    return jsonify(data)

def readData():

    #Lendo arquivo CSV
    df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-cities.csv')

    #Filtrando para linha da cidade determinada -> São Carlos
    sanca_data_v1 = df.loc[df['city'] == 'São Carlos/SP']

    #Excluindo colunas que não serão usadas
    sanca_data_v2 = sanca_data_v1.drop(columns = ['ibgeID', 'deaths_per_100k_inhabitants', 'totalCases_per_100k_inhabitants',
                                      'deaths_by_totalCases', '_source','name_RegiaoDeSaude','cod_RegiaoDeSaude'])

    #Tirando acentuação do nome da cidade de São Carlos -> São Carlos to Sao Carlos
    sanca_data_v2['city'] = sanca_data_v2['city'].replace(['São Carlos/SP'], 'Sao Carlos/SP')
    print(sanca_data_v2.columns)

    return sanca_data_v2

if __name__ == '__main__':
    app.run(debug=True)
