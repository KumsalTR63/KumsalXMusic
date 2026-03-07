# @The_Team_kumsal tarafından yasal olarak geliştirildi keyifli kullanımlar #kumsalteam

import asyncio
import importlib

from pyrogram import idle

from KumsalTR import anon, app, db, logger, stop, userbot
from KumsalTR.plugins import all_modules


def load_plugins() -> None:
    for module in all_modules:
        importlib.import_module(f"KumsalTR.plugins.{module}")

    # Ek modüller
    for extra in ("KumsalTR.Utah", "KumsalTR.av"):
        try:
            importlib.import_module(extra)
        except Exception as exc:
            logger.warning(f"Ek modül yüklenemedi: {extra} -> {exc}")


async def main() -> None:
    load_plugins()
    await db.connect()

    # Önbelleği bottaki dinamik listelere yükle
    app.bl_users.update(await db.get_blacklisted())
    app.sudoers.update(await db.get_sudoers())
    app.sudoers.add(app.owner)

    await app.boot()
    await userbot.boot()
    await anon.boot()

    logger.info("KumsalTR tamamen başlatıldı.")
    await idle()
    await stop()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())