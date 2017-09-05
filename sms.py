import nexmo
client = nexmo.Client(key = 'get the key', secret = 'type in the secret key')


message = raw_input('Enter your message: ')

response = client.send_message({'from' : 'ur phone no', 'to' : 'receivers message', 'text' : message})

response = response['messages'][0]

if response['status'] == '0':
    print 'send message', response['message-id']
else:
    print 'Error: ', response['error-text']
