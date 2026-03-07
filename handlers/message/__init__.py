from . import reports, start
from aiogram import Router

router = Router()
router.include_router(reports.router)
router.include_router(start.router)