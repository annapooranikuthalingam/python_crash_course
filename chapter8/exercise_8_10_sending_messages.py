"""
8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function
called send_messages() that prints each text message and moves each message to a new list called
sent_messages as it’s printed. After calling the function, print both of your lists to make sure
the messages were moved correctly.
"""
def show_messages(msg_list):
    for i in range(len(msg_list)):
        print(msg_list[i])

def send_messages(msg_list):
    sent_messages=[]
    while(msg_list):
        message=msg_list.pop()
        print(message)
        sent_messages.append(message)
    return sent_messages

msg_list=["Hi","Good Morning","Thank You","Good Bye"]
sent_messages=send_messages(msg_list)
print(msg_list)
print(sent_messages)