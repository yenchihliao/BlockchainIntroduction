# try to connect to assigned private chain and check if it succeeds.
from web3 import Web3

# There are ipc, websocket, and http providers. It depend on wheather the node provides such a connection.
# More details: https://web3py.readthedocs.io/en/stable/providers.html
w3 = Web3(Web3.HTTPProvider("http://localhost:8080"))
print(w3.isConnected())

