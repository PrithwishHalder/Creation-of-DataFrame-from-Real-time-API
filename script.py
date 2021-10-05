import websocket, pandas as pd, time, json
from datetime import datetime

coin = "etheur"
interval = 60
URL = f"wss://stream.binance.com:9443/ws/{coin}@trade"
start_time = time.time()
columns = [  
    "Event type",
    "Event time",  
    "Symbol",  
    "Trade ID",
    "Price",    
    "Quantity",    
    "Buyer order ID",    
    "Seller order ID",    
    "Trade time",
    "Is the buyer the market maker?",
    "Ignore"
]
records = list()
df = None

def on_message(ws, message):
    # Converting str to dict format
    msg = json.loads(message)
    # Converting Timestamp to datetime format
    msg['E'] = datetime.fromtimestamp(msg['E'] / 1e3).strftime("%m/%d/%Y, %H:%M:%S")
    msg['T'] = datetime.fromtimestamp(msg['T'] / 1e3).strftime("%m/%d/%Y, %H:%M:%S")
    # append each message to list
    records.append(msg)
    diff = int(time.time() - start_time)
    # Close connection after a time interval
    if diff >= interval:
        ws.close()
        # Create Dataframe using the list of records
        df = pd.DataFrame(records)
        # Assign column names
        df.columns = columns
        print(df.shape)

# Initializing Websocket
ws = websocket.WebSocketApp(URL,on_message= on_message)
# Executing Websocket
ws.run_forever()