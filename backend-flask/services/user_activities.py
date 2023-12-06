from datetime import datetime, timedelta, timezone

# Create a class for fetching user activities
class UserActivities:
    # Define a method within the class
    def run(user_handle):
        # Initialize a dictionary to store errors and data
        model = {
            'errors': None,
            'data': None
        }

        # Get the current time in UTC and convert it to the local time zone
        now = datetime.now(timezone.utc).astimezone()

        # Check if the user handle is blank
        if user_handle == None or len(user_handle) < 1:
            model['errors'] = ['blank_user_handle']
        else:
            # Get the current time again (this line is unnecessary, as 'now' was already defined)
            now = datetime.now()
            
            # Define a list of user activity results
            results = [{
                'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
                'handle':  'Tai Bui',
                'message': 'Cloud is fun!',
                'created_at': (now - timedelta(days=1)).isoformat(),
                'expires_at': (now + timedelta(days=31)).isoformat()
            }]

            # Set 'data' in the model with the list of user activity results
            model['data'] = results

        # Return the model
        return model



### Example of Input
# user_handle_input = "taibui"

### Example of Output
# {
#     'errors': None,
#     'data': [
#         {
#             'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
#             'handle': 'Tai Bui',
#             'message': 'Cloud is fun!',
#             'created_at': '<timestamp_1_day_ago>',
#             'expires_at': '<timestamp_in_31_days>'
#         }
#     ]
# }
