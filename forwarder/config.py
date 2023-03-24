from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "5937920852:AAG3ID9dUNRky3BgjvwaSdF5dXWFGteGYH0"  # Your bot API key
    OWNER_ID = 862271564  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    
    FROM_CHATS = [-1001231558352]# List of chat id's to forward messages from.
    TO_CHATS = [-1001102718567,-1001294920825,-1001368524326,-1001661821275,-1001519174543,-1001584192669,-1001582874261,-1001244586129]# List of chat id's to forward messages to.

    REMOVE_TAG = False
    WORKERS = 16
   
    
