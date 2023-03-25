from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "6256825136:AAG8JlB2zE_Ujlx5eHVMjEs8XUZPx322YS8"  # Your bot API key
    OWNER_ID = 862271564  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    
    FROM_CHATS = [-1001195952402]# List of chat id's to forward messages from.
    TO_CHATS = [-1001129438703,-1001759216384,-1001730754559,-1001573532147,-1001704363633,-1001787193837,-1001554668793,-1001612158871]# List of chat id's to forward messages to.

    REMOVE_TAG = True
    WORKERS = 16
   
    
