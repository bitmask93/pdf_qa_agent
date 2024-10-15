from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
class SlackHandler:
	def __init__(self, token):
		self.client = WebClient(token=token)
	
	def post_message_to_slack(self, channel, message):
		'''
			Post messages to Slack Channel

			Input : 
				channel : slack channel name
				message : message to be posted in slack channel
			Output : 

		'''
		try:
		    response = self.client.chat_postMessage(channel=channel, text=message)
		    return response
		except SlackApiError as e:
			print(f"API error: {e.response['error']}")

if __name__ == "__main__":
	slack_token = 'Your Agent Token'
	slack_channel = 'Your slack Channel'
	test_message = "Your Message"

	slack_handler = SlackHandler(token=slack_token)
	response = slack_handler.post_message_to_slack(slack_channel, test_message)
	if(response):
		print("Success")
	else:
		print("Failed to write")