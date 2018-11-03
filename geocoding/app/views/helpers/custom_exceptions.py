from rest_framework.exceptions import APIException

class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'

class ServerError(APIException):
    status_code = 500
    default_detail = 'Oops something went wrong'
    default_code = 'server_error'

class ParseError(APIException):
    status_code = 400
    default_detail = 'Bad Request'
    default_code = 'bad_request'

class ValidationError(APIException):
    status_code = 422
    default_detail = 'Validation failed'
    default_code = 'validation_error'

class NotFound(APIException):
    status_code = 404
    default_detail = 'Not Found'
    default_code = 'not_found'
