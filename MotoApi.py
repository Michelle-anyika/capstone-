# TODO: Import required modules for basic authentication (hint: you'll need base64)
# TODO: Import required modules for API documentation (hint: look into apispec and yaml)
import urllib.parse
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# TODO: Set up API documentation spec
# TASK 1: Create an APISpec instance with:
# - title: "Moto Taxi API"
# - version: "1.0.0" 
# - openapi_version: "3.0.2"
# - description: "API for managing Moto Taxi riders and rides"
# - servers: [{"url": "http://localhost:8888"}]
# - Include MarshmallowPlugin for schema handling

# In-memory database
# TODO: Create a USERS dictionary for authentication
# TASK 2: Implement user storage with the following users:
# - "admin": password "password123", role "admin"
# - "user": password "userpass", role "user" 
# - "demo": password "demo123", role "user"

# TODO: Add security scheme to API spec
# TASK 3: Add BasicAuth security scheme to the spec using:
# spec.components.security_scheme("BasicAuth", {...})

# moto taxi riders
riders = [
    {"id": 1, "name": "James", "location": "Nyamirambo", "is_available": True},
    {"id": 2, "name": "Bob", "location": "Remera", "is_available": False},
    {"id": 3, "name": "Charlie", "location": "Kicukiro", "is_available": True},
    {"id": 4, "name": "David", "location": "KCC", "is_available": True},
    {"id": 5, "name": "Eve", "location": "Nyabugogo", "is_available": True},
    {"id": 6, "name": "Frank", "location": "Downtown", "is_available": False},
    {"id": 7, "name": "Graham", "location": "Kanombe", "is_available": True},
    {"id": 8, "name": "Hannah", "location": "Kimironko", "is_available": True}
]


class APIHandler(BaseHTTPRequestHandler):

    @staticmethod
    def _authenticate():
        """Check if the request has valid Basic Authentication credentials"""
        # TODO: TASK 4 - Implement Basic Authentication
        # Steps to implement:
        # 1. Get the 'Authorization' header from self.headers
        # 2. Check if it starts with 'Basic '
        # 3. Extract and decode the base64 encoded credentials (hint: use base64.b64decode)
        # 4. Split the decoded string on ':' to get username and password
        # 5. Verify credentials against the USERS dictionary
        # 6. Return user info dict with username and role if valid, None if invalid
        # 7. Handle exceptions for malformed credentials
        
        # HINT: Authorization header format is "Basic <base64-encoded-username:password>"
        # HINT: Use try-except to handle ValueError and UnicodeDecodeError
        
        return None  # Replace this with your implementation

    @staticmethod
    def _require_auth():
        """Return True if authentication is required for this endpoint"""
        # TODO: TASK 5 - Implement authentication requirement logic
        # Steps:
        # 1. Parse the request path using urllib.parse.urlparse
        # 2. Define public endpoints that don't require auth: ['/', '/health', '/openapi.json', '/openapi.yaml']
        # 3. Return True if the path is NOT in public endpoints, False otherwise
        
        return False  # Replace this with your implementation

    def _send_auth_required(self):
        """Send 401 Unauthorized with WWW-Authenticate header"""
        # TODO: TASK 6 - Implement 401 Unauthorized response
        # Steps:
        # 1. Send 401 status code
        # 2. Set Content-type header to 'application/json'
        # 3. Set WWW-Authenticate header to 'Basic realm="Moto Taxi API"'
        # 4. Set CORS header 'Access-Control-Allow-Origin' to '*'
        # 5. End headers and send JSON error response
        # Response format: {"error": "Unauthorized", "message": "Basic authentication required"}
        
        pass  # Replace this with your implementation

    def _send_response(self, status_code, data):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def do_get(self):
        # TODO: TASK 7 - Implement authentication check
        # Steps:
        # 1. Check if authentication is required using _require_auth()
        # 2. If required, call _authenticate() to get user info
        # 3. If authentication fails (user is None), call _send_auth_required() and return
        
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path

        # TODO: TASK 8 - Add OpenAPI documentation endpoints
        # Add endpoints for '/openapi.json' and '/openapi.yaml'
        # For JSON: return spec.to_dict() with 200 status
        # For YAML: set content-type to 'text/yaml' and return yaml.dump(spec.to_dict())

        if path == '/':
            self._send_response(200, {"message": "Moto Taxi API"})
        elif path == '/riders':
            self._send_response(200, riders)
        elif path.startswith('/riders/'):
            route_part = path.split('/')[-1]
            if route_part == 'available':
                available_riders = [rider for rider in riders if rider['is_available']]
                self._send_response(200, available_riders)
            else:
                rider_id = int(route_part)
                rider = next((rider for rider in riders if rider['id'] == rider_id), None)
                if rider:
                    self._send_response(200, rider)
                else:
                    self._send_response(404, {"message": "Rider not found"})
        elif path == '/health':
            self._send_response(200, {"status": "OK"})
        else:
            self._send_response(404, {"message": "Not Found"})

# TODO: TASK 9 - Add API documentation for the root endpoint
# Use spec.path() to document the '/' endpoint with:
# - GET operation
# - Summary: 'Moto Taxi API'  
# - 200 response with example: {"message": "Moto Taxi API"}
# - Proper schema definition for the response

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8888), APIHandler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()