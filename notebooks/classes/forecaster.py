import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from joblib import load

class Forecaster:
    def __init__(self):

        # Inicialização da classe Forecaster
        self.dataframe_Tratado = pd.read_csv("G:\\\\Drives compartilhados\\Projeto 4\\df_tratado.csv")

    def gerador_do_forecaster(self, data, modelo):

        # Método para gerar previsões usando o modelo
        novo_df = self.dataframe_Tratado
        data_entrega = pd.to_datetime(data)  # Converte a data de entrega para o formato datetime
        print(data_entrega)
        semana = data_entrega.isocalendar().week  # Calcula a semana do ano da data de entrega
        print(semana)
        df_pred = self.dataFrame_completo(novo_df, data_entrega, semana)  # Cria um DataFrame completo para previsão
        prev = self.prever(df_pred, modelo, data_entrega)  # Realiza a previsão
        return self.campos_dataFrame_previsao(prev)  # Retorna o DataFrame com os campos de previsão

    def imputar_novas_colunas(self, df, sku, colunas):

        # Método para imputar valores médios em novas colunas
        valores_imputados = {}

        for coluna in colunas:
            valor_imputados = round(df[df['sku'] == sku][coluna].mean())
            valores_imputados[coluna] = valor_imputados

        return valores_imputados

    def criacao_nova_linha(self, data_usuario, sku, semana, tabela_limpa_SemNan):

        # Método para criar uma nova linha no DataFrame
        gerar_nova_linha_dataFrame = {
            'sku': sku,
        }

        ordem_features = ['sku', 'unit_price', 'sku_height', 'sku_width', 'sku_length',
                          'sku_weight', 'winning_price', 'stock_qty',
                          'log_avg_website_visits_last_week', 'diferencia_concorrencia']

        valores_imputados = self.imputar_novas_colunas(tabela_limpa_SemNan, sku, ordem_features)
        gerar_nova_linha_dataFrame.update(valores_imputados)

        gerar_nova_linha_dataFrame['items_sold'] = np.nan

        valores_avg_stock = self.imputar_novas_colunas(tabela_limpa_SemNan, sku,
                                                       ['log_avg_website_visits_last_week', 'stock_qty'])
        gerar_nova_linha_dataFrame.update(valores_avg_stock)

        gerar_nova_linha_dataFrame['semana_do_ano'] = semana

        dados_externos = self.imputar_novas_colunas(tabela_limpa_SemNan, sku, ['selic', 'taxa-desemprego'])
        gerar_nova_linha_dataFrame.update(dados_externos)

        return gerar_nova_linha_dataFrame

    def dataFrame_completo(self, df, data_usuario, semana):

        # Método para criar um DataFrame completo para previsão
        predicao_dataFrame = pd.DataFrame(columns=df.columns)

        skus_unicos = df['sku'].unique()

        dados_novos = []

        for sku in skus_unicos:
            nova_linha_dataFrame = self.criacao_nova_linha(data_usuario, sku, semana, df)
            dados_novos.append(nova_linha_dataFrame)

        predicao_dataFrame = pd.DataFrame(dados_novos)

        return predicao_dataFrame

    def prever(self, predicao_dataFrame, model, data_entrega):

        # Método para realizar a previsão
        teste = model.predict(predicao_dataFrame.drop(['items_sold'], axis=1))

        predicao_dataFrame['items_sold'] = teste.astype(int)
        predicao_dataFrame['data_entrega'] = data_entrega
        return predicao_dataFrame

    def campos_dataFrame_previsao(self, df_pred):
        
        # Método para selecionar os campos relevantes no DataFrame de previsão
        df_pred = df_pred.sort_values('sku').reset_index(drop=False)
        df_pred = df_pred[['sku', 'data_entrega', 'semana_do_ano', 'items_sold']]

        le = load('../notebooks/classes/modelo/label_encoder_sku.joblib')
        df_pred['sku'] = le.inverse_transform(df_pred['sku'])

        return df_pred
