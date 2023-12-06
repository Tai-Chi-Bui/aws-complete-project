from datetime import datetime, timezone

# Create a class for searching activities
class SearchActivities:
    # Define a method within the class
    def run(search_term):
        # Initialize a dictionary to store errors and data
        model = {
            'errors': None,
            'data': None
        }

        # Get the current time in UTC and convert it to the local time zone
        now = datetime.now(timezone.utc).astimezone()

        # Check if the search term is blank
        if search_term == None or len(search_term) < 1:
            model['errors'] = ['search_term_blank']
        else:
            # Define a list of search results
            results = [{
                'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
                'handle':  'Tai Bui',
                'message': 'Cloud is fun!',
                'created_at': now.isoformat()
            }]

            # Set 'data' in the model with the list of search results
            model['data'] = results

        # Return the model
        return model



### Example of Input
#search_term_input = "cloud"

### Example of Output
# {
#     'errors': None,
#     'data': [
#         {
#             'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
#             'handle': 'Tai Bui',
#             'message': 'Cloud is fun!',
#             'created_at': '<timestamp>'
#         }
#     ]
# }
