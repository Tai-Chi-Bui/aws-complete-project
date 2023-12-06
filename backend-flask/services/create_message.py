# Import necessary modules
import uuid
from datetime import datetime, timedelta, timezone

# Create a class for creating messages
class CreateMessage:
    # Define a method within the class
    def run(message, user_sender_handle, user_receiver_handle):
        # Initialize a dictionary to store errors and data
        model = {
            'errors': None,
            'data': None
        }

        # Validate user sender handle
        if user_sender_handle == None or len(user_sender_handle) < 1:
            # If user sender handle is blank, set an error
            model['errors'] = ['user_sender_handle_blank']

        # Validate user receiver handle
        if user_receiver_handle == None or len(user_receiver_handle) < 1:
            # If user receiver handle is blank, set an error
            model['errors'] = ['user_receiver_handle_blank']

        # Validate message
        if message == None or len(message) < 1:
            # If message is blank, set an error
            model['errors'] = ['message_blank'] 
        elif len(message) > 1024:
            # If message exceeds the maximum allowed characters, set an error
            model['errors'] = ['message_exceed_max_chars'] 

        # Check if there are any errors
        if model['errors']:
            # If there are errors, set 'data' in the model with user sender handle, display name, and message
            model['data'] = {
                'display_name': 'Tai Bui',
                'handle':  user_sender_handle,
                'message': message
            }
        else:
            # If no errors, generate a UUID and set additional data for the message
            now = datetime.now(timezone.utc).astimezone()
            model['data'] = {
                'uuid': uuid.uuid4(),
                'display_name': 'Tai Bui',
                'handle':  user_sender_handle,
                'message': message,
                'created_at': now.isoformat()
            }

        # Return the constructed model
        return model





### Example of Input
# message = "Hey there! How are you?"
# user_sender_handle = "john_doe"
# user_receiver_handle = "jane_smith"


### Example of Output (no errors)
# {
#     'errors': None,
#     'data': {
#         'uuid': <generated_uuid>,
#         'display_name': 'Tai Bui',
#         'handle':  'john_doe',
#         'message': 'Hey there! How are you?',
#         'created_at': <current_datetime_in_isoformat>
#     }
# }


### Example of Output (with errors)
# {
#     'errors': ['user_sender_handle_blank'],
#     'data': {
#         'display_name': 'Tai Bui',
#         'handle': 'john_doe',
#         'message': 'Hey there! How are you?'
#     }
# }


