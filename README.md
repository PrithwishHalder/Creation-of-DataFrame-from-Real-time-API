# Creation-of-DataFrame-from-Real-time-API

Use WebSocket, Pandas, Time, Json, Datetime

Steps:
1. Create a websocket URL, iiterval for which the websocket will continue to execute.
2. Initilize a empty list and df to be None.
3. Initialize a WebsocketApp and create a function
4. In the function get the message and convert the message to dictionary
5. Convert timeStapms to Datetime format and append the message to list
6. Continue until the interval time set for execution
7. Close the websocket connection
8. Create a DataFrame in df variable
9. Assign new column names

DONE!
