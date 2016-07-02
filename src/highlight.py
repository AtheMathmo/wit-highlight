import sys
from wit import Wit

if len(sys.argv) != 2:
    print('usage: python ' + sys.argv[0] + ' <wit-token>')
    exit(1)
access_token = sys.argv[1]

def send(request, response):
    print(response['text'])

def sendToHighlights(request):
	context = request['context']
	entities = request['entities']

	print "I stored:", entities

	return context



actions = {
    'send': send,
    'sendToHighlights': sendToHighlights,
}

client = Wit(access_token=access_token, actions=actions)
client.interactive()
