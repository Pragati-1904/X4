from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "5078862900:AAHRoD0gyEBBXyGYjSvRdby2Fl85dwhGy18"  # Your bot API key
    OWNER_ID = 862271564  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    
    FROM_CHATS = [-1001447690970 , -1001331185454]# List of chat id's to forward messages from.
    TO_CHATS = [-1001692624546]# List of chat id's to forward messages to.

    REMOVE_TAG = False
    WORKERS = 16
   
    
