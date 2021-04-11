import datetime
import logging
from typing import Any, Dict, List
from collections import defaultdict

import requests

from config import configuration

log = logging.getLogger(__name__)









percent_to_decimal_dic={ 9999:1.0001,
              9901:1.01,
              9804:1.02,
              9709:1.03,
              9615:1.04,
              9524:1.05,
              9434:1.06,
              9346:1.07,
              9259:1.08,
              9174:1.09,
              9091:1.1,
              9009:1.11,
              8929:1.12,
              8850:1.13,
              8772:1.14,
              8696:1.15,
              8621:1.16,
              8547:1.17,
              8475:1.18,
              8403:1.19,
              8333:1.20,
              8264:1.21,
              8197:1.22,
              8130:1.23,
              8065:1.24,
              8000:1.25,
              7937:1.26,
              7874:1.27,
              7812:1.28,
              7752:1.29,
              7692:1.30,
              7634:1.31,
              7576:1.32,
              7519:1.33,
              7463:1.34,
              7407:1.35,
              7353:1.36,
              7299:1.37,
              7246:1.38,
              7194:1.39,
              7143:1.40,
              7092:1.41,
              7042:1.42,
              6993:1.43,
              6944:1.44,
              6897:1.45,
              6849:1.46,
              6803:1.47,
              6757:1.48,
              6711:1.49,
              6667:1.5,
              6623:1.51,
              6579:1.52,
              6536:1.53,
              6494:1.54,
              6452:1.55,
              6410:1.56,
              6369:1.57,
              6329:1.58,
              6289:1.59,
              6250:1.6,
              6211:1.61,
              6173:1.62,
              6135:1.63,
              6098:1.64,
              6061:1.65,
              6024:1.66,
              5988:1.67,
              5952:1.68,
              5917:1.69,
              5882:1.70,
              5848:1.71,
              5814:1.72,
              5780:1.73,
              5747:1.74,
              5714:1.75,
              5682:1.76,
              5650:1.77,
              5618:1.78,
              5587:1.79,
              5556:1.8,
              5525:1.81,
              5495:1.82,
              5464:1.83,
              5435:1.84,
              5405:1.85,
              5376:1.86,
              5348:1.87,
              5319:1.88,
              5291:1.89,
              5263:1.90,
              5236:1.91,
              5208:1.92,
              5181:1.93,
              5155:1.94,
              5128:1.95,
              5102:1.96,
              5076:1.97,
              5051:1.98,
              5025:1.99,
              5000:2,
              4950:2.02,
              4902:2.04,
              4854:2.06,
              4808:2.08,
              4762:2.1,
              4717:2.12,
              4673:2.14,
              4630:2.16,
              4587:2.18,
              4545:2.2,
              4505:2.22,
              4464:2.24,
              4425:2.26,
              4386:2.28,
              4348:2.3,
              4310:2.32,
              4274:2.34,
              4237:2.36,
              4202:2.38,
              4167:2.4,
              4132:2.42,
              4098:2.44,
              4065:2.46,
              4032:2.48,
              4000:2.5,
              3968:2.52,
              3937:2.54,
              3906:2.56,
              3876:2.58,
              3846:2.6,
              3817:2.62,
              3788:2.64,
              3759:2.66,
              3731:2.68,
              3704:2.7,
              3676:2.72,
              3650:2.74,
              3623:2.76,
              3597:2.78,
              3571:2.8,
              3546:2.82,
              3521:2.84,
              3497:2.86,
              3472:2.88,
              3448:2.9,
              3425:2.92,
              3401:2.94,
              3378:2.96,
              3356:2.98,
              3333:3,
              3279:3.05,
              3226:3.1,
              3175:3.15,
              3125:3.2,
              3077:3.25,
              3030:3.3,
              2985:3.35,
              2941:3.4,
              2899:3.45,
              2857:3.5,
              2817:3.55,
              2778:3.6,
              2740:3.65,
              2703:3.7,
              2667:3.75,
              2632:3.8,
              2597:3.85,
              2564:3.9,
              2532:3.95,
              2500:4,
              2439:4.1,
              2381:4.2,
              2326:4.3,
              2273:4.4,
              2222:4.5,
              2174:4.6,
              2128:4.7,
              2083:4.8,
              2041:4.9,
              2000:5,
              1961:5.1,
              1923:5.2,
              1887:5.3,
              1852:5.4,
              1818:5.5,
              1786:5.6,
              1754:5.7,
              1724:5.8,
              1695:5.9,
              1667:6,
              1613:6.2,
              1562:6.4,
              1515:6.6,
              1471:6.8,
              1429:7,
              1389:7.2,
              1351:7.4,
              1316:7.6,
              1282:7.8,
              1250:8,
              1220:8.2,
              1190:8.4,
              1163:8.6,
              1136:8.8,
              1111:9,
              1087:9.2,
              1064:9.4,
              1042:9.6,
              1020:9.8,
              1000:10,
              952:10.5,
              909:11,
              870:11.5,
              833:12,
              800:12.5,
              769:13,
              741:13.5,
              714:14,
              690:14.5,
              667:15,
              645:15.5,
              625:16,
              606:16.5,
              588:17,
              571:17.5,
              556:18,
              541:18.5,
              526:19,
              513:19.5,
              500:20,
              476:21,
              455:22,
              435:23,
              417:24,
              400:25,
              385:26,
              370:27,
              357:28,
              345:29,
              333:30,
              312:32,
              294:34,
              278:36,
              263:38,
              250:40,
              238:42,
              227:44,
              217:46,
              208:48,
              200:50,
              182:55,
              167:60,
              154:65,
              143:70,
              133:75,
              125:80,
              118:85,
              111:90,
              105:95,
              100:100,
              91:110,
              83:120,
              77:130,
              71:140,
              67:150,
              62:160,
              59:170,
              56:180,
              53:190,
              50:200,
              48:210,
              45:220,
              43:230,
              42:240,
              40:250,
              38:260,
              37:270,
              36:280,
              34:290,
              33:300,
              20:500,
              10:1000,
              1:10000
        
            }



decimal_to_percent_dic={v: k for k, v in percent_to_decimal_dic.items()}




 




















class OrderPlaceError(Exception):
    pass





class SmarketsClient:
    def __init__(self):
        self.auth_token = None
        

    def _auth_headers(self):
        return {'Authorization': 'Session-Token ' + self.auth_token}

    def init_session(self):
        log.info('initiating session')
        self.auth_token = configuration['auth'].get('auth_token')
        if not self.auth_token:
            response = requests.post(
                f'{configuration["api"]["base_url"]}sessions/',
                json={
                    'username': configuration['auth']['login'],
                    'password': configuration['auth']['password'],
                },
            ).json()
            self.auth_token = response.get('token')
        log.info('auth token: %s', self.auth_token)

 
    
    
   


    def get_available_events(
        self,
        states: List[str] = None,
        types: List[str] = None,
        start_datetime_max: datetime.datetime = None,
        start_datetime_min: datetime.datetime = None,
        limit: int = 20,
        sort: str = 'id',
        type_domains : List[str] = None       
    ):
        
        
        all_filters=[]
        
        #Check if exist and add to all_filters
        if states:
            states_filter = [f'states={state}' for state in states]
            all_filters+=states_filter
        if types:
            types_filter = [f'types={type_}' for type_ in types]
            all_filters+=types_filter        
        if start_datetime_max:
            start_datetime_max=start_datetime_max.strftime("%Y-%m-%dT%H:%M:%SZ")
            start_datetime_max_filter=[f'start_datetime_max={start_datetime_max}']
            all_filters+=start_datetime_max_filter
        
        if type_domains:
            type_domains_filter = [f'type_domain={type_}' for type_ in type_domains]
            all_filters+=type_domains_filter    
        if start_datetime_min:
            start_datetime_min=start_datetime_min.strftime("%Y-%m-%dT%H:%M:%SZ")
            start_datetime_min_filter=[f'start_datetime_min={start_datetime_min}']
            all_filters+=start_datetime_min_filter






        #Add to all filters if gauranteed to exist
        limit_filter=[f'limit={limit}']
        all_filters+=limit_filter
        sort_filter=[f'sort={sort}']
        all_filters+=sort_filter
        
        
        
        
        
        page_filter='?'+'&'.join(all_filters)
        
        print(page_filter)
        events = [] 
        while page_filter:
            request_url = f'{configuration["api"]["base_url"]}events/{page_filter}'
            current_page = self._client_wrapper(request_url)
            events += current_page['events']
            page_filter = current_page['pagination']['next_page']

        return events













    def get_related_markets(self, events):
        markets = []
        event_ids = [event['id'] for event in events]
        i = 0
        chunk_size = configuration["api"]["chunk_size"]
        while i * chunk_size < len(event_ids):
            events_to_fetch = ','.join(
                event_ids[i * chunk_size:(i + 1) * chunk_size]
            )
            request_url = (
                f'''{configuration["api"]["base_url"]}events/{events_to_fetch}/markets/'''
                f'''?sort=event_id,display_order&with_volumes=true'''
            )
            markets += self._client_wrapper(request_url)['markets']
            i += 1
        return markets







    def get_related_contracts(self, markets):
        contracts = []
        market_ids = [market['id'] for market in markets]
        i = 0
        chunk_size = configuration["api"]["chunk_size"]
        while i * chunk_size < len(market_ids):
            markets_to_fetch = ','.join(
                market_ids[i * chunk_size:(i + 1) * chunk_size]
            )
            request_url = (
                f'''{configuration["api"]["base_url"]}markets/{markets_to_fetch}/contracts/'''
            )
            contracts += self._client_wrapper(request_url)['contracts']
            i += 1
        return contracts






 
    
    
    
    
    
    
    
    
    
    
    def place_order(
        self,
        market_id,
        contract_id,
        price,
        quantity,
        side,
    ):
        log.info(
            'placing order: m_id %s: c_id %s\t %s %s @ %s',
            market_id,
            contract_id,
            side,
            quantity,
            price,
        )
        response = requests.post(
            f'{configuration["api"]["base_url"]}orders/',
            json={
                'market_id': market_id,
                'contract_id': contract_id,
                'price': price,
                'quantity': quantity,
                'reference_id': str(int(datetime.datetime.utcnow().timestamp())),
                'side': side,
            },
            headers=self._auth_headers(),
        )
        response_body = response.json()
        if response.status_code != 200:
            raise OrderPlaceError(response_body.get('error_type'))
        log.info(
            f'''order placed: m_id {market_id}: c_id {contract_id} \t {side} {quantity} @ {price}|'''
            f'''balance:{response_body["available_balance"]} executed:{response_body["total_executed_quantity"]}'''
            f''' exposure:{response_body["exposure"]}'''
        )

    def cancel_order(self, order_id):
        requests.delete(
            f'{configuration["api"]["base_url"]}orders/{order_id}/',
            headers=self._auth_headers(),
        )

    def cancel_all_orders(self, market_id):
        requests.delete(
            f'{configuration["api"]["base_url"]}orders/?market_id={market_id}',
            headers=self._auth_headers(),
        )

    def get_orders(self, states):
        orders = []
        states_to_fetch = '&'.join([f'states={state}' for state in states])
        next_page = f'?limit={configuration["api"]["chunk_size"]}&{states_to_fetch}'
        while next_page:
            response = requests.get(
                f'{configuration["api"]["base_url"]}orders/{next_page}',
                headers=self._auth_headers(),
            ).json()
            log.info(response)
            orders += response['orders']
            next_page = response['pagination']['next_page']
        return orders








    def get_events(self, event_ids: List[str]):
        event_ids_filter = '&'.join([f'ids={event_id}' for event_id in event_ids])
        request_url = f'{configuration["api"]["base_url"]}events/?{event_ids_filter}'
        return self._client_wrapper(request_url).get('events')

    def get_markets(self, market_ids: List[str], with_volumes: bool=False):
        markets = ','.join(market_ids)
        request_url = f'{configuration["api"]["base_url"]}markets/{markets}/?with_volumes={with_volumes}'
        return self._client_wrapper(request_url).get('markets')




    def get_quotes(self, market_ids: List[str]):
        quotes = []
        i = 0
        chunk_size = configuration["api"]["chunk_size"]
        while i * chunk_size < len(market_ids):
            markets_to_fetch = ','.join(
                market_ids[i * chunk_size:(i + 1) * chunk_size]
            )
            request_url = f'{configuration["api"]["base_url"]}markets/{markets_to_fetch}/quotes/'
            quotes += [self._client_wrapper(request_url)]
            i += 1
        
        quotes_result = {}
        for quote_entry in quotes:
            for contract_id, order_book in quote_entry.items():
                quotes_result[contract_id] = order_book
        return quotes_result












    def get_accounts(self):
        response = requests.get(
            f'{configuration["api"]["base_url"]}accounts/', headers=self._auth_headers()
        ).json()
        return response

    def _client_wrapper(self, url: str) -> Dict[str, Any]:
        log.info(f'calling url: {url}')
        return requests.get(url).json()



    def percent_to_decimal(self,odds):
        
        decimal=percent_to_decimal_dic[odds]
        return decimal

    def decimal_to_percent(self,odds):
        
        percent=decimal_to_percent_dic[odds]
        return percent
    
    
    def quantity_to_stake(self,quantity,price):
        
        return round((quantity*price/100000000  ), 2)
        
        
    def stake_to_quantity(self,stake,price):
        return int(stake*100000000/  price)