from rest_framework.views import exception_handler

from apps.core.responses import error_response


def custom_exception_handler(exc, context):

    response = exception_handler(exc, context)

    if response is not None:

        message = 'Something went wrong'

        if response.status_code == 400:
            message = 'Validation error'

        elif response.status_code == 401:
            message = 'Unauthorized'

        elif response.status_code == 403:
            message = 'Forbidden'

        elif response.status_code == 404:
            message = 'Not found'

        return error_response(
            message=message,
            errors=response.data,
            status_code=response.status_code
        )

    return error_response(
        message='Internal server error',
        errors=str(exc),
        status_code=500
    )