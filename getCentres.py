#!./env/bin/python3
import time
import requests
import json
import datetime

# Session schema keys
min_age = 'min_age_limit'
available_capacity = 'available_capacity'
vaccine = 'vaccine'
name = 'name'
pincode = 'pincode'

date_format = '%d-%m-%y'


def get_avail_centers():
	# Api endpoint
	api = '/v2/appointment/sessions/public/findByDistrict'
	endpoint = 'https://cdn-api.co-vin.in/api'

	# Api Params
	bbmp_district_id = '294'
	today = datetime.date.today()

	all_centers = {}

	for i in range(3):
		date = today + datetime.timedelta(days=i)
		sessions = None
		ok = False

		while not ok:
			r = requests.get(endpoint+api, {'district_id': bbmp_district_id, 'date': date.strftime(date_format)})
			if r.ok:
				ok = True
				sessions = json.loads(r.text)['sessions']
			else:
				print(r)
				print(r.text)
				time.sleep(2)

		avail = []
		for centre in sessions:
			if centre[min_age] < 45 and centre[available_capacity] > 0:
				avail.append(centre)
		if len(avail) > 0:
			print(date)
			all_centers[date] = avail

	return all_centers


def main():
	avail_centers = get_avail_centers()
	if len(avail_centers) > 0:
		print('hi')
		print(avail_centers[datetime.date.today()])


if __name__ == "__main__":
	main()
