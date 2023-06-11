import telebot
from telebot import types
import sqlite3
from settings import *
import time
from app import *
from datetime import datetime
import psycopg2



token = "5955004061:AAF6RFnFHYVW-Fvi3zdsgtTYFTxkvVHNLUQ"
chat_id = "463312066"
bot = telebot.TeleBot(token = token)

now = datetime.now() # get current time, output: 2023-06-10 21:22:32.212543
print(now) 

@bot.message_handler(commands = ["start"])

def start(message):
    bot.send_message(message.chat.id, text = "Welcome to Roman's Coffee House !\nNew orders will appear here")
    
    # c = data1()
    # bot.send_message(message.chat.id, text = c)
    # print(c)
    # print(message.chat.id)

    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)

    start_receiving = types.KeyboardButton("Start Receiving Orders")
    markup.add(start_receiving)

    bot.send_message(message.chat.id, text = "Press the button to start receiving new orders ", reply_markup = markup)

print(PATH_INSTANCE + "coffee_house.db")


@bot.message_handler(content_types = ["text"])

def receive_orders(message):
    if message.text == "Start Receiving Orders":
        markup = types.ReplyKeyboardRemove(selective = False)   # hide markup ( button )

        bot.send_message(message.chat.id, text = "You will be notified about new orders", reply_markup = markup)

        #conn = sqlite3.connect("")
        conn = psycopg2.connect("postgresql://flaskproject3_user:xnEZUvJuHkuCcDunC65QwPUPriKJt9Mh@dpg-ci2r01ak728i8tao9rd0-a.frankfurt-postgres.render.com/flaskproject3")
        cursor = conn.cursor()
        list_of_all_orders = []
        # for order in data:
        #     order_details = f"               NEW ORDER | {order[0]} |\n---------------------------------------\n\nOrder details:\n\n{order[8]}                                               ${order[7]} total\n\nCustomer info:\n\n{order[1]}\n{order[2]}\n{order[3]}\n{order[4]}\n{order[5]}\n{order[6]}\n\n---------------------------------------"   
        #     bot.send_message(message.chat.id, order_details)
        order_id = 0
        while True:
            cursor.execute('''SELECT * FROM receive_order''')
            data = cursor.fetchall()
            print(data)
            
            for order in data:
                order_id = order[0] # get order id
                #print(order_id)
                #print(order_id)
                if order_id in list_of_all_orders:  # if order in list
                    print(1)
                else:
                    print(5)
                    list_of_all_orders.append(order_id) # if not add order, so only new orders will be sent
                    order_details = f"               NEW ORDER | {order[0]} | {now.strftime('%H:%M')} \n---------------------------------------\n\nOrder details:\n\n{order[8]}                                               ${order[7]} total\n\nCustomer info:\n\n{order[1]}\n{order[2]}\n{order[3]}\n{order[4]}\n{order[5]}\n{order[6]}\n\n---------------------------------------"   
                    bot.send_message(message.chat.id, order_details)    # send order
                    # now.strftime('%H:%M:%S:%f) - 21:22:720768.... # hours, minutes, seconds, milliseconds
           
            #print(list_of_all_orders)

            #order_details = f"               NEW ORDER | {order[0]} |\n---------------------------------------\n\nOrder details:\n\n{order[8]}                                               ${order[7]} total\n\nCustomer info:\n\n{order[1]}\n{order[2]}\n{order[3]}\n{order[4]}\n{order[5]}\n{order[6]}\n\n---------------------------------------"   
            #bot.send_message(message.chat.id, order_details)
            
        
print("Bot has started")            
bot.polling(none_stop = True)

# while True:
#     data()
    #receive_order()
    #time.sleep(1)   # set delay for few seconds
    #bot.infinity_polling()  # launch the bot



   


# scripts runs together with flask, another terminal