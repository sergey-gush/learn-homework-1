import logging
import settings
from datetime import date
import ephem
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, CallbackContext

logging.basicConfig(
    filename='bot.log',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

consts = {
    'Aries': 'Овен', 
    'Taurus': 'Телец',
    'Gemini': 'Близнецы',
    'Cancer': 'Рак',
    'Leo': 'Лев',
    'Virgo': 'Дева',
    'Libra': 'Весы',
    'Scorpius': 'Скорпион',
    'Sagittarius': 'Стрелец',
    'Capricornus': 'Козерог',
    'Aquarius': 'Водолей',
    'Pisces': 'Рыбы'
}

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print('/start')
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def planets(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    text = update.message.text.split()
    planet_name = text[1]
    today = date.today()
    planet = getattr(ephem, planet_name)
    planet_today = planet(today)
    print(planet_today)
    planet_const = ephem.constellation(planet_today)
    await update.message.reply_text(f'The {planet_name} is in the constellation {planet_const[1]}')
    

async def talk_to_me(update: Update, context: CallbackContext):
    text = update.message.text
    print(text)
    await update.message.reply_text(text)

def main():
    mybot = ApplicationBuilder().token(settings.API_KEY).build()

    start_handler = CommandHandler('start', hello)
    planet_handler = CommandHandler('planet', planets)
    msg_handler = MessageHandler(filters.TEXT, talk_to_me)
    mybot.add_handler(start_handler)
    mybot.add_handler(planet_handler)
    mybot.add_handler(msg_handler)

    logging.info('Started')
    mybot.run_polling()

if __name__ == '__main__':
    main()

