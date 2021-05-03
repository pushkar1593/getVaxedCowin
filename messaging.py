#!./env/bin/python3
import requests

# telegram api details
api_id = 4618509
api_hash = 'TELEGRAM_API_HASH'
bot_token = 'TELEGRAM_BOT_TOKEM'

# telegram group conf
channel_name = 'TELEGRAM_CHANNEL_NAME'


def send(message):
    send_text = 'https://api.telegram.org/bot'\
                + bot_token + '/sendMessage?chat_id=' + channel_name \
                + '&parse_mode=Markdown&text=' + message

    requests.get(send_text)


def main():
    print(send('testing'))


if __name__ == '__main__':
    main()
