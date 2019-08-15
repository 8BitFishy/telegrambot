import sys
import time
import telepot
from gpiozero import LED
from time import sleep



chat_id = '9999999999'


#LED
def talk():
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
    led.on()
    sleep(1)
    led.off()
    bot.sendMessage(chat_id, "Turning computer on")
    print("Turning computer on")
    return
def off():
    led.off()
    bot.sendMessage(chat_id, "Turning computer on")
    return
# to use Raspberry Pi board pin numbers
# set up GPIO output channel
led = LED(17)

def handle(msg):
    
    command = msg['text']

    print('Got command: %s' % command)

    if command == 'ON':
        on()
    elif command =='OFF':
        off()
    elif command =='TALK':
        talk()

bot = telepot.Bot('XXXXXXXXXXXXX')
bot.message_loop(handle)
print('I am listening...')

while 1:
    try:
        time.sleep(10)
    
    except KeyboardInterrupt:
        print('\n Program interrupted')
        led.off()
        exit()
    
    except:
        print('Other error or exception occured!')
        led.off()

