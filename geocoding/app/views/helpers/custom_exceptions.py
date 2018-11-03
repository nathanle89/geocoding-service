from rest_framework.exceptions import APIException

class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'

class ParseError(APIException):
    status_code = 400
    default_detail = 'Bad Request'
    default_code = 'bad_request'

class ValidationError(APIException):
    status_code = 422
    default_detail = 'Validation failed'
    default_code = 'validation_error'
