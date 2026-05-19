from rest_framework.views import exception_handler

from apps.core.responses import error_response


def custom_exception_handler(exc, context):

    response = exception_handler(exc, context)

    if response is not None:

        status_code = response.status_code
        errors = response.data

        message = 'Something went wrong'

        # Validation Error
        if status_code == 400:
            message = 'Validation error'

        # Unauthorized
        elif status_code == 401:

            detail = str(errors.get('detail', ''))

            if 'Token is expired' in str(errors):
                message = 'Token expired'

            elif 'token_not_valid' in str(errors):
                message = 'Invalid token'

            else:
                message = 'Unauthorized'

            errors = None

        # Forbidden
        elif status_code == 403:
            message = 'Forbidden'

        # Not Found
        elif status_code == 404:
            message = 'Not found'

        return error_response(
            message=message,
            errors=errors,
            status_code=status_code
        )

    return error_response(
        message='Internal server error',
        errors=None,
        status_code=500
    )