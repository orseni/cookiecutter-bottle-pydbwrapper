import time

import jwt


class TokenExtractor:

    def extract_token(authorization):
        if not authorization:
            raise TokenExtractorError('validacao.TOKEN_AUSENTE')

        parts = authorization.split(' ')
        if len(parts) != 2:
            raise TokenExtractorError('validacao.TOKEN_INVALIDO')

        return parts[1]

    def renew(payload):
        id = payload.jti
        issuer = payload.iss
        subject = payload.sub
        exp = payload.exp
        privilegios = payload.roles

        now = current_time_milliseconds()
        diff = int(exp) - now

        quinzeMinutos = 1000 * 60 * 15
        umaHora = 1000 * 60 * 60

        if diff < quinzeMinutos:
            return SmartToken.token(id, issuer, subject, umaHora, privilegios)


class SmartToken:
    algorithm = 'HS256'
    secret = '$Key_ivendas_Y2hhdmVfdHJhZGVsaW5rcw=='

    def token(id, issuer, subject, ttl_milliseconds, privilegios):
        now = current_time_milliseconds()
        exp = now + ttl_milliseconds

        payload = {
            'jti': id,
            'iat': now,
            'sub': subject,
            'iss': issuer,
            'exp': exp,
            'roles': privilegios
        }

        return jwt.encode(payload,
                          SmartToken.secret,
                          algorithm=SmartToken.algorithm)

    def decode_payload(token):
        payload_dict = jwt.decode(token,
                                  SmartToken.secret,
                                  algorithm=SmartToken.algorithm)

        return Payload(**payload_dict)


class TokenExtractorError(Exception):
    pass


class Payload:
    def __init__(self, **kargs):
        self.__dict__ = kargs


def current_time_milliseconds():
    return int(time.time())
