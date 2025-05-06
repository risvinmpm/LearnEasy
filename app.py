from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/whatsapp', methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.form.get('Body')
    resp = MessagingResponse()
    msg = resp.message()

    # Simple keyword-based reply
    if 'hello' in incoming_msg.lower():
        reply = "Hi there! 👋 How can I help you today?"
    elif 'price' in incoming_msg.lower():
        reply = "Our pricing starts from $99. Want to know more?"
    else:
        reply = "Thanks for messaging! We'll get back to you shortly."

    msg.body(reply)
    return str(resp)

if __name__ == '__main__':
    app.run()
