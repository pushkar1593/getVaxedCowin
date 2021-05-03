#!./env/bin/python3
import traceback
import time
import datetime
import getCentres
import messaging
import pytz


def update(cur_time):
    centres = getCentres.get_avail_centers()
    if len(centres) > 0:
        messaging.send("=UPDATE AS OF {}=".format(cur_time))
        results = 0
        for c in centres:
            message = list()
            message.append("=Centres available for date " + c.strftime(getCentres.date_format) + "=")
            for centre in centres[c]:
                results += 1
                message.append(str(centre[getCentres.pincode]) + "\n"
                    + centre[getCentres.vaccine] + "\n"
                    + str(centre[getCentres.available_capacity]) + " slots available \n"
                    + centre[getCentres.name] + "\n")
            messaging.send('\n'.join(message))
        messaging.send("=END OF UPDATE=")

        print("{} results sent out".format(results))


def main():
    ist = pytz.timezone("Asia/Kolkata")
    while True:
        cur_time = ist.localize(datetime.datetime.utcnow()).strftime('%d-%m-%y %H:%M:%S')
        try:
            update(cur_time)
        except:
            print("Error occured on {}".format(cur_time))
            traceback.print_exc()
        else:
            print("Run successful on {}".format(cur_time))
        time.sleep(10)


if __name__ == '__main__':
    main()
