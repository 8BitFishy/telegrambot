import Telegram_Manager
from time import sleep
from gpiozero import LED
from time import sleep

filename = '/home/pi/Documents/telegramID.txt'
with open(filename) as f:
    IDS = f.read().splitlines()

print(filename)

chat_id = str(IDS[0])
TOKEN = str(IDS[1])
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


led = LED(17)


def on():
    led.on()
    sleep(1)
    led.off()
    print("Turning computer on")
    return


def off():
    led.off()
    print("Turning computer off")
    return


def hold(duration, Octavius_Receiver):
    Octavius_Receiver.send_message("Holding...")
    led.on()
    print("Pressed")
    sleep(duration)
    led.off()
    Octavius_Receiver.send_message("...Released")

    print("Released")
    return


def handle(msg, Octavius_Receiver):
    duration = 0
    print(msg)
    rawcommand = msg['text']
    capcommand = rawcommand.upper()

    command = capcommand.split()
    action = command[0]

    print('Got command: %s' % command)
    print("{}, {}".format(action, duration))

    if action == 'ON':
        Octavius_Receiver.send_message("Turning computer on")
        on()
    elif action == 'OFF':
        Octavius_Receiver.send_message("Turning computer off")
        off()
    elif action == 'TALK':
        Octavius_Receiver.send_message("Hello, what can I do for you?")

    elif action == "HOLD":
        duration = int(command[1])
        hold(duration, Octavius_Receiver)

def receiver_loop(Octavius_Receiver):
    while True:
        text = Octavius_Receiver.get_response()
        if text != "":
            handle(text, Octavius_Receiver)

        sleep(0.5)


if __name__ == '__main__':

    print("Starting")
    previousmessage = ''

    Octavius_Receiver = Telegram_Manager.generate_receiver()
    Octavius_Receiver.send_message("I am awake...")
    receiver_loop(Octavius_Receiver)

