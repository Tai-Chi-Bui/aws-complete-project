# Import necessary modules from Flask and other libraries
from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
import os

# Import various services from custom modules
from services.home_activities import *
from services.user_activities import *
from services.create_activity import *
from services.create_reply import *
from services.search_activities import *
from services.message_groups import *
from services.messages import *
from services.create_message import *
from services.show_activity import *

# Create a Flask web application
app = Flask(__name__)

# Fetch frontend and backend URLs from environment variables
frontend = os.getenv('FRONTEND_URL')
backend = os.getenv('BACKEND_URL')

# Define allowed origins for CORS
origins = [frontend, backend]

# Enable CORS for the app with specific configurations
cors = CORS(
  app, 
  resources={r"/api/*": {"origins": origins}},
  expose_headers="location,link",
  allow_headers="content-type,if-modified-since",
  methods="OPTIONS,GET,HEAD,POST"
)

# Define a route to fetch message groups
@app.route("/api/message_groups", methods=['GET'])
def data_message_groups():
  # Set a default user handle for fetching message groups
  user_handle = 'andrewbrown'
  # Run the MessageGroups service to get data model
  model = MessageGroups.run(user_handle=user_handle)
  # Check for errors in the data model
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200

# Define a route to fetch messages for a specific user
@app.route("/api/messages/@<string:handle>", methods=['GET'])
def data_messages(handle):
  # Set a default user sender handle for fetching messages
  user_sender_handle = 'andrewbrown'
  # Get the user receiver handle from the query parameters
  user_receiver_handle = request.args.get('user_reciever_handle')
  # Run the Messages service to get data model
  model = Messages.run(user_sender_handle=user_sender_handle, user_receiver_handle=user_receiver_handle)
  # Check for errors in the data model
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200

# Define a route to create a new message
@app.route("/api/messages", methods=['POST','OPTIONS'])
@cross_origin()
def data_create_message():
  # Set a default user sender handle for creating a message
  user_sender_handle = 'andrewbrown'
  # Get user receiver handle and message from JSON request
  user_receiver_handle = request.json['user_receiver_handle']
  message = request.json['message']
  # Run the CreateMessage service to get data model
  model = CreateMessage.run(message=message, user_sender_handle=user_sender_handle, user_receiver_handle=user_receiver_handle)
  # Check for errors in the data model
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200

# Define a route to fetch home activities
@app.route("/api/activities/home", methods=['GET'])
def data_home():
  # Run the HomeActivities service to get data model
  data = HomeActivities.run()
  return data, 200

# Define a route to fetch activities for a specific user
@app.route("/api/activities/@<string:handle>", methods=['GET'])
def data_handle(handle):
  # Run the UserActivities service to get data model
  model = UserActivities.run(handle)
  # Check for errors in the data model
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200

# Define a route to search activities based on a term
@app.route("/api/activities/search", methods=['GET'])
def data_search():
  # Get the search term from query parameters
  term = request.args.get('term')
  # Run the SearchActivities service to get data model
  model = SearchActivities.run(term)
  # Check for errors in the data model
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200

# Define a route to create a new activity
@app.route("/api/activities", methods=['POST','OPTIONS'])
@cross_origin()
def data_activities():
  # Set a default user handle for creating an activity
  user_handle = 'andrewbrown'
  # Get message and time-to-live (TTL) from JSON request
  message = request.json['message']
  ttl = request.json['ttl']
  # Run the CreateActivity service to get data model
  model = CreateActivity.run(message, user_handle, ttl)
  # Check for errors in the data model
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200

# Define a route to fetch details of a specific activity
@app.route("/api/activities/<string:activity_uuid>", methods=['GET'])
def data_show_activity(activity_uuid):
  # Run the ShowActivity service to get data model
  data = ShowActivity.run(activity_uuid=activity_uuid)
  return data, 200

# Define a route to create a reply to a specific activity
@app.route("/api/activities/<string:activity_uuid>/reply", methods=['POST','OPTIONS'])
@cross_origin()
def data_activities_reply(activity_uuid):
  # Set a default user handle for creating a reply
  user_handle = 'andrewbrown'
  # Get message from JSON request
  message = request.json['message']
  # Run the CreateReply service to get data model
  model = CreateReply.run(message, user_handle, activity_uuid)
  # Check for errors in the data model
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200

# Run the Flask application if the script is executed directly
if __name__ == "__main__":
  app.run(debug=True)
