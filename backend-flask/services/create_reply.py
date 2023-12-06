# Import necessary modules
import uuid
from datetime import datetime, timedelta, timezone

# Create a class for creating replies
class CreateReply:
    # Define a method within the class
    def run(message, user_handle, activity_uuid):
        # Initialize a dictionary to store errors and data
        model = {
            'errors': None,
            'data': None
        }

        # Validate user handle
        if user_handle == None or len(user_handle) < 1:
            # If user handle is blank, set an error
            model['errors'] = ['user_handle_blank']

        # Validate activity UUID
        if activity_uuid == None or len(activity_uuid) < 1:
            # If activity UUID is blank, set an error
            model['errors'] = ['activity_uuid_blank']

        # Validate message
        if message == None or len(message) < 1:
            # If message is blank, set an error
            model['errors'] = ['message_blank'] 
        elif len(message) > 1024:
            # If message exceeds the maximum allowed characters, set an error
            model['errors'] = ['message_exceed_max_chars'] 

        # Check if there are any errors
        if model['errors']:
            # If there are errors, set 'data' in the model with user handle, display name, message, and reply-to activity UUID
            model['data'] = {
                'display_name': 'Tai Bui',
                'handle':  user_handle,
                'message': message,
                'reply_to_activity_uuid': activity_uuid
            }
        else:
            # If no errors, generate a UUID and set additional data for the reply
            now = datetime.now(timezone.utc).astimezone()
            model['data'] = {
                'uuid': uuid.uuid4(),
                'display_name': 'Tai Bui',
                'handle':  user_handle,
                'message': message,
                'created_at': now.isoformat(),
                'reply_to_activity_uuid': activity_uuid
            }

        # Return the constructed model
        return model




### Example of Input
# message = "Thanks for sharing!"
# user_handle = "jane_smith"
# activity_uuid = "123e4567-e89b-12d3-a456-426614174001"

### Example of Output (no errors)
# {
#     'errors': None,
#     'data': {
#         'uuid': <generated_uuid>,
#         'display_name': 'Tai Bui',
#         'handle':  'jane_smith',
#         'message': 'Thanks for sharing!',
#         'created_at': <current_datetime_in_isoformat>,
#         'reply_to_activity_uuid': '123e4567-e89b-12d3-a456-426614174001'
#     }
# }

### Example of Output (with errors)
# {
#     'errors': ['user_handle_blank'],
#     'data': {
#         'display_name': 'Tai Bui',
#         'handle': None,
#         'message': 'Thanks for sharing!',
#         'reply_to_activity_uuid': '123e4567-e89b-12d3-a456-426614174001'
#     }
# }
