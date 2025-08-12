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
            url = self.API_URL.format(currency=currency.upper(), date=date)
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()

        except (requests.RequestException, ValueError) as e:
            print(f"[ExchangeService] Erro ao buscar cotação: {e}")
            return 0.0