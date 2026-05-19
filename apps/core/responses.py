from rest_framework.response import Response


def success_response(
    message='Success',
    data=None,
    status_code=200
):

    response = {
        'success': True,
        'message': message,
        'data': data
    }

    return Response(
        response,
        status=status_code
    )


def error_response(
    message='Error',
    errors=None,
    status_code=400
):

    response = {
        'success': False,
        'message': message,
        'errors': errors
    }

    return Response(
        response,
        status=status_code
    )