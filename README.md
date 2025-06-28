# 🤖 AutoBot - Telegram AI Auto-Reply Bot

A smart Telegram bot that automatically responds to messages using OpenAI's GPT-3.5-turbo model.

## 🚀 Features

- **Automatic AI Responses**: Uses OpenAI GPT-3.5-turbo to generate intelligent replies
- **Real-time Messaging**: Responds to incoming messages instantly
- **Edited Message Support**: Also responds to edited messages
- **User-friendly**: Natural, conversational responses
- **Logging**: Comprehensive logging for monitoring and debugging
- **Error Handling**: Robust error handling with fallback responses

## 📋 Prerequisites

- Python 3.7 or higher
- Telegram account
- OpenAI API key

## 🛠️ Installation

1. **Clone or download this repository**

2. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your credentials:**
   - Open `config.py`
   - Replace `your_openai_api_key_here` with your actual OpenAI API key

## ⚙️ Configuration

The bot is already configured with your Telegram API credentials:
- **API ID**: 27977268
- **API Hash**: 0992b260412b2e31fadab84037989a1e
- **App Title**: autobot
- **Short Name**: autops

## 🚀 Usage

1. **First time setup:**
   ```bash
   python autobot.py
   ```
   - You'll be prompted to enter your phone number
   - Enter the verification code sent to your Telegram
   - The session will be saved for future use

2. **Subsequent runs:**
   ```bash
   python autobot.py
   ```

## 📱 How it Works

1. The bot runs as a Telegram user (not a bot)
2. It automatically responds to any message sent to your account
3. Uses OpenAI to generate contextual, friendly replies
4. Logs all activities for monitoring

## 🔧 Customization

### Modify AI Behavior
Edit the system prompt in `autobot.py`:
```python
"content": f"You are a friendly and helpful Telegram user named AutoBot. Respond naturally and conversationally. Keep replies concise but engaging. The person messaging you is {sender_name}."
```

### Change AI Model
Modify the model parameter:
```python
model="gpt-4"  # or "gpt-3.5-turbo"
```

### Adjust Response Length
Change `max_tokens` parameter:
```python
max_tokens=200  # Increase for longer responses
```

## 📊 Logging

The bot provides detailed logging:
- Incoming messages
- AI response generation
- Error messages
- Connection status

## ⚠️ Important Notes

- **API Limits**: Be mindful of OpenAI API usage and costs
- **Privacy**: The bot processes all incoming messages
- **Session Security**: Keep the session file secure
- **Rate Limiting**: Respect Telegram's rate limits

## 🆘 Troubleshooting

### Common Issues:

1. **"Please configure your OpenAI API key"**
   - Add your OpenAI API key to `config.py`

2. **Authentication errors**
   - Delete the session file and re-authenticate

3. **Import errors**
   - Ensure all requirements are installed: `pip install -r requirements.txt`

## 📄 License

This project is for educational and personal use.

## 🤝 Support

If you encounter any issues, check the logs for detailed error messages.
