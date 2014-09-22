__author__ = 'quek'


import requests
import json

def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

ancient_ids = []
with open('missingGENEIDuniq.txt') as f:
    for line in f:
        ancient_ids.append(line.strip())

ancient_chuncks = chunks(ancient_ids, 400)

for x in ancient_chuncks:
    data = { "id" : x }
    headers = {'content-type' : 'application/json', 'accept' :'text/javascript'}
    jdata = json.dumps(data)
    r = requests.post('http://rest.ensembl.org/archive/id', data=jdata, headers=headers )
    return_array = json.loads(r.text)
    for x in return_array:
        print "%s\t%s" % (x['id'] , x['release'])





