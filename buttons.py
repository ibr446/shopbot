from aiogram import types

key = [
    [types.KeyboardButton(text="Keyimlar", ), types.KeyboardButton(text="Texnika", )],
     # types.KeyboardButton(text="Telefon"), types.KeyboardButton(text="Kompyuter")],
]
keyboard = types.ReplyKeyboardMarkup(keyboard=key, resize_keyboard=True)


Gadjet = [
    [types.KeyboardButton(text="Phone",), types.KeyboardButton(text="Computer")],
    [types.KeyboardButton(text="Headphones",), types.KeyboardButton(text="Televizor")],
]
Gadjet = types.ReplyKeyboardMarkup(keyboard=Gadjet, resize_keyboard=True)



sezon = [
    [types.KeyboardButton(text="Qish🥶"),types.KeyboardButton(text="Bahor😍")],
    [types.KeyboardButton(text="Kuz🍀"),types.KeyboardButton(text="Yoz⛱")],
]
sezonkey = types.ReplyKeyboardMarkup(keyboard=sezon, resize_keyboard=True)

phonebrand = [
    [types.KeyboardButton(text="iphone"), types.KeyboardButton(text="Samsung")],
    [types.KeyboardButton(text="Redmi"), types.KeyboardButton(text="Vivo")],
    [types.KeyboardButton(text="Oppo"), types.KeyboardButton(text="Poco")],
    [types.KeyboardButton(text="Huawie"), types.KeyboardButton(text="Honor")],
]
phonebrand = types.ReplyKeyboardMarkup(keyboard=phonebrand, resize_keyboard=True)




model = [
    [types.KeyboardButton(text="iphone 15 Pro Max"), types.KeyboardButton(text="Iphone 14 Pro Max")],
    [types.KeyboardButton(text="Iphone 13 Pro Max"), types.KeyboardButton(text="Iphone 12 Pro Max")],
    [types.KeyboardButton(text="Iphone 11 Pro Max"), types.KeyboardButton(text="Iphone XS MAX")],
    [types.KeyboardButton(text="Iphone XR"), types.KeyboardButton(text="Iphone XS")],
]
model = types.ReplyKeyboardMarkup(keyboard=model, resize_keyboard=True)


s = [
    [types.KeyboardButton(text="Samsung Galaxy S23 Ultra"), types.KeyboardButton(text="Samsung Galaxy S22 Ultra")],
    [types.KeyboardButton(text="Samsung Galaxy S22"), types.KeyboardButton(text="Samsung Galaxy A73")],
    [types.KeyboardButton(text="Samsung Galaxy A53"), types.KeyboardButton(text="Samsung Galaxy Z Flip5")],
    [types.KeyboardButton(text="Samsung Galaxy M14"), types.KeyboardButton(text="Samsung Galaxy A54")],
]
s = types.ReplyKeyboardMarkup(keyboard=s, resize_keyboard=True)



winterClothes = [
    [types.KeyboardButton(text="ustki kiyim🧥"),types.KeyboardButton(text="oyoq kiyim🥾")],
    [types.KeyboardButton(text="Qolqop🧤"),types.KeyboardButton(text="Sharf🧣")],
]
winterClothes = types.ReplyKeyboardMarkup(keyboard=winterClothes, resize_keyboard=True)


spring = [
    [types.KeyboardButton(text="olimpika👚"), types.KeyboardButton(text="krosovka👟")],
    [types.KeyboardButton(text="sviter🧥"),types.KeyboardButton(text="noski🧦")],
]
spring = types.ReplyKeyboardMarkup(keyboard=spring, resize_keyboard=True)


autum = [
    [types.KeyboardButton(text="Koylak👔"), types.KeyboardButton(text="shim👖")],
    [types.KeyboardButton(text="kepka🧢"),types.KeyboardButton(text="jacket autum")],
]
autum = types.ReplyKeyboardMarkup(keyboard=autum, resize_keyboard=True)
