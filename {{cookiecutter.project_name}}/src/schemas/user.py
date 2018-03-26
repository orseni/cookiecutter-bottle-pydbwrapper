from bottle_cerberus import Schema

from .constants import DatePattern


class UserSchema(Schema):
    def schema(self):
        return {
            "id": {
                "type": "integer",
                "required": True
            },
            "name": {
                "type": "string",
                "required": True
            },
            "birth": {
                "type": "string",
                "required": True,
                "regex": DatePattern.DATE,
            }
        }
