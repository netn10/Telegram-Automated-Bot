# In order to use inline bot messages, follow this:
# 1. Create the inline message with the photo, caption, buttons, etc.
# 2. Forward the message from the bot to yourself.
# 3. Use this url: https://api.telegram.org/<TOKEN>/getUpdates 
# 4. On the bottom of the page, search for the last message, and copy the message_id and the id to from_chat_id and message_id of this script.
# 5. Check example.bmp for a visual explenation of the last point.

TOKEN = "1065279137:AAGK1WOL1ugdJNEI--lo_uxbsraDzs5YHFc"

ALL_INFO = [
    #{'chat_id' : "-373962624", "type": "photo", "time_to_wait": 0.1, 'msg': "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Google_Chrome_icon_%28September_2014%29.svg/1200px-Google_Chrome_icon_%28September_2014%29.svg.png&caption=חולצה 3ב10"},
    #{'chat_id' : "-373962624", "type": "text", "time_to_wait": 0.1, 'msg': "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1553186467-hanes-1553186375.jpg?crop=1xw:1xh;center,top&resize=480:*"},
    {'chat_id' : "-373962624", "type": "post", "time_to_wait": 2, 'msg' : '&from_chat_id=856757580&message_id=463'},
]