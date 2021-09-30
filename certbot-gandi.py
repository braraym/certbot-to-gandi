#!/bin/python
import os
import configparser
import requests
import json

try:
	config = configparser.ConfigParser()
	config.read('/usr/local/etc/certbot-gandi.conf')

except Exception as e:
	print(e)
	exit(1)

section = os.environ['CERTBOT_DOMAIN']

try:
	print('Section: ' + section)
	apikey = config.get(section, 'apikey')
	domain = config.get(section, 'domain')
	record_type = config.get(section, 'record_type')
	record_name = config.get(section, 'record_name')
	record_ttl = config.getint(section, 'record_ttl')

	record = {'type': record_type, 'name': record_name, 'ttl': record_ttl}

	certbot_validation = os.environ['CERTBOT_VALIDATION']
	print('Updating the record to ' + certbot_validation)

	url = 'https://dns.api.gandi.net/api/v5/domains/' + domain + '/records/' + record['name'] + '/' + record['type']
	headers = {'Content-Type': 'application/json', 'X-Api-Key': apikey}
	data = {'rrset_ttl': record['ttl'], 'rrset_values': [ certbot_validation ]}

	response = requests.put(url, headers=headers, data=json.dumps(data))
	result = json.loads(response._content)
	print(result)

	if response.status_code != 201:
		errorCount += 1

except Exception as e:
	print(e)
	exit(1)
