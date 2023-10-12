from django.http import HttpRequest, JsonResponse
import json


def add(request: HttpRequest) -> JsonResponse:
    if request.method != "POST":
        return JsonResponse({"error": "Method not allwed"})
    
    body = request.body.decode()
    data = json.loads(body)

    result = data['operand1'] + data['operand2']
    return JsonResponse({"result": result})


def subtract(request: HttpRequest) -> JsonResponse:
    if request.method != "POST":
        return JsonResponse({"error": "Method not allwed"})
    pass


def multiply(request: HttpRequest) -> JsonResponse:
    if request.method != "POST":
        return JsonResponse({"error": "Method not allwed"})
    pass


def divide(request: HttpRequest) -> JsonResponse:
    if request.method != "POST":
        return JsonResponse({"error": "Method not allwed"})

    body = request.body.decode()
    data = json.loads(body)

    if data['operand2'] == 0:
        return JsonResponse({"error": "Division by zero is not allowed."})
        
    result = data['operand1'] / data['operand2']
    return JsonResponse({"result": result})


def square(request: HttpRequest) -> JsonResponse:
    if request.method != "POST":
        return JsonResponse({"error": "Method not allwed"})
    pass


def square_root(request: HttpRequest) -> JsonResponse:
    if request.method != "POST":
        return JsonResponse({"error": "Method not allwed"})
    pass