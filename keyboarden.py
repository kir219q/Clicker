from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
kbclicken = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=("Click")),
            KeyboardButton(text=("Improve")),
        ],
        [
            KeyboardButton(text="PvP"),
            KeyboardButton(text=("Settings")),
            KeyboardButton(text="Author"),
            #            KeyboardButton(text=("Support the author"))
        ],
        [
            KeyboardButton(text=("Achievements")),
            KeyboardButton(text=('Leaderboard')),
            KeyboardButton(text=("Exit"))
        ]
    ],
    resize_keyboard=True
)
kbchoiceen = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Yes"),
            KeyboardButton(text="No"),
        ]
    ],
    resize_keyboard=True
)
kbpvpen = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="PvP battle by nickname"),
         KeyboardButton(text="Selection of PvP battle players")
         ],
        [
            KeyboardButton(text="Settings"),
            KeyboardButton(text="Exit")
        ]
    ],
    resize_keyboard=True
)
kbnexten = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Previous"),
            KeyboardButton(text="Next")
        ],
        [
            KeyboardButton(text="Close")
        ]
    ],
    resize_keyboard=True
)
kbsetingen = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="First", callback_data="seting1"),
    ],
    [
        InlineKeyboardButton(text="Second", callback_data="seting3"),
    ],
    [
        InlineKeyboardButton(text="Change the language", callback_data="setinglang")
    ],
    [
        InlineKeyboardButton(text="Change your nickname", callback_data="setingname")
    ]

])
kbmpinven = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Agree", callback_data="mpyes"),
    ],
    [
        InlineKeyboardButton(text="Refuse", callback_data="mpno"),
    ],
])
kbcancelpodboren = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Cancel", callback_data="cancelpodbor")
    ]
])
kbmpstarten = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Start", callback_data="mpstart")
    ]
])
kbmpen = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Click"),
        ],
        [
            KeyboardButton(text="Improve")
        ]
    ],
    resize_keyboard=True
)
kbplusen = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Improve",callback_data="mpplusyes")
    ]

])
kbinvcancelen = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text=("Cancel the invitation."),callback_data="mpinvcancel")
    ]
])
kboken = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Ok.",callback_data="mpok")
    ]
])