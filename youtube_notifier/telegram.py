import requests


def telegram_bot_sendtext(bot_message):

    bot_token = ''
    bot_chadID = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chadID + '&parse_mode=MarkdownV2&disable_web_page_preview=True&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


if __name__ == "__main__":
    test = telegram_bot_sendtext("Test Message")