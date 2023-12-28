# Crypto-kraken

## Descripción General
Esta herramienta está diseñada para analizar datos de criptomonedas, centrándose especialmente en pares de divisas y sus indicadores técnicos. Utiliza la API de Kraken para obtener datos en tiempo real y ofrece gráficos interactivos para visualizar los datos y calcular indicadores técnicos como el Oscilador Estocástico y las Medias Móviles.

## Instalación

### Requisitos

Python 3.x
Bibliotecas de Python requeridas como se enumeran en requirements.txt

### Configuración

Clonar el Repositorio (Asumiendo que Git está instalado)

```
git clone [URL de Tu Repositorio]
cd [Nombre de Tu Repositorio]
```
Instalar Dependencias

```
pip install -r requirements.txt
```

## Ejecución de la Aplicación
Iniciar la Aplicación Dash

```
python application.py
```
Acceder a la Interfaz Web

Abre un navegador web y navega a http://127.0.0.1:8050/ (o la dirección indicada en la terminal).

## Características
Recuperación de Datos: Obtener datos de criptomonedas en tiempo real de Kraken.
Gráficos Interactivos: Visualizar pares de divisas y sus movimientos a lo largo del tiempo.
Indicadores Técnicos: Calcular y mostrar indicadores como el Oscilador Estocástico y las Medias Móviles.
Entrada del Usuario: Personalizar la visualización de datos a través de varias opciones de entrada.

## Estructura de Archivos
application.py: Configuración principal de la aplicación Dash y servidor.
kraken_data.py: Maneja la obtención de datos de la API de Kraken.
graphing.py: Funciones para generar gráficos interactivos.
technical_indicators.py: Cálculo de indicadores técnicos.
requirements.txt: Lista de dependencias de Python.

## Notas de Uso
Asegúrate de tener una conexión a internet estable para la obtención de datos.
La herramienta está diseñada con fines educativos y no para operaciones de trading en vivo.

## Contribuir
Siéntete libre de bifurcar el proyecto y enviar solicitudes de cambios para cualquier mejora.