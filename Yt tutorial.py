# -*- coding: utf-8 -*-
"""
Created on Sun Apr  11 18:30:07 2021

@author: iiaaaronn
"""


# %%
#-------------------------------------------------------------------------
# Episode 3
#-------------------------------------------------------------------------
import os
os.chdir('INSERT YOUR FILE PATH HERE\\smk_trading_bot-master')
#e.g.
# os.chdir('C:\\Users\\iiaaaronn\\Documents\\YT\\Betting\\Smarkets API tutorial\\Code\\smk_trading_bot-master')  
import client as sm_client
client = sm_client.SmarketsClient()
client.init_session()



# %%
#-------------------------------------------------------------------------
# Episode 4
#-------------------------------------------------------------------------
import os
os.chdir('YOUR FILE PATH')
import client as sm_client
client = sm_client.SmarketsClient()
client.init_session()

import datetime
start_date=datetime.datetime.now()+datetime.timedelta(days=1)
events =client.get_available_events(states=['upcoming'],types=['horse_racing_race'],start_datetime_max=start_date,limit=20)



# %%
#-------------------------------------------------------------------------
# Episode 5
#-------------------------------------------------------------------------

import os
os.chdir('YOUR FILE PATH')
import client as sm_client
client = sm_client.SmarketsClient()
client.init_session()

import datetime
start_date=datetime.datetime.now()+datetime.timedelta(days=1)

events=client.get_available_events(states=['upcoming'],
                                   types=['horse_racing_race'],
                                   start_datetime_max=start_date,
                                   limit=20,
                                   sort='id')

events=client.get_available_events(states=['upcoming'],
                                   types=['horse_racing_race'],
                                   #start_datetime_max=start_date,
                                   limit=20,
                                   sort='id')

events=client.get_available_events(states=['upcoming'],
                                   #types=['horse_racing_race'],
                                   start_datetime_max=start_date,
                                   limit=20,
                                   sort='id')



# %%
#-------------------------------------------------------------------------
# Episode 6
#-------------------------------------------------------------------------
import os
os.chdir('YOUR FILE PATH')
import client as sm_client
client = sm_client.SmarketsClient()
client.init_session()

import datetime
start_date=datetime.datetime.now()+datetime.timedelta(days=1)

events=client.get_available_events(states=['upcoming'],
                                   #types=['horse_racing_race'],
                                   type_domains=['horse_racing'],
                                   start_datetime_max=start_date,
                                    limit=20,
                                   sort='id')

# %%
#-------------------------------------------------------------------------
# Episode 7
#-------------------------------------------------------------------------
import os
os.chdir('YOUR FILE PATH')
import client as sm_client
client = sm_client.SmarketsClient()
client.init_session()
from datetime import datetime
from datetime import timedelta
start_date=datetime.datetime.now()+datetime.timedelta(days=1)

# enter time of race today in format 12:00
event_time='19:45'
# date today + time of event as a string
event_date_time=(datetime.today()).strftime("%Y-%m-%d")+" "+event_time
# convert that string to a date time object
event_date_time=datetime.strptime(event_date_time,"%Y-%m-%d %H:%M")
# set max start date for 5 min after event
start_date=event_date_time+timedelta(minutes=5)
# set min start date for 5 min before event
end_date=event_date_time-timedelta(minutes=5)

events=client.get_available_events(states=['upcoming'],
                                   #types=['horse_racing_race'],
                                   type_domains=['horse_racing'],
                                   start_datetime_max=start_date,
                                   start_datetime_min=end_date,
                                   limit=20,
                                   sort='id')
   
markets=client.get_related_markets(events)



# %%
#-------------------------------------------------------------------------
# Episode 8
#-------------------------------------------------------------------------
import os
os.chdir('YOUR FILE PATH')
import client as sm_client
client = sm_client.SmarketsClient()
client.init_session()
from datetime import datetime
from datetime import timedelta
start_date=datetime.datetime.now()+datetime.timedelta(days=1)

# enter time of race today in format 12:00
event_time='19:45'
# date today + time of event as a string
event_date_time=(datetime.today()).strftime("%Y-%m-%d")+" "+event_time
# convert that string to a date time object
event_date_time=datetime.strptime(event_date_time,"%Y-%m-%d %H:%M")
# set max start date for 5 min after event
start_date=event_date_time+timedelta(minutes=5)
# set min start date for 5 min before event
end_date=event_date_time-timedelta(minutes=5)

events=client.get_available_events(states=['upcoming'],
                                   #types=['horse_racing_race'],
                                   type_domains=['horse_racing'],
                                   start_datetime_max=start_date,
                                   start_datetime_min=end_date,
                                   limit=20,
                                   sort='id')
   
markets=client.get_related_markets(events)


# Quick method - normally works
to_win_market = markets[0]

# More robust method to ensure obtain 'To win market'
for market in markets:
    if market['name']=='To win':
        to_win_market = market
      
  
contracts =  client.get_related_contracts(   [to_win_market]  )  



for contract in contracts:
    name=contract['name']
    contract_id=contract['id']
    market_id=contract['market_id']
    print(f'name: {name}, contract_id: {contract_id}, market_id: {market_id}')
    
  
    
    
    
contracts =  client.get_related_contracts(   markets  ) 
for contract in contracts:
    name=contract['name']
    contract_id=contract['id']
    market_id=contract['market_id']
    print(f'name: {name}, contract_id: {contract_id}, market_id: {market_id}')    
    
    
    
    
    
# %%
#-------------------------------------------------------------------------
# Episode 9
#-------------------------------------------------------------------------
   
import os
os.chdir('YOUR FILE PATH')
import client as sm_client
client = sm_client.SmarketsClient()
client.init_session()
from datetime import datetime
from datetime import timedelta
start_date=datetime.datetime.now()+datetime.timedelta(days=1)

# enter time of race today in format 12:00
event_time='19:45'
# date today + time of event as a string
event_date_time=(datetime.today()).strftime("%Y-%m-%d")+" "+event_time
# convert that string to a date time object
event_date_time=datetime.strptime(event_date_time,"%Y-%m-%d %H:%M")
# set max start date for 5 min after event
start_date=event_date_time+timedelta(minutes=5)
# set min start date for 5 min before event
end_date=event_date_time-timedelta(minutes=5)

events=client.get_available_events(states=['upcoming'],
                                   #types=['horse_racing_race'],
                                   type_domains=['horse_racing'],
                                   start_datetime_max=start_date,
                                   start_datetime_min=end_date,
                                   limit=20,
                                   sort='id')
   
markets=client.get_related_markets(events)


for market in markets:
    if market['name']=='To win':
        to_win_market = market
      
quotes=client.get_quotes([to_win_market['id']])
    



# %%
#-------------------------------------------------------------------------
# Episode 10
#-------------------------------------------------------------------------
import os
os.chdir('YOUR FILE PATH')
import client as sm_client
client = sm_client.SmarketsClient()
client.init_session()

client.percent_to_decimal(4950)












