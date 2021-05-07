#!./env/bin/python3
import sys
import traceback
import cowinException
import time
import datetime
import getCentres
import messaging
import pytz


def update(cur_time, district, telegram_group_code):
    centres = getCentres.get_avail_centers(district)
    if len(centres) > 0:
        message = list()
        message.append("=UPDATE AS OF {}=\n".format(cur_time))
        results = 0
        for c in centres:
            results += 1
            message.append('===============')
            message.append(c[getCentres.name_key])
            message.append(c[getCentres.address_key])
            message.append(str(c[getCentres.pincode_key]))
            for s in c[getCentres.sessions_key]:
                message.append('----')
                message.append(str(s[getCentres.available_capacity_key]) + " slots available")
                message.append("for " + s[getCentres.vaccine_key])
                message.append("on " + s[getCentres.date_key])
            message.append('===============\n')
        message.append("=END OF UPDATE=")

        messaging.send('\n'.join(message), telegram_group_code)

        print("{} results sent out".format(results))


def main():
    district_code = get_district_code(sys.argv[1])
    telegram_group_code = get_telegram_group_code(sys.argv[1])
    ist = pytz.timezone("Asia/Kolkata")
    sleep_time = 10
    while True:
        now = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
        cur_time = ist.localize(now).strftime('%d-%m-%y %H:%M:%S')
        try:
            update(cur_time, district_code, telegram_group_code)
        except cowinException.CowinException:
            print("waiting for a minute")
            if sleep_time < 600:
                sleep_time *= 2
            else:
                messaging.sendError('cowinException for district {}'.format(sys.argv[1]))
        except:
            print("Error occured on {}".format(cur_time))
            messaging.sendError("main thread excpetion for district {}".format(sys.argv[1]))
            traceback.print_exc()
        else:
            print("Run successful on {}".format(cur_time))
            sleep_time = 10
        time.sleep(sleep_time)


def get_district_code(district):
    switcher = {
        'bbmp': '294',
        'bangalore_urban': '265',
        'bangalore_rural': '276',
        'udupi': '286'
        # Add more districts as needed
    }
    if district in switcher:
        return switcher[district]
    else:
        raise NotImplementedError


def get_telegram_group_code(district):
    switcher = {
        'bbmp': 'TELEGRAMGROUPID',
        'bangalore_urban': 'TELEGRAMGROUPID',
        'udupi': 'TELEGRAMGROUPID'
        # Add more districts as needed
    }
    if district in switcher:
        return switcher[district]
    else:
        raise NotImplementedError


if __name__ == '__main__':
    main()
