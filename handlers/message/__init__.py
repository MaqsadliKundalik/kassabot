from . import reports, start, admin
from aiogram import Router

router = Router()
router.include_router(reports.router)
router.include_router(start.router)
router.include_router(admin.router)