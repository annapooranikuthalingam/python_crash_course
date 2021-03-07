"""
8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages()
with a copy of the list of messages. After calling the function, print both of your lists to show
that the original list has retained its messages.
"""
def send_messages(msg_list):
    sent_messages=[]
    while(msg_list):
        message=msg_list.pop()
        print(message)
        sent_messages.append(message)
    return sent_messages

msg_list=["Hi","Good Morning","Thank You","Good Bye"]
sent_messages=send_messages(msg_list[:])
print(msg_list)
print(sent_messages)