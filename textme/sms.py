from twilio.rest import Client

account_sid = '*******************'
auth_token = '*****************'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='*******',
    to='***************',
    body="Hi from twilio"
)

print(message.sid)
