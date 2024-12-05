import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from config import token
from buttons import keyboard, sezonkey, Gadjet, phonebrand, model, s, winterClothes, spring, autum
import random
    
TOKEN = token

dp = Dispatcher()


rasm1 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoFPVUNxhBX3nTzfElIZSYqIlKRnsG5Slnsp2eTtC9&s/"
rasm2 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSibbXj1wgSPus83iLrKwiSpNPuPysnOqo0rw&usqp=CAU/"
rasm3 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlVLcSEbZlLskmN8OHzipA0sKLLCw84pqevA&usqp=CAU/"
rasm4 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQAoDB_aYyd3Xdrs4fB4CYlfNCG97Lyc-CWbQ&usqp=CAU/"
rasm5 = "https://encrypted-tbn0.gstatic.   com/images?q=tbn:ANd9GcRbL4HsPGA0EqZX0EHnEovVw_k8EkwF_x8Iyw&usqp=CAU/"

rasm6 = "https://wallpapers.com/images/hd/black-animal-lying-cat-f2ovvd5g5sk8sa3m.webp/"
rasm7 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS91TsRwhMxcom_fZD41XGMW1xOugcmnmbjbg&usqp=CAU/"
rasm8 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSVgg2ATlvmv8gKNELV1TTV4RKc9Vv4kY-UFg&usqp=CAU/"
rasm9 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZjUopLfH6YYSIGge18PLSAuLtZmuQmfhJ2Q&usqp=CAU/"
rasm10 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0AOkUS3TcJe6iyedAm5P_8G8aSo-YYSU3qg&usqp=CAU/"


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(f" {message.from_user.first_name}  siz botga xush kelibsiz")  # noqa



@dp.message(Command("help"))
async def start(message: types.Message):
    await message.reply(f" salom {message.from_user.username} sizga qanday yordam bera olman")



@dp.message(Command("allpages"))
async def rasm(message: types.message):
    imageList = [rasm1, rasm2, rasm3, rasm4, rasm5, rasm6, rasm7, rasm8, rasm9, rasm10]
    for img in imageList:
        await message.answer(img)





@dp.message(Command("contact"))
async def contact(message: types.Message):
    f = message.from_user.first_name
    await message.answer_contact('+998909187086', first_name=f)



@dp.message(Command("location"))
async def location(message: types.Message):
    key = [
        [types.KeyboardButton(text="location", request_location=True)],
        [types.KeyboardButton(text="contact", request_location=True)],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=key, resize_keyboard=True)
    await message.answer(text="location or contact", reply_markup=keyboard)


@dp.message(Command("rasm"))
async def rasm(message: types.message):
    gold = [rasm1, rasm2, rasm3, rasm4, rasm5, rasm6, rasm7, rasm8, rasm9]
    away = random.choice(gold)
    await message.answer_photo(photo=f"{away}")


# @dp.message(Command("hayvonlar"))
# async def rasm(message: types.message):
#     iron = [rasm6, rasm7, rasm8, rasm9, rasm10]
#     ibr = random.choice(iron)
#     await message.answer_photo(photo=f"{ibr}")


@dp.message(Command("savol"))
async def start(message: types.Message):
    await message.answer("🟢savol \n 1. python qachon yaratilgan?")

    @dp.message()
    async def res(message: types.message):
        text = message.chat
        print(text)
        if message.text == "1991":
            await message.reply("✅")
        elif message.text != "1991":
            await message.reply("❌")



@dp.message(Command("shop"))
async def shop(message: Message):
    await message.answer(f" {message.from_user.first_name} shop turini tanlang", reply_markup=keyboard)

    @dp.message(F.text == "Keyimlar")
    async def keyimlar(message: Message):
        await message.answer_photo(photo="https://images.app.goo.gl/upbBmapdjXNvU1im8", reply_markup=sezonkey)

        @dp.message(F.text == "Qish🥶")
        async def Qish(message: Message):
            await message.answer("tanlang", reply_markup=winterClothes)

            @dp.message(F.text == "ustki kiyim🧥")
            async def Qish(message: Message):
                await message.answer_photo(photo="https://images.app.goo.gl/KWSvxv7xE9VXbTzD6", caption="Erkaklar uchun\n razmer bomba🧨\n Narxi 600USD💸\n")

                @dp.message(F.text == "oyoq kiyim🥾")
                async def Qish(message: Message):
                    await message.answer_photo(photo="https://images.app.goo.gl/Gw23vg8q4doW8DXK8", caption="Juda zor oyoqkiyimlar kelid🔥\n Narxi bomba💥 350USD💸\n")


                    @dp.message(F.text == "Qolqop🧤")
                    async def Qish(message: Message):
                        await message.answer_photo(photo="https://images.app.goo.gl/VWRMqjHu2ZrZhANL8", caption="zor gloveslar keldi🔥\n Narxi bomba 200USD💸")


                        @dp.message(F.text =="Sharf🧣")
                        async def Qish(message: Message):
                            await message.answer_photo(photo="https://images.app.goo.gl/pGGb952XAr9x6gCB6", caption="zor sharflar keldi\n Narxi Bomba 250USD💸🔥")


            @dp.message(F.text == "Bahor😍")
            async def Bahor(message: Message):
                await message.answer("tanlang", reply_markup=spring)

                @dp.message(F.text == "olimpika👚")
                async def Bahor(message: Message):
                    await message.answer_photo(photo="https://images.app.goo.gl/uCavgS31dnZUj9Yy7", caption="Narxi 350.000som\n")


                    @dp.message(F.text == "krosovka👟")
                    async def Bahor(message: Message):
                        await message.answer_photo(photo="https://images.app.goo.gl/BkVrDPcxHMC3kgDR9", caption="Super krossovkala\n Narxi=400USD\n")

                        @dp.message(F.text == "sviter🧥")
                        async def Bahor(message: Message):
                            await message.answer_photo(photo="https://images.app.goo.gl/ZPJiP66Sd7bsfV3KA", caption="Super skidka\n Narxi=350USD\n")

                            @dp.message(F.text == "noski🧦")
                            async def Bahor(message: Message):
                                await message.answer_photo(photo="https://images.app.goo.gl/HU5rHRHAxH5F1Jc59", caption="Narxi 150USD\n")

                        @dp.message(F.text == "Kuz🍀")
                        async def Kuz(message: Message):
                            await message.answer("tanlang", reply_markup=autum)

                            @dp.message(F.text == "Koylak👔")
                            async def Kuz(message: Message):
                                await message.answer_photo(photo="https://images.app.goo.gl/qwZHo6jabsXQrccQ6", caption="Narxi 250USD")

                                @dp.message(F.text == "shim👖")
                                async def Kuz(message: Message):
                                    await message.answer_photo(photo="https://images.app.goo.gl/nPJyRuWHCKjiRFxz7", caption= "narxi 300USD")







@dp.message(F.text == "Texnika")
async def Texnika(message: Message):
    await message.answer_photo(photo="https://images.app.goo.gl/qStxLtpqZXcyDNLm6", reply_markup=Gadjet)


@dp.message(F.text == "iphone")
async def Phone(message: Message):
    await message.answer_photo(photo="https://images.app.goo.gl/7qRjTUY3n8WUH5Mw8",reply_markup=model, caption='Iphone')


@dp.message(F.text=="Phone")
async def phone(message: types.message):
    await message.answer("tanlang", reply_markup=phonebrand)

    @dp.message(F.text =="iphone 15 Pro Max")
    async def iphone(message: Message):
        await message.answer_photo(photo="https://images.app.goo.gl/PsfjqpTVtpm3F8Ex9", caption= "📲Iphone 15 Pro Max 256gb sim\n🛠Holati ideal \n⚙️Aybi yoq \n🔋98% radnoy\n🎨Deep Purple \n📦Karobka dokument\n📝31 kun garantiya \n💸900$🔥\n♻️Obmen Iphone bor !\n🙅🏻‍♂️Kredit/Rasrochka yo'q\n\n👨🏻‍💻@Applemarketuzb\n☎️ 90 012 5555\n☎️ 91 012 5555\n☎️ 98 000 1474\n\n🌙Halollik Foydadan Ustun \n👬🏻👭🏻Yaxshi niyatda do'stlarga yuvorib qo'yamiz !\n💯Muhimi Ishonchli ✅\n\n🚘Dostavka xizmati Uzbekiston boylab\n📍Malika bozor B blok 44/3 Apple Market dokoni🍏\n\n🆔https://t.me/Applemarketuzbb",)


        @dp.message(F.text =="Iphone 14 Pro Max")
        async def iphone(message: Message):
            await message.answer_photo(photo="https://images.app.goo.gl/ZfJHFj7ByK9bTKkBA", caption="📲Iphone 14 Pro Max 256gb sim\n🛠Holati ideal \n⚙️Aybi yoq \n🔋89% radnoy\n🎨Deep Purple \n📦Karobka dokument\n📝31 kun garantiya \n💸900$🔥\n♻️Obmen Iphone bor !\n🙅🏻‍♂️Kredit/Rasrochka yo'q\n\n👨🏻‍💻@Applemarketuzb\n☎️ 90 012 5555\n☎️ 91 012 5555\n☎️ 98 000 1474\n\n🌙Halollik Foydadan Ustun \n👬🏻👭🏻Yaxshi niyatda do'stlarga yuvorib qo'yamiz !\n💯Muhimi Ishonchli ✅\n\n🚘Dostavka xizmati Uzbekiston boylab\n📍Malika bozor B blok 44/3 Apple Market dokoni🍏\n\n🆔https://t.me/Applemarketuzbb")


            @dp.message(F.text == "Iphone 13 Pro Max")
            async def iphone(message: Message):
                await message.answer_photo(photo="https://images.app.goo.gl/7us8SruZgstQFUE96",caption="📲Iphone 13 Pro Max 256gb\n🛠Holati ideal \n⚙️Aybi yoq LLA🇺🇸\n🔋97% radnoy\n🎨Graphite\n📦Karobka dokument\n📝31 kun garantiya \n💸840$🔥\n♻️Obmen Iphone bor !\n🙅🏻‍♂️Kredit/Rasrochka yo'q\n\n👨🏻‍💻@Applemarketuzb\n☎️ 90 012 5555\n☎️ 91 012 5555\n☎️ 98 000 1474\n\n🌙Halollik Foydadan Ustun \n👬🏻👭🏻Yaxshi niyatda do'stlarga yuvorib qo'yamiz !\n💯Muhimi Ishonchli ✅\n\n🚘Dostavka xizmati Uzbekiston boylab\n📍Malika bozor B blok 44/3 Apple Market dokoni🍏\n\n🆔https://t.me/Applemarketuzbb")



                @dp.message(F.text == "Iphone 12 Pro Max")
                async def iphone(message: Message):
                    await message.answer_photo(photo="https://images.app.goo.gl/SfmbFbG8nDuA6GkC6",caption="📲Iphone 12 Pro Max 256gb\n🛠Holati ideal ☑️\n⚙️Aybi yoq LLA🇺🇸\n🔋85% radnoy\n🎨Graphite \n📦Karobka dokument\n📝31 kun garantiya \n💸560$🔥\n♻️Obmen Iphone bor !\n🙅🏻‍♂️Kredit/Rasrochka yo'q\n\n👨🏻‍💻@Applemarketuzb\n👨🏻‍💻Telegram 900647777\n☎️ 90 012 5555\n☎️ 91 012 5555\n☎️ 98 000 1474\n\n🌙Halollik Foydadan Ustun \n👬🏻👭🏻Yaxshi niyatda do'stlarga yuvorib qo'yamiz !\n💯Muhimi Ishonchli ✅\n\n🚘Dostavka xizmati Uzbekiston boylab\n📍Malika bozor B blok 44/3 Apple Market dokoni🍏\n\n🆔https://t.me/Applemarketuzbb",)


                    @dp.message(F.text == "Iphone 11 Pro Max")
                    async def iphone(message: Message):
                        await message.answer_photo(photo="https://images.app.goo.gl/8q1dN2969KcwsGfD9", caption="🙋🏻‍♂️Qadrli \n🙋🏻Obunachilarimiz \n😊Uchun\n\n📲Iphone 11 Pro Max 64gb\n🛠Holati ideal ☑️\n⚙️Aybi yoq \n🔋100% radnoy \n🎨Green\n📦Karobka dokument\n📝31 kun garantiya \n💸480$🔥\n♻️Obmen Iphone bor !\n🙅🏻‍♂️Kredit/Rasrochka yo'q\n\n👨🏻‍💻@Applemarketuzb\n👨🏻‍💻Telegram 900647777\n☎️ 90 012 5555\n☎️ 91 012 5555\n☎️ 98 000 1474\n\n🌙Halollik Foydadan Ustun \n👬🏻👭🏻Yaxshi niyatda do'stlarga yuvorib qo'yamiz !\n💯Muhimi Ishonchli ✅\n\n🚘Dostavka xizmati Uzbekiston boylab\n📍Malika bozor B blok 44/3 Apple Market dokoni🍏\n\n🆔https://t.me/Applemarketuzbb",)



                        @dp.message(F.text == "Iphone XS MAX")
                        async def iphone(message: Message):
                            await message.answer_photo(photo="https://images.app.goo.gl/QmVgM2QtaGEXRzVC8", caption="📲Iphone Xs Max 256gb\n🛠Holati ideal \n⚙️Aybi yoq LLA🇺🇸\n🔋82% radnoy\n🎨Gold\n📦Karobka dokument\n📝31 kun garantiya \n💸310$🔥\n♻️Obmen Iphone bor !\n🙅🏻‍♂️Kredit/Rasrochka yo'q\n\n👨🏻‍💻@Applemarketuzb\n👨🏻‍💻Telegram 900647777\n☎️ 90 012 5555\n☎️ 91 012 5555\n☎️ 98 000 1474\n\n🌙Halollik Foydadan Ustun \n👬🏻👭🏻Yaxshi niyatda do'stlarga yuvorib qo'yamiz !\n💯Muhimi Ishonchli ✅\n\n🚘Dostavka xizmati Uzbekiston boylab\n📍Malika bozor B blok 44/3 Apple Market dokoni🍏\n\n🆔https://t.me/Applemarketuzbb",)


                            @dp.message(F.text == "Iphone XR")
                            async def iphone(message: Message):
                                await message.answer_photo(photo="https://images.app.goo.gl/dgdpDRTPzSkR5kbHA", caption="📲Iphone Xr 128gb\n🛠Holati ideal\n⚙️Aybi yoq \n🔋85% radnoy\n🎨White\n📦✖️\n📝31 kun garantiya \n💸270$\n♻️Obmen Rassrochka yoq\n\n👨🏻‍💻@Applemarketuzb\n☎️ 98 000 1474\n☎️ 99 314 7474\n☎️ 90 012 5555\n☎️ 91 012 5555\n\n🌙Halollik Foydadan Ustun \n👬🏻👭🏻Yaxshi niyatda do'stlarga yuvorib qo'yamiz !\n💯Muhimi Ishonchli ✅\n\n🚘Dostavka xizmati Uzbekiston boylab\n📍Malika bozor B blok 44/3 Apple Market dokoni🍏\n\n🆔https://t.me/Applemarketuzbb",)


                                @dp.message(F.text == "Iphone XS")
                                async def iphone(message: Message):
                                    await message.answer_photo(photo="https://images.app.goo.gl/xvRZXyzFyoy6mXHH8", caption="📲Iphone Xs 64gb\n🛠Holati ideal ☑️\n⚙️Aybi yoq \n🔋82% radnoy\n🎨Black\n📦✖️\n📝31 kun garantiya \n💸230$🔥\n♻️Obmen Iphone bor !\n🙅🏻‍♂️Kredit/Rasrochka yo'q\n\n👨🏻‍💻@Applemarketuzb\n👨🏻‍💻Telegram 900647777\n☎️ 90 012 5555\n☎️ 91 012 5555\n☎️ 98 000 1474\n\n🌙Halollik Foydadan Ustun \n👬🏻👭🏻Yaxshi niyatda do'stlarga yuvorib qo'yamiz !\n💯Muhimi Ishonchli ✅\n\n🚘Dostavka xizmati Uzbekiston boylab\n📍Malika bozor B blok 44/3 Apple Market dokoni🍏\n\n🆔https://t.me/Applemarketuzbb",)


@dp.message(F.text == "Samsung")
async def Samsung(message: Message):
    await message.answer_photo(photo="https://images.app.goo.gl/ZR6BeMvnoA61Xcmh8", reply_markup=s, caption="Samsung")


    @dp.message(F.text == "Samsung Galaxy S23 Ultra")
    async def Samsung(message: Message):
        await message.answer_photo(photo="https://images.app.goo.gl/VQABB6jBT7ridhNn6", caption="Applemarket 🍎\n\n🙋🏻‍♂️Samsung S23 Ultra soraganla uchun \nSotuvga keldi 😍\n\n🔝S23\n🔝S23+\n🔝S23 Ultra \n\n☎️98 000 1474\n☎️99 314 7474\n\n🌙Halollik Foydadan Ustun \n👬🏻👭🏻Yaxshi niyatda do'stlarga yuvorib qo'yamiz !\n💯Muhimi Ishonchli ✅\n\n🚘Dostavka xizmati Uzbekiston boylab\n📍Malika bozor B blok 44/3 Apple Market dokoni🍏\n\n🆔https://t.me/Applemarketuzbb",)


        @dp.message(F.text == "Samsung Galaxy S22 Ultra")
        async def Samsung(message: Message):
            await message.answer_photo(photo="https://images.app.goo.gl/if9fx5YWMKnvV3eQ6", caption="Applemarket🍎\n\n🙋🏻Samsung S22 Ultra soraganla uchun \n Narxi 850$\n")


            @dp.message(F.text == "Samsung Galaxy S22")
            async def Samsung(message: Message):
                await message.answer_photo(photo="https://images.app.goo.gl/ir6DTYUo4Xr5GT737", caption="Applemarket🍎\n\n🙋🏻Samsung S22 soraganla uchun \n Narxi 850$\n")







async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

