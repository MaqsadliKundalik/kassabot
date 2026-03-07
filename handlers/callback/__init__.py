from . import reports
from aiogram import Router

router = Router()
router.include_router(reports.router)