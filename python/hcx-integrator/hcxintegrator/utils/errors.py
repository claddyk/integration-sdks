import enum

class ErrorCodes(enum.Enum):
    ERR_INVALID_PAYLOAD = "ERR_INVALID_PAYLOAD"
    ERR_INVALID_ENCRYPTION = "ERR_INVALID_ENCRYPTION"
    ERR_WRONG_DOMAIN_PAYLOAD = "ERR_WRONG_DOMAIN_PAYLOAD"
    ERR_INVALID_DOMAIN_PAYLOAD = "ERR_INVALID_DOMAIN_PAYLOAD"
    ERR_SENDER_NOT_SUPPORTED = "ERR_SENDER_NOT_SUPPORTED"
    ERR_MANDATORY_HEADER_MISSING = "ERR_MANDATORY_HEADER_MISSING"
    ERR_INVALID_API_CALL_ID = "ERR_INVALID_API_CALL_ID"
    ERR_INVALID_CORRELATION_ID = "ERR_INVALID_CORRELATION_ID"
    ERR_INVALID_TIMESTAMP = "ERR_INVALID_TIMESTAMP"
    ERR_INVALID_REDIRECT_TO = "ERR_INVALID_REDIRECT_TO"
    ERR_INVALID_STATUS = "ERR_INVALID_STATUS"
    ERR_INVALID_DEBUG_FLAG = "ERR_INVALID_DEBUG_FLAG"
    ERR_INVALID_ERROR_DETAILS = "ERR_INVALID_ERROR_DETAILS"
    ERR_INVALID_DEBUG_DETAILS = "ERR_INVALID_DEBUG_DETAILS"
    ERR_INVALID_WORKFLOW_ID = "ERR_INVALID_WORKFLOW_ID"
    ERR_SERVICE_UNAVAILABLE = "ERR_SERVICE_UNAVAILABLE"
    ERR_DOMAIN_PROCESSING = "ERR_DOMAIN_PROCESSING"


class ResponseMessage(enum.Enum): 
    INVALID_PAYLOAD_LENGTH_ERR_MSG = "Mandatory elements of JWE token are missing.Should have all 5 elements";
    INVALID_PAYLOAD_VALUES_ERR_MSG = "Payload contains null or empty values";
    INVALID_API_CALL_ID_ERR_MSG = "Api call id cannot be null, empty and other than 'String'";
    INVALID_CORRELATION_ID_ERR_MSG = "Correlation id cannot be null, empty and other than 'String'";
    INVALID_WORKFLOW_ID_ERR_MSG = "Workflow id should be a string";
    INVALID_TIMESTAMP_ERR_MSG = "Timestamp cannot be in future date";
    INVALID_DEBUG_FLAG_ERR_MSG = "Debug flag cannot be null, empty and other than 'String'";
    INVALID_DEBUG_FLAG_RANGE_ERR_MSG = "Debug flag cannot be other than {0}";
    INVALID_ERROR_DETAILS_ERR_MSG = "Error details cannot be null, empty and other than 'JSON Object' with mandatory fields code or message";
    INVALID_ERROR_DETAILS_RANGE_ERR_MSG = "Error details should contain only: {0}";
    INVALID_ERROR_DETAILS_CODE_ERR_MSG ="Invalid Error Code";
    INVALID_DEBUG_DETAILS_ERR_MSG = "Debug details cannot be null, empty and other than 'JSON Object' with mandatory fields code or message";
    INVALID_DEBUG_DETAILS_RANGE_ERR_MSG = "Debug details should contain only: {0}";
    INVALID_STATUS_ERR_MSG = "Status cannot be null, empty and other than 'String'";
    INVALID_STATUS_ACTION_RANGE_ERR_MSG = "Status value for action API calls can be only: {0}";
    INVALID_STATUS_ON_ACTION_RANGE_ERR_MSG = "Status value for on_action API calls can be only: {0}";

    INVALID_MANDATORY_ERR_MSG = "Mandatory headers are missing: {0}";
    INVALID_REDIRECT_ERR_MSG = "Redirect requests must have valid participant code for field {0}";
    INVALID_REDIRECT_SELF_ERR_MSG = "Sender can not redirect request to self";
    INVALID_JSON_REQUEST_BODY_ERR_MSG = "Request body should be a proper JWE object for action API calls";