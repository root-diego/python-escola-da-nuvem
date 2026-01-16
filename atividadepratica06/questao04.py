import requests

def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()

        dados = resposta.json()[f"{moeda.upper()}BRL"]

        cotacao = float(dados["bid"])
        alta = float(dados["high"])
        baixa = float(dados["low"])
        data = dados["create_date"]

        return (
            f"Cotação: R${cotacao:.2f}\n"
            f"Alta: R${alta:.2f}\n"
            f"Baixa: R${baixa:.2f}\n"
            f"Data: {data}"
        )

    except requests.RequestException as e:
        return f"Erro ao consultar cotação: {e}"
    except KeyError:
        return "Moeda inválida ou não encontrada."

moeda = input("Digite a moeda (ex: USD, EUR, BTC, GBP): ")
resultado = consultar_cotacao(moeda)
print(resultado)
