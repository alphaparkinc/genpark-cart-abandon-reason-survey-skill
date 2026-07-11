from client import CartAbandonReasonClient
client = CartAbandonReasonClient()
print(client.analyze_reason("shipping_cost", 50.0))