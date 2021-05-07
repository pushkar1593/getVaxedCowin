#!./env/bin/python3
import requests

# telegram api details
api_id = 4  # API_ID
api_hash = ''  # API HASH
bot_token = ''  # BOT TOKEN

# telegram group conf
bot_chatid = ''  # BOT ID


def sendError(message):
    send_text = 'https://api.telegram.org/bot' \
                + bot_token + '/sendMessage?chat_id=' + bot_chatid \
                + '&parse_mode=Markdown&text=' + message
    requests.get(send_text)


def send(message, group_code):
    send_text = 'https://api.telegram.org/bot'\
                + bot_token + '/sendMessage?chat_id=' + group_code \
                + '&parse_mode=Markdown&text=' + message

    requests.get(send_text)


def main():
    print(sendError('testing'))


if __name__ == '__main__':
    main()
