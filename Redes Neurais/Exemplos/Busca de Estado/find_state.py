import geopandas as gpd
import pandas as pd
import numpy as np
from shapely.geometry import Point
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

class ClassificadorEstadosBrasil:
    def __init__(self, caminho_geojson, pontos_por_estado=1000, tamanho_teste=0.2,
                 divisao_validacao=0.1, epocas=20, tamanho_lote=32, estado_random=42):
        self.caminho_geojson = caminho_geojson
        self.pontos_por_estado = pontos_por_estado
        self.tamanho_teste = tamanho_teste
        self.divisao_validacao = divisao_validacao
        self.epocas = epocas
        self.tamanho_lote = tamanho_lote
        self.estado_random = estado_random

        self.estados_gdf = None
        self.dados = None
        self.codificador = None
        self.num_classes = None
        self.modelo = None

    def carregar_estados(self):
        self.estados_gdf = gpd.read_file(self.caminho_geojson)
        self.estados_gdf = self.estados_gdf.rename(columns={'name': 'estado'})

    def amostrar_pontos_poligono(self, poligono):
        minx, miny, maxx, maxy = poligono.bounds
        pontos = []
        while len(pontos) < self.pontos_por_estado:
            x = np.random.uniform(minx, maxx)
            y = np.random.uniform(miny, maxy)
            p = Point(x, y)
            if poligono.contains(p):
                pontos.append((y, x))
        return pontos

    def gerar_amostras(self):
        lista_amostras = []
        for _, linha in self.estados_gdf.iterrows():
            nome_estado = linha['estado']
            geometria = linha['geometry']
            pontos = self.amostrar_pontos_poligono(geometria)
            for lat, lon in pontos:
                lista_amostras.append({'lat': lat, 'lon': lon, 'estado': nome_estado})
        self.dados = pd.DataFrame(lista_amostras)

    def preparar_dados(self):
        self.codificador = LabelEncoder()
        self.dados['id_estado'] = self.codificador.fit_transform(self.dados['estado'])
        self.num_classes = len(self.codificador.classes_)

        X = self.dados[['lat', 'lon']].values
        y = tf.keras.utils.to_categorical(self.dados['id_estado'], self.num_classes)
        return train_test_split(
            X, y,
            test_size=self.tamanho_teste,
            random_state=self.estado_random
        )

    def construir_modelo(self):
        self.modelo = tf.keras.Sequential([
            tf.keras.layers.Input(shape=(2,)),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(self.num_classes, activation='softmax')
        ])
        self.modelo.compile(
            optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )

    def treinar(self):
        X_train, X_test, y_train, y_test = self.preparar_dados()
        self.construir_modelo()
        self.modelo.fit(
            X_train, y_train,
            epochs=self.epocas,
            batch_size=self.tamanho_lote,
            validation_split=self.divisao_validacao
        )
        perda, acuracia = self.modelo.evaluate(X_test, y_test)
        print(f"Acurácia no teste: {acuracia:.4f}")

    def prever(self, lat, lon):
        coords = np.array([[lat, lon]])
        probs = self.modelo.predict(coords)
        indice = np.argmax(probs, axis=1)[0]
        return self.codificador.inverse_transform([indice])[0]

if __name__ == '__main__':
    classificador = ClassificadorEstadosBrasil('brazil-states.geojson')
    classificador.carregar_estados()
    classificador.gerar_amostras()
    classificador.treinar()

    try:
        lat = float(input("Latitude: ").strip())
        lon = float(input("Longitude: ").strip())
    except ValueError:
        print("Coordenadas inválidas.")
        exit(1)

    estado_pred = classificador.prever(lat, lon)
    print(f"O ponto ({lat}, {lon}) provavelmente está em: {estado_pred}")
