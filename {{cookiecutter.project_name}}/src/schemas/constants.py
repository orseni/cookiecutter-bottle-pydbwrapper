class SchemaType:
    """
        Tipos aceitos pelo bottle-cerberus
    """
    QUERY_STRING = 'query_string'
    BODY = 'body'
    URL = 'url'


class DatePattern:
    """
        Valida datas no formato ISO 8601
    """
    DATE = "[0-9]{4}(-[0-9]{1,2}){2}"  # casa com 1991-5-13
    DATETIME = "[0-9]{4}(-[0-9]{1,2}){2}T[0-9]{2}(:[0-9]{2}){2}(.[0-9]{3})?[Z]"  # casa com 1991-5-13T12:00:00
