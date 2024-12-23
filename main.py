# Install libraries
from twilio.rest import Client
from datetime import datetime, timedelta
import time

# Twilio account credentials
account_sid = '' # Enter your Twilio account SID
auth_token = '' # Enter your Twilio account auth token

client = Client(account_sid, auth_token)

# Send message function
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! Message SID{message.sid}')
    except Exception as e:
        print('An error occurred')

# User input
name = input('Enter the recipient name: ')
recipient_number = input('Enter the recipient WhatsApp number with country code: ')
message_body = input(f'Enter the message you want to send to {name}: ')

# Schedule message
date_str = input('Enter the date you want to send the message (YYYY-MM-DD): ')
time_str = input('Enter the time you want to send the message (HH:MM in 24 hour format): ')

schedule_datetime = datetime.strptime(f'{date_str} {time_str}', '%Y-%m-%d %H:%M')
current_datetime = datetime.now()

time_difference = schedule_datetime - current_datetime
delays_seconds = time_difference.total_seconds()

if delays_seconds <= 0:
    print('Invalid time. Please enter a future time')
else:
    print(f'Message scheduled to be sent to {name} at {schedule_datetime}.')

# Wait until the scheduled time
time.sleep(delays_seconds)

# Send the message
send_whatsapp_message(recipient_number, message_body)