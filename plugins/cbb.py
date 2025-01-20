from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = """
╭───────────⋗
├⋗<b> ᴍʏ ɴᴀᴍᴇ</b> : <a href=https://t.me/Sand_Store_bot>˹sαɳԃ 友 sƚσɾҽ˼</a> 
├⋗<b> ᴅᴇᴠᴇʟᴏᴘᴇʀ</b> : <a href=http://t.me/SAJIIDFF>亗 ᏚᎪᎫⵊᎠ ƑƑ</a> 
├⋗<b> ʟɪʙʀᴀʀʏ</b> : <a href=https://github.com/pyrogram>ᴘʏʀᴏɢʀᴀᴍ</a>
├⋗<b> ʟᴀɴɢᴜᴀɢᴇ</b> : <a href=https://www.python.org>ᴘʏᴛʜᴏɴ 𝟹</a>     
╰─────────────────⋗
""", 
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
