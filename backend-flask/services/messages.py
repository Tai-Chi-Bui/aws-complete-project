from datetime import datetime, timezone

# Create a class for fetching messages
class Messages:
    # Define a method within the class
    def run(user_sender_handle, user_receiver_handle):
        # Initialize a dictionary to store errors and data
        model = {
            'errors': None,
            'data': None
        }

        # Get the current time in UTC and convert it to the local time zone
        now = datetime.now(timezone.utc).astimezone()

        # Define a list of message results
        results = [
            {
                'uuid': '4e81c06a-db0f-4281-b4cc-98208537772a',
                'display_name': 'Tai Bui',
                'handle':  'taibui',
                'message': 'Cloud is fun!',
                'created_at': now.isoformat()
            },
            {
                'uuid': '66e12864-8c26-4c3a-9658-95a10f8fea67',
                'display_name': 'Tai Bui',
                'handle':  'taibui',
                'message': 'This platform is great!',
                'created_at': now.isoformat()
            }
        ]

        # Set 'data' in the model with the list of message results
        model['data'] = results

        # Return the model
        return model



### Example of Output
# {
#     'errors': None,
#     'data': [
#         {
#             'uuid': '4e81c06a-db0f-4281-b4cc-98208537772a',
#             'display_name': 'Tai Bui',
#             'handle': 'taibui',
#             'message': 'Cloud is fun!',
#             'created_at': '<timestamp>'
#         },
#         {
#             'uuid': '66e12864-8c26-4c3a-9658-95a10f8fea67',
#             'display_name': 'Tai Bui',
#             'handle': 'taibui',
#             'message': 'This platform is great!',
#             'created_at': '<timestamp>'
#         }
#     ]
# }
