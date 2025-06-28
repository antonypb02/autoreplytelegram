# ✅ AutoBot - Telegram AI Auto-Reply Bot
# Created with your provided credentials - Now using Google Gemini AI

import os
import logging
from telethon import TelegramClient, events
import google.generativeai as genai
from config import API_ID, API_HASH, GEMINI_API_KEY, SESSION_NAME

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Initialize Google Gemini AI
genai.configure(api_key=GEMINI_API_KEY)

# Create the Telegram client
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

# === Function: Generate AI reply using Gemini ===
def generate_ai_reply(user_msg, sender_name="User"):
    try:
        logger.info(f"🧠 Generating AI reply for: {user_msg[:50]}...")
        
        # Create Gemini model instance
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Create the prompt
        system_prompt = f"""You are a friendly and helpful Telegram user named AutoBot. 
        Respond naturally and conversationally. Keep replies concise but engaging (max 100 words). 
        The person messaging you is {sender_name}.
        
        User message: {user_msg}
        
        Please provide a friendly, natural response:"""
        
        # Generate response
        response = model.generate_content(system_prompt)
        
        reply = response.text.strip()
        logger.info(f"✅ AI Reply generated: {reply[:50]}...")
        return reply
        
    except Exception as e:
        logger.error(f"❌ AI Error: {e}")
        return "Hey! I'm a bit busy right now, but I'll get back to you soon! 😊"

# === Event Listener: Handle incoming messages ===
@client.on(events.NewMessage(incoming=True))
async def handle_incoming_message(event):
    try:
        # Get sender information
        sender = await event.get_sender()
        sender_name = sender.first_name if sender.first_name else "Someone"
        sender_id = sender.id
        
        # Get message content
        user_message = event.message.message
        
        # Log the incoming message
        logger.info(f"📩 Message from {sender_name} (ID: {sender_id}): {user_message}")
        
        # Skip if it's our own message
        if sender_id == (await client.get_me()).id:
            return
        
        # Generate AI reply
        ai_reply = generate_ai_reply(user_message, sender_name)
        
        # Send the reply
        await event.reply(ai_reply)
        logger.info(f"✅ Reply sent to {sender_name}")
        
    except Exception as e:
        logger.error(f"❌ Error handling message: {e}")

# === Event Listener: Handle edited messages ===
@client.on(events.MessageEdited(incoming=True))
async def handle_edited_message(event):
    try:
        sender = await event.get_sender()
        sender_name = sender.first_name if sender.first_name else "Someone"
        user_message = event.message.message
        
        logger.info(f"✏️ Edited message from {sender_name}: {user_message}")
        
        # Generate AI reply for edited message
        ai_reply = generate_ai_reply(f"(Edited) {user_message}", sender_name)
        await event.reply(ai_reply)
        
    except Exception as e:
        logger.error(f"❌ Error handling edited message: {e}")

# === Start the bot ===
async def start_bot():
    logger.info("🚀 Starting AutoBot with Google Gemini AI...")
    
    # Check if Gemini API key is configured
    if GEMINI_API_KEY == "your_gemini_api_key_here":
        logger.error("❌ Please configure your Gemini API key in config.py")
        return
    
    try:
        await client.start()
        me = await client.get_me()
        logger.info(f"✅ Logged in as: {me.first_name} (@{me.username})")
        logger.info("🤖 AutoBot is now live and ready to respond!")
        logger.info("📱 The bot will automatically reply to incoming messages using Gemini AI")
        
        # Keep the bot running
        await client.run_until_disconnected()
        
    except Exception as e:
        logger.error(f"❌ Failed to start bot: {e}")

# === Main execution ===
if __name__ == '__main__':
    import asyncio
    asyncio.run(start_bot()) 