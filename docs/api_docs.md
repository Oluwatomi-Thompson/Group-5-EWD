 API DOCUMENTATION
Mobile Money SMS Transaction REST API
INTRODUCTION
This API is part of a Mobile Money (MoMo) SMS processing system. It provides secure access to transaction records stored in an XML dataset (modified_sms_v2.xml). The API allows clients to perform CRUD operations (Create, Read, Update, Delete) on transaction data.

The system is built using Python’s built-in http.server module and follows RESTful design principles.

2. BASE URL



http://127.0.0.1:8000/transactions

Server running
image
3. AUTHENTICATION & SECURITY
Authentication Method
The API uses Basic Authentication.

Valid Credentials
Username | Password -- | -- admin | momo2025 group5 | password123
4.

2. DATA FORMAT
Each transaction is stored in XML and converted to JSON for API responses.

XML Structure 1 send 5000 A B 2026-05-30

5.

2. API ENDPOINTS (CRUD OPERATIONS)/h1>
5.1 Get all Transactions Endpoint GET /transactions Description

Returns all transaction records from the XML file.

Example Request curl.exe -u admin:momo2025http://127.0.0.1:8000/transactions Example Response (200 OK) [ { "id": 1, "type": "send", "amount": 5000, "sender": "A", "receiver": "B", "timestamp": "2026-05-30" } ] Error Response (401 Unauthorized) { "error": "Unauthorized", "message": "Invalid or missing credentials" } 5.2 GET TRANSACTION BY ID Endpoint GET /transactions/{id} Description Returns a single transaction matching the given ID.

Example Request

curl.exe -u admin:momo2025 http://127.0.0.1:8000/transactions/1 image

Response (200 OK) { "id": 1, "type": "send", "amount": 5000, "sender": "A", "receiver": "B" } Error (404 Not Found) { "error": "Not Found", "message": "Transaction does not exist" } 5.3 CREATE TRANSACTION (POST) Endpoint POST /transactions Description

Creates a new transaction and stores it in the XML file.

Request Body { "type": "send", "amount": 7000, "sender": "A", "receiver": "B" } Example Request

curl.exe -u admin:momo2025 -X POST http://127.0.0.1:8000/transactions -H "Content-Type: application/json" --data-binary "@payload.json" Success Response (201 Created)

image
{ "status": "created", "message": "Transaction saved successfully", "transaction_id": 2 } Error Response (400 Bad Request) { "error": "Bad Request", "message": "Invalid JSON body" } 5.4 UPDATE TRANSACTION (PUT) Endpoint PUT /transactions/{id} Description

Updates an existing transaction.

Example Request

curl.exe -u admin:momo2025 -X PUT "http://127.0.0.1:8000/transactions/1" -H "Content-Type: application/json" --data-binary "@update.json" Response (200 OK) { "message": "Transaction updated successfully" }

image
5.5 DELETE TRANSACTION Endpoint DELETE /transactions/{id} Description

Deletes a transaction from the XML file.

Example Request curl.exe -u admin:momo2025 -X DELETE http://127.0.0.1:8000/transactions/1 Response (200 OK) { "message": "Transaction deleted successfully" }

image
Error Response (404 Not Found) { "error": "Not Found", "message": "Transaction does not exist" }

6. DATA STRUCTURES & ALGORITHMS (DSA)
Linear Search
Iterates through all transactions one by one
Time Complexity: O(n)
Dictionary Lookup
Uses a HashMap (id → transaction)
Time Complexity: O(1)
Comparison
Method	Time Complexity	Efficiency
Linear Search	O(n)	Slow
Dictionary Lookup	O(1)	Fast
TESTING
The API was tested using:

curl.exe
Postman
✔ Test Cases Covered
Successful GET with authentication
Unauthorized access (401)
Successful POST request
Successful PUT request
Successful DELETE request
GET request success

Screenshot 2026-05-30 211621
Unauthorized access error

image

COMMENT
Dictionary lookup is significantly faster because it directly accesses data using keys instead of scanning all records.

Improvement Suggestion
Other efficient structures:

Balanced Binary Search Trees (O(log n))
Indexed databases (SQLite, PostgreSQL)
Hash indexing systems

9.CONCLUSION

The API successfully implements secure CRUD operations over XML data using Basic Authentication. The system demonstrates efficient data handling and comparison of search algorithms using DSA principles.





📄 API DOCUMENTATION
Mobile Money SMS Transaction REST API

1.INTRODUCTION

2. BASE URL
   
3. AUTHENTICATION & SECURITY
   
4.Authentication Method

5.Valid Credentials

6. DATA FORMAT
   
7. API ENDPOINTS (CRUD OPERATIONS)/h1>
   
8. DATA STRUCTURES & ALGORITHMS (DSA)
   
Linear Search

Dictionary Lookup

Comparison

Test Cases Covered

COMMENT

Improvement Suggestion
