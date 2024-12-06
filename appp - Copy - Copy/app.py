from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session to work

# Predefined responses
responses = {
    "hello": "Hi there! How can I assist you today?",
    "how are you": "I'm just a bunch of code, but I'm here to help!",
    "bye": "Goodbye! Have a great day!",
    # Add more responses if needed
}

@app.route('/')
def index():
    if 'messages' not in session:
        session['messages'] = []  # Initialize messages if not set

    return render_template('index.html', messages=session['messages'])

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.form.get('message')
    # Save user message
    session['messages'].append({'sender': 'user', 'text': user_message})

    # Get bot response based on user message
    bot_response = responses.get(user_message.lower(), "Sorry, I don't understand that.")
    
    # Save bot response
    session['messages'].append({'sender': 'bot', 'text': bot_response})

    session.modified = True  # Ensure session is updated
    return render_template('index.html', messages=session['messages'])

@app.route('/clear', methods=['POST'])
def clear_chat():
    session.pop('messages', None)  # Clear chat history
    return render_template('index.html', messages=[])

if __name__ == '__main__':
    app.run(debug=True)


