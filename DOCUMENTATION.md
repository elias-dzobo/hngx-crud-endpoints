## Standard formats for requests and responses for each endpoint.

Get all users GET /api This endpoint returns a list of all users.

Request No request body is required.

Response The response body is a JSON array of user objects. Each user
object has the following properties: \* id: The user ID. \* name: The
user's name. \* track: The user's track. JSON \[ { "id": 1, "name":
"John Doe", "track": "Software Engineering" }, { "id": 2, "name": "Jane
Doe", "track": "Data Science" }\]

Get user by ID GET /api/{userID}

This endpoint returns the user with the specified ID.

Request The request path parameter id specifies the user ID.

Response The response body is a JSON object of the user with the
specified ID.

JSON { "id": 1, "name": "John Doe", "track": "Software Engineering" }

Get user by name

GET /api/{name} This endpoint returns the user with the specified name.

Request The request path parameter name specifies the user name.

Response The response body is a JSON object of the user with the
specified name.

JSON { "id": 1, "name": "John Doe", "track": "Software Engineering" }

Create user

POST /api This endpoint creates a new user.

Request The request body is a JSON object with the following properties:
\* name: The user's name. \* track: The user's track. \* JSON { "name":
"John Doe", "track": "Software Engineering" }

Response The response body is a JSON object of the newly created user.
JSON { "id": 1, "name": "John Doe", "track": "Software Engineering" }

Update user PUT /api/{userID} This endpoint updates the user with the
specified ID.

Request The request path parameter id specifies the user ID. The request
body is a JSON object with the properties you want to update.

JSON { "name": "Jane Doe", "Track": "Backend" }

Response The response body is a JSON object of the updated user. JSON {
"id": 1, "name": "Jane Doe", "track": "Backend" }

Delete user DELETE /api{userID} This endpoint deletes the user with the
specified ID.

Request The request path parameter id specifies the user ID.

Response The response body is empty.

Known limitations and assumptions \* The API only supports users with
names and tracks. \* The API does not support authentication or
authorization. \* The API is not fault-tolerant.
