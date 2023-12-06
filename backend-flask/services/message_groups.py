from datetime import datetime, timedelta, timezone

# Create a class for fetching message groups
class MessageGroups:
    # Define a method within the class
    def run(user_handle):
        # Initialize a dictionary to store errors and data
        model = {
            'errors': None,
            'data': None
        }

        # Get the current time in UTC and convert it to the local time zone
        now = datetime.now(timezone.utc).astimezone()

        # Define a list of message group results
        results = [
            {
                'uuid': '24b95582-9e7b-4e0a-9ad1-639773ab7552',
                'display_name': 'Tai Bui',
                'handle':  'taibui',
                'created_at': now.isoformat()
            },
            {
                'uuid': '417c360e-c4e6-4fce-873b-d2d71469b4ac',
                'display_name': 'Worf',
                'handle':  'worf',
                'created_at': now.isoformat()
            }
        ]

        # Set 'data' in the model with the list of message group results
        model['data'] = results

        # Return the model
        return model




### Example of Output
# {
#     'errors': None,
#     'data': [
#         {
#             'uuid': '24b95582-9e7b-4e0a-9ad1-639773ab7552',
#             'display_name': 'Tai Bui',
#             'handle': 'taibui',
#             'created_at': '<timestamp>'
#         },
#         {
#             'uuid': '417c360e-c4e6-4fce-873b-d2d71469b4ac',
#             'display_name': 'Worf',
#             'handle': 'worf',
#             'created_at': '<timestamp>'
#         }
#     ]
# }
