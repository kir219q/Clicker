from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from load_all import _
kbclickru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=("Клик")),
            KeyboardButton(text=("Улучшить")),
        ],
        [
            KeyboardButton(text="PvP"),
            KeyboardButton(text=("Настройки")),
            KeyboardButton(text="Автор")
            #            KeyboardButton(text=("Поддержать автора"))
        ],
        [
            KeyboardButton(text=("Достижения")),
            KeyboardButton(text=('Лидеры')),
            KeyboardButton(text=("Выход"))
        ]
    ],
    resize_keyboard=True
)
kbchoiceru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Да"),
            KeyboardButton(text="Нет"),
        ]
    ],
    resize_keyboard=True
)
kbpvpru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="PvP сражение по нику"),
         KeyboardButton(text="Подбор игроков PvP сражения")
         ],
        [
            KeyboardButton(text="Настройки"),
            KeyboardButton(text="Выход")
        ]
    ],
    resize_keyboard=True
)
kbnextru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Предыдущее"),
            KeyboardButton(text="Следующее")
        ],
        [
            KeyboardButton(text="Закрыть")
        ]
    ],
    resize_keyboard=True
)
kbsetingru = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Первый", callback_data="seting1"),
    ],
    [
        InlineKeyboardButton(text="Второй", callback_data="seting3"),
    ],
    [
        InlineKeyboardButton(text="Изменить язык", callback_data="setinglang")
    ],
    [
        InlineKeyboardButton(text="Изменить ник", callback_data="setingname")
    ]
])
kbmpinvru = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Согласиться", callback_data="mpyes"),
    ],
    [
        InlineKeyboardButton(text="Отказаться", callback_data="mpno"),
    ],
])

kbcancelpodborru = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Отмена", callback_data="cancelpodbor")

    ]
])

kbmpstartru = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Старт", callback_data="mpstart")
    ]
])
kbmpru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Клик"),
        ],
        [
            KeyboardButton(text="Улучшить")
        ]
    ],
    resize_keyboard=True
)
kbplusru = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Улучшить",callback_data="mpplusyes")
    ]

])
kbinvcancelru = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text=("Отменить приглашение."),callback_data="mpinvcancel")
    ]
])
kbokru = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Ок.",callback_data="mpok")
    ]
])
kblang = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="English", callback_data="en"),
        InlineKeyboardButton(text="Русский", callback_data="ru")
    ]
])
kblistp = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Следующий", callback_data="nextp"),
        InlineKeyboardButton(text="Выход", callback_data="exitp")
    ]
])