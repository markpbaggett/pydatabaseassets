from urllib2 import urlopen
import json

f = open('apikey.txt', 'r')
apikey = f.read()
fullURL = 'http://lgapi.libapps.com/1.1/assets?site_id=681&key=' + apikey.rstrip('\n') + '&asset_types=10'
req = urlopen(fullURL).read()
outfile= json.loads(req)
recordCount = 0

textFile = open('databaseassets.csv', 'w')
textFile.write('Database name,URL, Enabled Proxy\n')
for record in outfile:
	recordCount += 1
	textFile.write(record['name'] + ',' + record['url'] + ',' + str(record['meta']['enable_proxy']) + '\n')
textFile.close()

print "\nWrote out %d records" % recordCount
