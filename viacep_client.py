import re
import requests
from typing import Optional, Dict

def get_address_by_cep(cep: str) -> Optional[Dict[str, str]]:
    cep_limpo = re.sub(r'\D', '', cep or '')
    
    if len(cep_limpo) != 8:
        return None
    
    try:
        response = requests.get(
            f'https://viacep.com.br/ws/{cep_limpo}/json/',
            timeout = 5
        )
        data = response.json()
        
        if data.get('erro'):
            return None
        
        return {
            'cep': cep_limpo,
            'address': data.get('logradouro', ''),
            'neighborhood': data.get('bairro', ''),
            'city': data.get('localidade', ''),
            'state': data.get('uf', ''),
        }
        
    except requests.RequestException as e:
        print(f'[ViaCEP] Erro ao consultar CEP {cep_limpo}: {e}')
        return None
    