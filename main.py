#!/usr/bin/python
#https://github.com/python-telegram-bot/python-telegram-bot

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
from telegram import InlineQueryResultArticle, ChatAction, InputTextMessageContent
import logging, os, platform, time
import Magnet_To_Torrent2, btclient
import configparser, shutil
import utils

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

config = configparser.ConfigParser()
config.read('config.ini')


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"' % (update, error))

def start(bot, update):
    update.message.reply_text('Hello World!')
    chat_id = update.message.chat_id
    update.message.reply_text('Chat id {}'.format(update.message.chat_id))
    if chat_id != 4106334:
        update.message.reply_text('Not allowed')

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))
def prueba(bot, update):
    update.message.reply_text('Esto es una prueba')
    update.message.reply_text(update.message.chat_id)
    bot.send_message(chat_id=update.message.chat_id, text="Hi. I'm sudobot.")

def magnet(bot, update, args):
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    update.message.reply_text('Converting magnet to torrent...')
    print os.environ['TMP']
    Magnet_To_Torrent2.magnet2torrent(args[0], os.environ['TMP'] + '/asd.torrent')
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    time.sleep(1)
    update.message.reply_text('Done')    
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    time.sleep(1)
    update.message.reply_text('Now downloading torrent. This may take a while')
    archivo = btclient.download(os.environ['TMP'] + '/asd.torrent',os.environ['TMP'])
    mypath = os.path.join(os.environ['TMP'] + '/' + archivo)
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    time.sleep(1)
    update.message.reply_text('Downloaded. Now sending file to you...')
    if os.path.isdir(mypath):
        archivos = get_files_by_file_size(mypath)
        bot.send_document(chat_id=update.message.chat_id,document=open(archivos[0], 'rb'))
        shutil.rmtree(mypath)
    else:
        bot.send_document(chat_id=update.message.chat_id,document=open(mypath, 'rb'))
        os.remove(mypath)
def ip(bot, update)
    if update.message.from_user.id != int(config['ADMIN']['id']):
        bot.sendChatAction(chat_id=update.message.chat_id,
                           action=ChatAction.TYPING)
        time.sleep(1)
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="It seems like you aren't allowed to use me. :(")        
    else:
        bot.sendChatAction(chat_id=update.message.chat_id,
                           action=ChatAction.TYPING)
        time.sleep(1)
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="The server current ip is")
        bot.sendChatAction(chat_id=update.message.chat_id,
                           action=ChatAction.TYPING)
        time.sleep(1.5)
         bot.sendMessage(chat_id=update.message.chat_id,text=ipgetter.myip())


def get_files_by_file_size(dirname, reverse=True):
    """ Return list of file paths in directory sorted by file size """

    # Get list of files
    onlyfiles = [f for f in os.listdir(dirname) if os.path.isfile(os.path.join(dirname, f))]

    # Re-populate list with filename, size tuples
    for i in xrange(len(onlyfiles)):
        onlyfiles[i] = (os.path.join(dirname,onlyfiles[i]), os.path.getsize(os.path.join(dirname,onlyfiles[i])))
    # Sort list by file size
    # If reverse=True sort from largest to smallest
    # If reverse=False sort from smallest to largest
    onlyfiles.sort(key=lambda filename: filename[1], reverse=reverse)

    # Re-populate list with just filenames
    for i in xrange(len(onlyfiles)):
        onlyfiles[i] = onlyfiles[i][0]

    return onlyfiles

if platform.system() == 'Linux':
    if not 'TMP' in os.environ:
        os.environ['TMP'] = '/tmp'
updater = Updater(token=config['KEYS']['bot_api'])

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('culo', prueba))
updater.dispatcher.add_handler(CommandHandler('ip', ip))
updater.dispatcher.add_handler(CommandHandler('magnet', magnet, pass_args=True))


updater.start_polling()
updater.idle()
