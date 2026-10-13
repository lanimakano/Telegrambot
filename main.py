import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiohttp import web

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
        await message.answer("Привет! Бот успешно запущен в облаке на Render!")

@dp.message()
async def echo_cmd(message: types.Message):
        if message.text:
                    await message.answer(f"Эхо: {message.text}")

    # Простой веб-сервер для бесплатного тарифа Render
    async def handle(request):
            return web.Response(text="Bot is running!")

async def start_web_server():
        app = web.Application()
        app.router.add_get("/", handle)
        runner = web.AppRunner(app)
        await runner.setup()
        port = int(os.environ.get("PORT", 10000))
        site = web.TCPSite(runner, "0.0.0.0", port)
        await site.start()

async def main():
        await start_web_server()
        await dp.start_polling(bot)

if __name__ == "__main__":
        asyncio.run(main())
