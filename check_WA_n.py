from yowsup.demos.zclient.views import RecentChatsView
from yowsup.demos.zclient.utils import Helpers

class WhatsAppNotificationListener(RecentChatsView):
    def onMessageReceived(self, messageId, jid, messageContent, timestamp, wantsReceipt, pushName, isBroadcast):
        # Print the sender's name if a new message arrives
        print("New message from:", pushName)

# Phone number and password for authentication
phone_number = "YOUR_PHONE_NUMBER"
password = "YOUR_PASSWORD"

# Initialize the WhatsApp client
client = Helpers.createClient(phone_number, password, WhatsAppNotificationListener)
client.connect()

# Start listening for new messages
client.startListener()
