from aiogram.types import Update
from aiogram import BaseMiddleware
from models.main import User
from typing import Callable, Dict, Any, Awaitable

class UserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any],
    ) -> Any:
        if event.message:
            event_data = event.message
        elif event.callback_query:
            event_data = event.callback_query
        user = await User.get_or_none(telegram_id=event_data.from_user.id)
        if not user:
            user = await User.create(
                telegram_id=event_data.from_user.id,
                name=event_data.from_user.full_name,
            )
        data["user"] = user
        return await handler(event, data)