# How Servers Return Responses

---

## 1. Client Request
- **Client (Browser/App)** sends a request to the server.
  - Example: `GET /users`
  - Sent over HTTP/HTTPS protocols.

---

## 2. Server Processes Request
- **Server** processes the request.
  - Figures out the appropriate resource (file, db, another service).

---

## 3. Server Response
- The **server responds** to the client with:
  1. **Header**
     - **Status Code**: Indicates the result of the request.
        - Examples:
          - `200 OK` 
          - `404 Not Found` 
          - `500 Internal Server Error`
     - **Content Type**
       - 
  2. **Body**
     - **Response Text**: The content of the response.
        - Examples:
          - JSON data
          - HTML content
          - Image as binary data

---

## 4. Example Response
### Request:
```http
GET /api/users HTTP/1.1
Host: example.com
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234
<html>
<body>
<div>
    <h1>Example Domain</h1>
</div>
</body>
</html>
```