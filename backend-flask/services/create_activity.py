# Import necessary modules
import uuid
from datetime import datetime, timedelta, timezone

# Create a class for creating activities
class CreateActivity:
    # Define a method within the class
    def run(message, user_handle, ttl):
        # Initialize a dictionary to store errors and data
        model = {
            'errors': None,
            'data': None
        }

        # Get the current time in UTC and convert it to the local time zone
        now = datetime.now(timezone.utc).astimezone()

        # Handle Time-to-Live (TTL) based on the provided input
        if (ttl == '30-days'):
            ttl_offset = timedelta(days=30) 
        elif (ttl == '7-days'):
            ttl_offset = timedelta(days=7) 
        elif (ttl == '3-days'):
            ttl_offset = timedelta(days=3) 
        elif (ttl == '1-day'):
            ttl_offset = timedelta(days=1) 
        elif (ttl == '12-hours'):
            ttl_offset = timedelta(hours=12) 
        elif (ttl == '3-hours'):
            ttl_offset = timedelta(hours=3) 
        elif (ttl == '1-hour'):
            ttl_offset = timedelta(hours=1) 
        else:
            # If TTL value is not recognized, set an error
            model['errors'] = ['ttl_blank']

        # Validate user handle
        if user_handle == None or len(user_handle) < 1:
            # If user handle is blank, set an error
            model['errors'] = ['user_handle_blank']

        # Validate message
        if message == None or len(message) < 1:
            # If message is blank, set an error
            model['errors'] = ['message_blank'] 
        elif len(message) > 280:
            # If message exceeds the maximum allowed characters, set an error
            model['errors'] = ['message_exceed_max_chars'] 

        # Check if there are any errors
        if model['errors']:
            # If there are errors, set 'data' in the model with user_handle and message
            model['data'] = {
                'handle':  user_handle,
                'message': message
            }   
        else:
            # If no errors, generate a UUID and set additional data for the activity
            model['data'] = {
                'uuid': uuid.uuid4(),
                'display_name': 'Tai Bui',
                'handle':  user_handle,
                'message': message,
                'created_at': now.isoformat(),
                'expires_at': (now + ttl_offset).isoformat()
            }

        # Return the constructed model
        return model









### Example of Input
# message = "Hello, world!"
# user_handle = "john_doe"
# ttl = "7-days"

### Example of Output
# {
#     'errors': None,
#     'data': {
#         'uuid': <generated_uuid>,
#         'display_name': 'Tai Bui',
#         'handle':  'john_doe',
#         'message': 'Hello, world!',
#         'created_at': <current_datetime_in_isoformat>,
#         'expires_at': <expiration_datetime_in_isoformat>
#     }
# }

