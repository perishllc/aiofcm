from uuid import uuid4
from typing import Optional, Dict, Any, NoReturn


PRIORITY_NORMAL = 'normal'
PRIORITY_HIGH = 'high'

STATUS_SUCCESS = 'SUCCESS'


class Message:
    __slots__ = ('device_token', 'notification', 'data', 'priority', 'content_available',
                 'message_id', 'time_to_live', 'collapse_key')

    def __init__(
            self,
            device_token: str,
            notification: Optional[Dict[str, Any]] = None,
            data: Optional[Dict[str, Any]] = None,
            priority: Optional[str] = None,
            content_available: Optional[bool] = False,
            message_id: Optional[str] = None,
            time_to_live: Optional[int] = None,
            collapse_key: Optional[str] = None):

        self.device_token = device_token
        self.notification = notification
        self.data = data
        self.priority = priority
        self.content_available = content_available
        self.message_id = message_id or str(uuid4())
        self.time_to_live = time_to_live
        self.collapse_key = collapse_key

    def as_dict(self) -> Dict[str, Any]:
        result = dict(
            message_id=self.message_id,
            to=self.device_token,
        )

        for field in ('notification', 'data', 'priority', 'content_available', 'time_to_live',
                      'collapse_key'):
            value = getattr(self, field, None)
            if value is not None:
                result[field] = value

        return result


class MessageResponse:
    __slots__ = ('message_id', 'status', 'description')

    def __init__(self, message_id, status, description=None):
        # type: (str, str, Optional[str]) -> NoReturn
        self.message_id = message_id
        self.status = status
        self.description = description

    @property
    def is_successful(self):
        return self.status == STATUS_SUCCESS
