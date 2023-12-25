from twilio.rest import Client

account_sid = 'AC364272f94e359f35dee808aa69b50870'
auth_token = 'f86982da674e0bc28e65e33b000e1c5d'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+17623095535',
    body='I AM ALIVE!!!',
    to='+917700972384'
)

print(message.sid)
