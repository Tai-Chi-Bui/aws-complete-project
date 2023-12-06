from datetime import datetime, timedelta, timezone

# Create a class for showing activities
class ShowActivities:
    # Define a method within the class
    def run(activity_uuid):
        # Get the current time in UTC and convert it to the local time zone
        now = datetime.now(timezone.utc).astimezone()

        # Define a list of activity results
        results = [{
            'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
            'handle':  'Tai Bui',
            'message': 'Cloud is fun!',
            'created_at': (now - timedelta(days=2)).isoformat(),
            'expires_at': (now + timedelta(days=5)).isoformat(),
            'replies': {
                'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
                'handle':  'Worf',
                'message': 'This post has no honor!',
                'created_at': (now - timedelta(days=2)).isoformat()
            }
        }]

        # Return the list of activity results
        return results



### Example of Input
# activity_uuid_input = "68f126b0-1ceb-4a33-88be-d90fa7109eee"

### Example of Ouput
# [
#     {
#         'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
#         'handle':  'Tai Bui',
#         'message': 'Cloud is fun!',
#         'created_at': '<timestamp_2_days_ago>',
#         'expires_at': '<timestamp_in_5_days>',
#         'replies': {
#             'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
#             'handle':  'Worf',
#             'message': 'This post has no honor!',
#             'created_at': '<timestamp_2_days_ago_for_reply>'
#         }
#     }
# ]

