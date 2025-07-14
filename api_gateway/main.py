from fastapi import FastAPI, Request
from fastapi.responses import Response
import httpx

app = FastAPI(title="API Gateway")

MICROSERVICES = {
    "users": "http://users_service:8000",
    "events": "http://events_service:8001",
    "purchases": "http://purchase_service:8002",
    "locations": "http://location_service:8003",
    "notifications": "http://notification_service:8004",
    "tickets": "http://tickets_service:8006",
    "payments": "http://payments_service:8007"
}

@app.api_route("/{service}/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy(service: str, path: str, request: Request):
    if service not in MICROSERVICES:
        return JSONResponse(status_code=404, content={"detail": "Servicio no encontrado"})

    url = f"{MICROSERVICES[service]}/{path}"
    method = request.method
    headers = dict(request.headers)
    body = await request.body()

    async with httpx.AsyncClient() as client:
        response = await client.request(
            method, url, headers=headers, content=body
        )

    return Response(content=response.content, status_code=response.status_code, media_type=response.headers.get("content-type", "application/json"))