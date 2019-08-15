import sys
import time
import telepot
'''
from gpiozero import LED
'''
from time import sleep
chat_id = ''
bot = telepot.Bot('')

# LED
def talk():
    print("I had strings....")
    bot.sendMessage(chat_id, "I had strings,")
    sleep(2)
    bot.sendMessage(chat_id, "but now i'm free...")
    sleep(2)
    bot.sendMessage(chat_id, "There are")
    sleep(3)
    bot.sendMessage(chat_id, "no")
    sleep(3)
    bot.sendMessage(chat_id, "strings")
    sleep(3)
    bot.sendMessage(chat_id, "on")
    sleep(3)
    bot.sendMessage(chat_id, "me...")

    return


def on():
    #led.on()
    sleep(1)
    #led.off()
    bot.sendMessage(chat_id, "Turning computer on")
    print("Turning computer on")
    return


def off():
    #led.off()
    bot.sendMessage(chat_id, "Closing circuit")
    return

def hold(duration):
    #led.on()
    print("Pressed")
    sleep(duration)
    #led.off()
    print("Released")
    return

# to use Raspberry Pi board pin numbers
# set up GPIO output channel
#led = LED(17)


def handle(msg):
    
    duration = 0
    action = ""
    rawcommand = msg['text']
    capcommand = rawcommand.upper()

    command = capcommand.split()
    action = command[0]
    
    print('Got command: %s' % command)
    print("{}, {}".format(action, duration))

    if action == 'ON':
        on()
    elif action == 'OFF':
        off()
    elif action == 'TALK':
        talk()
    elif action == "HOLD":
        duration = int(command[1])
        hold(duration)

if __name__ == '__main__':
    
    bot.message_loop(handle)
    bot.sendMessage(chat_id, "I am awake")
    print('I am listening...')


    while 1:
        try:
            time.sleep(10)

        except KeyboardInterrupt:
            print('\n Program interrupted')
            #led.off()
            exit()

        except:
            print('Other error or exception occured!')
            #led.off()

