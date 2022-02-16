#Github.com/Vasusen-code

import os
from .. import bot as Drone
from telethon import events, Button

from ethon.mystarts import start_srb
    
S = "Send me Link of any message to clone it here, For private channels sent its invite link first and then send message link, which is needed to forward. \n if it is public channel,then invite link not needed. Just sent the message link.\n\n To report any issues contact @botthelp. \n\nUse /batch command to upload many files with a single link. \nCredits: Mahesh chouhan"

@Drone.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply(f'{S}', 
                      buttons=[
                              [Button.inline("Set thumbnail", data="set"),
                               Button.inline("Delete thumbnail", data="rem")]
                              ])
    try:
        await Bot.start()
        await userbot.start()
        await idle()
    except Exception as e:
        if 'Client is already connected' in str(e):
            pass
        else:
            return

@Drone.on(events.callbackquery.CallbackQuery(data="set"))
async def sett(event):    
    Drone = event.client                    
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await event.delete()
    async with Drone.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("Send me any image for thumbnail as a `reply` to this message.", buttons=Button.force_reply()) 
        x = await conv.get_reply()
        if not x.media:
            xx.edit("No media found.")
        mime = x.file.mime_type
        if not 'png' in mime:
            if not 'jpg' in mime:
                if not 'jpeg' in mime:
                    return await xx.edit("No image found.")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'Trying.')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("Temporary thumbnail saved!")
        
@Drone.on(events.callbackquery.CallbackQuery(data="rem"))
async def remt(event):  
    Drone = event.client            
    await event.edit('Trying.')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('Removed!')
    except Exception:
        await event.edit("No thumbnail saved.")                        
  

    
