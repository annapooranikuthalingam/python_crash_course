"""
8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function
called show_messages(), which prints each text message.
"""

def show_messages(msg_list):
    for i in range(len(msg_list)):
        print(msg_list[i])

msg_list=["Hi","Good Morning","Thank You","Good Bye"]
show_messages(msg_list)