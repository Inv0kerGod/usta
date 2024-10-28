CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:8000",
    "http://localhost",
    "http://127.0.0.1",
    "http://localhost:8080",
]


CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000 ",
    "http://localhost:8000 ",
]

CORS_ORIGIN_WRITELIST = (
    'http://localhost:3000',
    'http://localhost:',
)

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://127.0.0.1:8000',
]


CORS_ALLOW_HEADERS = (
    'content-disposition', 'accept-encoding',
    'content-type', 'accept', 'origin', 'Authorization', 'access-control-allow-methods',
    'Access-Control-Allow-Origin'
)

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)