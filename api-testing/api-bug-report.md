\# API Test Report



\## Issue Title



POST /users returns 201 Created, but the returned resource cannot be retrieved



\## API



JSONPlaceholder



\## Environment



Public test API: `https://jsonplaceholder.typicode.com`



\## Test Objective



Verify whether a user returned as successfully created by the `POST /users` endpoint can subsequently be retrieved using the ID returned by the API.



\## Test 1 — Create User



\### Request



\*\*Method:\*\* `POST`



\*\*Endpoint:\*\*



`https://jsonplaceholder.typicode.com/users`



\*\*Request Body:\*\*



```json

{

&#x20;   "name": "Test User"

}

```



\### Actual Result



\*\*HTTP Status:\*\* `201 Created`



\*\*Response Body:\*\*



```json

{

&#x20;   "name": "Test User",

&#x20;   "id": 11

}

```



The API returned `201 Created` and assigned the new resource ID `11`.



\## Test 2 — Retrieve Created User



Immediately after the POST request, a GET request was made using the ID returned by the API.



\### Request



\*\*Method:\*\* `GET`



\*\*Endpoint:\*\*



`https://jsonplaceholder.typicode.com/users/11`



\### Expected Result



The API should return the user associated with ID `11` if the POST response represents a retrievable created resource.



\### Actual Result



\*\*HTTP Status:\*\* `404 Not Found`



\*\*Response Body:\*\* None



The resource returned by the POST response could not be retrieved using the returned ID.



\## Reproduction Steps



1\. Send a `POST` request to `/users`.

2\. Use the JSON body:



&#x20;  ```json

&#x20;  {

&#x20;      "name": "Test User"

&#x20;  }

&#x20;  ```

3\. Confirm that the API returns `201 Created`.

4\. Record the ID returned in the response.

5\. Send a `GET` request to `/users/11` using the returned ID.

6\. Observe that the API returns `404 Not Found` with no response body.



\## Result



The POST operation reports successful creation and returns resource ID `11`, but a subsequent GET request for that resource returns `404 Not Found`.



\## Severity



\*\*Low\*\*



\## QA Assessment



This behavior is an observable inconsistency between the POST response and the subsequent GET request.



Because JSONPlaceholder is a public mock/testing API rather than a production application with a supplied API specification, this test does not establish a confirmed production defect. The result is documented as an API behavior observed during testing.



\## Evidence



\* POST `/users` → `201 Created`

\* POST response returned ID `11`

\* GET `/users/11` → `404 Not Found`

\* GET response contained no body



