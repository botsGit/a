from pyrogram import filters
from pyrogram import Client as MT_ID_Bot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from MT_ID_Bot.Translation import Translation
from MT_ID_Bot.Config import Config

UPDATE_CHANNEL=Config.UPDATE_CHANNEL # Update Channel Forces Subscribe
BOT_USERNAME=Config.BOT_USERNAME # ReStart Option 
JOIN=Translation.JOIN_TEXT # Button Text (Update Channel)
TRY=Translation.TRY_TEXT # Button Text (Update Channel)
SUB_TEXT=Translation.FSUB_TEXT # FSUB Information Text

@MT_ID_Bot.on_message(filters.private & filters.forwarded)
async def info(motech, msg):
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await motech.get_chat_member(update_channel, msg.chat.id)
            if user.status == "kicked out":
               await update.reply_text("š Sorry Dude, You are **š±ļøš°ļøš½ļøš½ļøš“ļøš³ļø š**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{Channel User Name} To Use Me") From Motech.py
            await msg.reply_text(
                text=f"<b>{SUB_TEXT}</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=f"{JOIN}", url=f"t.me/{UPDATE_CHANNEL}")],
                    [ InlineKeyboardButton(text=f"{TRY}", url=f"https://t.me/{BOT_USERNAME}?start=try")]
              ])
            )
            return
        except Exception:
            await msg.reply_text(f"@{UPDATE_CHANNEL}")
            return
    if msg.forward_from:
        text = "<u>ššØš«š°šš«š šš§ššØš«š¦šš­š¢šØš§ š</u> \n\n"
        if msg.forward_from["is_bot"]:
            text += "<u>š¤ ššØš­ šš§ššØ</u>"
        else:
            text += "<u>š¤šš¬šš« šš§ššØ</u>"
        text += f'\n\nšØāš¼ ššš¦š : {msg.forward_from["first_name"]}'
        if msg.forward_from["username"]:
            text += f'\n\nš šš¬šš«ššš¦š : @{msg.forward_from["username"]} \n\nš ID : <code>{msg.forward_from["id"]}</code>'
        else:
            text += f'\n\nš šš : `{msg.forward_from["id"]}`'
        await msg.reply(text, quote=True)
    else:
        hidden = msg.forward_sender_name
        if hidden:
            await msg.reply(
                f"āļøšš«š«šØš« <b><i>{hidden}</i></b> āļøšš«š«šØš«",
                quote=True,
            )
        else:
            text = f"<u>ššØš«š°šš«š šš§ššØš«š¦šš­š¢šØš§ š</u>.\n\n"
            if msg.forward_from_chat["type"] == "channel":
                text += "<u>š¢ šš”šš§š§šš„</u>"
            if msg.forward_from_chat["type"] == "supergroup":
                text += "<u>š£ļø šš«šØš®š©</u>"
            text += f'\n\nš ššš¦š {msg.forward_from_chat["title"]}'
            if msg.forward_from_chat["username"]:
                text += f'\n\nā”ļø šš«šØš¦ : @{msg.forward_from_chat["username"]}'
                text += f'\n\nš šš : `{msg.forward_from_chat["id"]}`'
            else:
                text += f'\n\nš šš `{msg.forward_from_chat["id"]}`\n\n'
            await msg.reply(text, quote=True)
