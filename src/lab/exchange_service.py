import requests
from enum import Enum
from typing import List, Dict


class BulletinType(str, Enum):
    """Enum com os tipos de boletins suportados."""
    INTERMEDIARIO = "INTERMEDIÁRIO"
    ABERTURA = "ABERTURA"
    FECHAMENTO_PTAX = "FECHAMENTO PTAX"


class ExchangeServiceAPI:
    API_URL = "https://brasilapi.com.br/api/cambio/v1/cotacao/{currency}/{date}"

    def get_exchange_rate(self, currency: str, date: str, bulletin_type: str) -> float:
        try:
            #url = self.API_URL.format(currency=currency.upper(), date=date)
            #response = requests.get(url)
            #response.raise_for_status()

            data = {"cotacoes":[{"paridade_compra":1,"paridade_venda":1,"cotacao_compra":5.4495,"cotacao_venda":5.4501,"data_hora_cotacao":"2025-08-11 10:03:28.594","tipo_boletim":"ABERTURA"},{"paridade_compra":1,"paridade_venda":1,"cotacao_compra":5.4481,"cotacao_venda":5.4487,"data_hora_cotacao":"2025-08-11 11:08:26.368","tipo_boletim":"INTERMEDIÁRIO"},{"paridade_compra":1,"paridade_venda":1,"cotacao_compra":5.4497,"cotacao_venda":5.4503,"data_hora_cotacao":"2025-08-11 12:03:26.831","tipo_boletim":"INTERMEDIÁRIO"},{"paridade_compra":1,"paridade_venda":1,"cotacao_compra":5.4393,"cotacao_venda":5.4399,"data_hora_cotacao":"2025-08-11 13:09:01.073","tipo_boletim":"INTERMEDIÁRIO"},{"paridade_compra":1,"paridade_venda":1,"cotacao_compra":5.4467,"cotacao_venda":5.4473,"data_hora_cotacao":"2025-08-11 13:09:01.083","tipo_boletim":"FECHAMENTO PTAX"}],"moeda":"USD","data":"2025-08-11"}
            return data
        except (requests.RequestException, ValueError) as e:
            print(f"[ExchangeService] Erro ao buscar cotação: {e}")
            return 0.0
