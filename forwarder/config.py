from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "6236974671:AAHpKETTm-MufNooU59AJrtnclUNgLJjZG4"  # Your bot API key
    OWNER_ID = 862271564  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    
    FROM_CHATS = [-1001192743751]# List of chat id's to forward messages from.
    TO_CHATS = [-1001240181567,-1001741279076,-1001684632059,-1001703245432,-1001640996330,-1001715704828,-1001713522142,-1001796119329]# List of chat id's to forward messages to.

    REMOVE_TAG = False
    WORKERS = 16
   
    
