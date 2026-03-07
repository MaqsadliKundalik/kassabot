from . import message, callback
from aiogram import Router

router = Router()
router.include_routers(message.router, callback.router)