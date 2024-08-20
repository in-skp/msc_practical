from bitcoinlib.wallets import Wallet
w = Wallet.create('Wallet1')
key1 = w.get_key()
print(key1.address)

# Send small transaction to wallet
w.scan()
print(w.info())


