import Telegram_Manager
from time import sleep
from gpiozero import LED
from time import sleep

'''
#filename = '/home/pi/Documents/telegramID.txt'
filename = 'telegramID.txt'

with open(filename) as f:
    IDS = f.read().splitlines()

print(filename)

#chat_id = str(IDS[0])
TOKEN = str(IDS[0])
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
'''

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
    #rawcommand = msg['text']
    capcommand = msg.upper()

    command = capcommand.split()
    action = command[0]

    print('Got command: %s' % command)
    print("{}".format(action), end="")

    if action == 'ON':
        print()
        try:
            on()
            Octavius_Receiver.send_message("Turning computer on")
        except NameError:
            Octavius_Receiver.send_message("LED package not recognised, are you sure this is a pi?")

    elif action == 'OFF':
        print()
        try:
            off()
            Octavius_Receiver.send_message("Turning computer off")
        except NameError:
            Octavius_Receiver.send_message("LED package not recognised, are you sure this is a pi?")

    elif action == 'TALK':
        print()
        Octavius_Receiver.send_message("Hello, what can I do for you?")

    elif action == "HOLD":
        try:
            duration = int(command[1])
            print(" {}".format(duration))
            hold(duration, Octavius_Receiver)
        except NameError:
            Octavius_Receiver.send_message("LED package not recognised, are you sure this is a pi?")

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

