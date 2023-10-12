# Django Calculator Project REST API

This project provides a simple REST API for a calculator built using Django. The API allows you to perform basic arithmetic operations. You can use the following endpoints to interact with the calculator:

| Endpoint                        | HTTP Method | Description                              |
|---------------------------------|-------------|------------------------------------------|
| `/api/add/`                     | POST        | Perform addition.                        |
| `/api/subtract/`                | POST        | Perform subtraction.                     |
| `/api/multiply/`                | POST        | Perform multiplication.                  |
| `/api/divide/`                  | POST        | Perform division.                        |
| `/api/square/`                  | POST        | Calculate the square of a number.       |
| `/api/square-root/`             | POST        | Calculate the square root of a number.  |

### Usage

To use the API, make HTTP requests to the respective endpoints with the necessary data in the request body. Here's an example request using the `curl` command:

**Perform addition:**

```bash
curl -X POST -H "Content-Type: application/json" -d '{"operand1": 5, "operand2": 3}' http://your-api-url/api/add/
```

**Perform subtraction:**

```bash
curl -X POST -H "Content-Type: application/json" -d '{"operand1": 5, "operand2": 3}' http://your-api-url/api/subtract/
```

**Perform multiplication:**

```bash
curl -X POST -H "Content-Type: application/json" -d '{"operand1": 5, "operand2": 3}' http://your-api-url/api/multiply/
```

**Perform division:**

```bash
curl -X POST -H "Content-Type: application/json" -d '{"operand1": 6, "operand2": 2}' http://your-api-url/api/divide/
```

**Calculate the square of a number:**

```bash
curl -X POST -H "Content-Type: application/json" -d '{"number": 4}' http://your-api-url/api/square/
```

**Calculate the square root of a number:**

```bash
curl -X POST -H "Content-Type: application/json" -d '{"number": 16}' http://your-api-url/api/square-root/
```

### Response

The API will respond with a JSON object containing the result of the calculation. For example:

```json
{"result": 8}
```

### Error Handling

If there's an error, the API will respond with a JSON object containing an error message, such as:

```json
{"error": "Division by zero is not allowed."}
```
