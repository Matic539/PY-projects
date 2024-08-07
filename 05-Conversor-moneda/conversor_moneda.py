import requests

def obtener_tasas_de_cambio(api_url):
    # Hacer una solicitud HTTP a la API y obtener las tasas de cambio
    pass

def convertir_moneda(tasa_cambio, cantidad):
    # Realizar la conversión de moneda
    pass

def main():
    # Definir las monedas disponibles
    monedas_disponibles = ['USD', 'EUR', 'GBP', 'JPY', ...]

    # Solicitar moneda de origen, moneda de destino y cantidad al usuario
    moneda_origen = input("Introduce la moneda de origen: ").upper()
    moneda_destino = input("Introduce la moneda de destino: ").upper()
    cantidad = float(input("Introduce la cantidad a convertir: "))

    # Validar las entradas del usuario
    if moneda_origen not in monedas_disponibles or moneda_destino not in monedas_disponibles:
        print("Moneda no válida.")
        return

    # Obtener las tasas de cambio
    api_url = 'URL_DE_TU_API'
    tasas_de_cambio = obtener_tasas_de_cambio(api_url)

    # Calcular la tasa de cambio específica para las monedas seleccionadas
    tasa_cambio = tasas_de_cambio[moneda_destino] / tasas_de_cambio[moneda_origen]

    # Convertir la moneda
    resultado = convertir_moneda(tasa_cambio, cantidad)
    print(f"{cantidad} {moneda_origen} son {resultado} {moneda_destino}")

if __name__ == "__main__":
    main()
