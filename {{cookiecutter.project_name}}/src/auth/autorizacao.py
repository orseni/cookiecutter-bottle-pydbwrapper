import bottle
import jwt
from .token import TokenExtractor, SmartToken, TokenExtractorError

ROTAS_IGNORADAS = ['/login', '/api/public/']


def before_request():
    if any([rota in bottle.request.url for rota in ROTAS_IGNORADAS]):
        return

    try:
        authorization = bottle.request.headers['Authorization']
        token = TokenExtractor.extract_token(authorization)
        payload = SmartToken.decode_payload(token)

        Usuario.ID = payload.jti
        Usuario.EMAIL = payload.sub

        if token:
            renewed_token = TokenExtractor.renew(payload)
            if renewed_token:
                bottle.response.add_header('token-renewed', renewed_token)
    except KeyError:
        raise_unauthorized_status()
    except jwt.exceptions.ExpiredSignatureError:
        raise_unauthorized_status()
    except TokenExtractorError:
        raise_unauthorized_status()


def raise_unauthorized_status():
    raise bottle.HTTPError(401, body=bottle.HTTP_CODES[401])


class Usuario:
    ID = None
    EMAIL = None
