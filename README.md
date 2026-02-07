Moto Taxi API - capstone
Project Overview
This project is designed to help you learn web API development, authentication, and documentation. You'll work in groups to implement a comprehensive RESTful API for a Motor Taxi service, complete with proper authentication and OpenAPI documentation.

Group Guidelines
Discussion: Monday - be prepared to discuss your implementation and demonstrate your API
Submission: Submit your completed api.py file and a brief group reflection document
Getting Started
Prerequisites
Python 3.9+
Basic understanding of HTTP methods and REST APIs
Familiarity with JSON data format
Setup Instructions
Clone this repository
Create a virtual environment:
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
Install dependencies (you'll need to complete requirements.txt first):
pip install -r requirements.txt
Run the server:
python api.py
Test the API at http://localhost:8888
Tasks Overview

### Phase 1: Foundation Setup
Tasks 1-3: Project Dependencies and Documentation Setup

### Phase 2: Authentication System
Tasks 4-7: Implement Basic HTTP Authentication

### Phase 3: API Documentation
Tasks 8-9: Add OpenAPI/Swagger Documentation

Phase 4: New Resource Implementation
Tasks 10-12: Create Passengers Resource

Detailed Task Instructions
TASK 1: Install Required Dependencies
Assigned to: Entire group (setup meeting)

Complete the requirements.txt file with these packages:

apispec==6.8.4 - for OpenAPI specification generation
marshmallow==4.0.1 - for schema serialization
packaging==25.0 - dependency for apispec
PyYAML==6.0.2 - for YAML format support
TASK 2: Set up API Documentation Spec
Assigned to: Documentation Lead

In api.py, create an APISpec instance with:

Title: "Moto Taxi API"
Version: "1.0.0"
OpenAPI version: "3.0.2"
Description: "API for managing Moto Taxi riders, passengers, and rides"
Servers: [{"url": "http://localhost:8888"}]
Include MarshmallowPlugin for schema handling
Success Criteria: APISpec object is properly initialized

TASK 3: Create a User Authentication System
Assigned to: Security Lead

Create a USERS dictionary with these test accounts:

"admin": password "password123", role "admin"
"user": password "userpass", role "user"
"demo": password "demo123", role "user"
Add BasicAuth security scheme to your APISpec.

Success Criteria: Users dictionary is properly structured

TASK 4: Implement Basic Authentication
Assigned to: Security Lead + Backend Developer

Complete the _authenticate(self) method:

Extract the Authorization header
Verify it starts with "Basic."
Decode the base64 credentials
Split on: to get username/password
Validate against the USERS dictionary
Return user info dict or None
Handle exceptions properly
Success Criteria: Method correctly authenticates valid users and rejects invalid ones

TASK 5: Implement Authorization Logic
Assigned to: Security Lead

Complete the _require_auth(self) method:

Public endpoints (no auth required): ['/', '/health', '/openapi.json', '/openapi.yaml']
All other endpoints require authentication
Return True if auth is required, False otherwise
Success Criteria: Public endpoints accessible, protected endpoints require auth

TASK 6: Handle Unauthorized Requests
Assigned to: Backend Developer

Complete the _send_auth_required(self) method:

Send 401 status code
Set Content-type header to application/json
Set WWW-Authenticate header to Basic realm="Moto Taxi API"
Set CORS header
Send JSON error response
Success Criteria: Returns proper 401 response with correct headers

TASK 7: Integrate Authentication Flow
Assigned to: Backend Developer

In the do_GET() method:

Check if the endpoint requires authentication
If yes, authenticate the user
If authentication fails, send a 401 response
Success Criteria: Protected endpoints require valid credentials

TASK 8: Add Documentation Endpoints
Assigned to: Documentation Lead

Add these endpoints to do_GET():

GET /openapi.json - Return spec.to_dict()
GET /openapi.yaml - Return YAML format with proper content-type
Success Criteria: Both endpoints return valid OpenAPI documentation

TASK 9: Document Existing Endpoints
Assigned to: Documentation Lead + API Developer

Use spec.path() to document:

Root endpoint /
All rider endpoints (/riders, /riders/{id}, /riders/available)
Include proper schemas, examples, and response codes.

Success Criteria: All endpoints have complete OpenAPI documentation

PHASE 4: NEW RESOURCE - PASSENGERS
TASK 10: Create Passengers Data Model
Assigned to: API Developer

Create a passengers list with sample data:

passengers = [
    {
        "id": 1,
        "name": "John",
        "Phone": "+25078123456",
        "location": "Kimironko",
        "rating": 4.5
    },
    {
        "id": 2,
        "name": "Jane",
        "Phone": "+25078987654",
        "location": "Kigali Downtown",
        "rating": 4.5
    },
    {
        "id": 3,
        "name": "Jill",
        "Phone": "+25078123456",
        "location": "Nyamirambo",
        "rating": 4.5
    }
]
TASK 11: Implement Passengers Endpoints
Assigned to: API Developer + Backend Developer

Add these protected endpoints to do_GET():

GET /passengers - Return all passengers
GET /passengers/{id} - Return specific passenger by ID
GET /passengers/high-rated - Return passengers with rating >= 4.5
Success Criteria: All passenger endpoints work correctly and require authentication

TASK 12: Document Passengers API
Assigned to: Documentation Lead

Add complete OpenAPI documentation for all passenger endpoints including:

Request/response schemas
Error responses (404, 401)
Examples
Parameter descriptions
Success Criteria: Passenger endpoints fully documented in OpenAPI spec

Testing Your Implementation
Manual Testing Checklist
Authentication Tests:

 Access public endpoints without credentials
 Access protected endpoints without credentials (should return 401)
 Access protected endpoints with invalid credentials (should return 401)
 Access protected endpoints with valid credentials (should work)
API Functionality Tests:

 GET / - API welcome message
 GET /health - Health check
 GET /riders - List all riders (requires auth)
 GET /riders/1 - Get specific rider (requires auth)
 GET /riders/available - Get available riders (requires auth)
 GET /passengers - List all passengers (requires auth)
 GET /passengers/1 - Get specific passenger (requires auth)
 GET /passengers/high-rated - Get high-rated passengers (requires auth)
Documentation Tests:

 GET /openapi.json - Returns a valid JSON schema
 GET /openapi.yaml - Returns valid YAML schema
 Visit the schema in Swagger UI or a similar tool
Testing Commands
# Test public endpoints
curl [http://localhost:8888/](http://localhost:8888/) curl [http://localhost:8888/health](http://localhost:8888/health)
# Test protected endpoints (should fail)
curl [http://localhost:8888/riders](http://localhost:8888/riders)
# Test with authentication (should work)
curl -u admin:password123 [http://localhost:8888/riders](http://localhost:8888/riders) curl -u user:userpass [http://localhost:8888/passengers](http://localhost:8888/passengers)
# Test documentation
curl [http://localhost:8888/openapi.json](http://localhost:8888/openapi.json) curl [http://localhost:8888/openapi.yaml](http://localhost:8888/openapi.yaml)
Bonus Challenges (Optional)
If your group finishes early, try these advanced features:

Role-Based Access Control: Implement different permissions for admin vs user roles
POST/PUT/DELETE Methods: Add endpoints to create, update, and delete passengers
Data Validation: Add input validation for passenger data
Search Functionality: Add /passengers/search?location=Kigali endpoint
API Rate Limiting: Implement basic rate limiting for API calls
Getting Help
Stuck on a task? Check with your group first, then ask your coaches for help
Authentication not working? Review HTTP Basic Auth specifications
Documentation issues? Check OpenAPI 3.0 specification docs
Testing problems? Use curl commands or Postman for debugging
