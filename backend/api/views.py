from django.db import DatabaseError, connection
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def root(request):
    return Response({"message": "Field Service Management API is running"})


@api_view(["GET"])
def health(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
    except DatabaseError:
        return Response(
            {"detail": "Database connection unavailable"},
            status=503,
        )

    return Response({"status": "ok", "database": "connected"})
