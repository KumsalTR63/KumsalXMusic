# @The_Team_kumsal tarafından yasal olarak geliştirildi keyifli kullanımlar #kumsalteam
# Copyright (c) 2025 TheHamkerAlone
# Licensed under the MIT License.
# This file is part of KumsalTR

from pyrogram import types
from KumsalTR import app, config, lang
from KumsalTR.core.lang import lang_codes


class Inline:
    def __init__(self):
        self.ikm = types.InlineKeyboardMarkup
        self.ikb = types.InlineKeyboardButton

    def cancel_dl(self, text) -> types.InlineKeyboardMarkup:
        return self.ikm([[self.ikb(text="❌ İᴘᴛᴀʟ 𝐄ᴛ", callback_data=f"cancel_dl")]])

    def controls(
        self,
        chat_id: int,
        status: str = None,
        timer: str = None,
        remove: bool = False,
    ) -> types.InlineKeyboardMarkup:
        keyboard = []
        if status:
            keyboard.append(
                [self.ikb(text=status, callback_data=f"controls status {chat_id}")]
            )
        elif timer:
            keyboard.append(
                [self.ikb(text=timer, callback_data=f"controls status {chat_id}")]
            )

        if not remove:
            keyboard.append(
                [
                    self.ikb(
                        text="✙ 𝐁єηі 𝐆ʀσυвυηα 𝐄ᴋʟє ✙",
                        url=f"https://t.me/{app.username}?startgroup=true"
                    )
                ]
            )
            keyboard.append(
                [
                    self.ikb(text="˹ 𝐃єѕᴛєᴋ ˼", url="https://t.me/The_Team_Kumsal"),
                    self.ikb(text="⌯ 𝐊ᴀᴘᴀᴛ ⌯", callback_data="help close")
                ]
            )
        return self.ikm(keyboard)

    def help_markup(
        self, _lang: dict, back: bool = False
    ) -> types.InlineKeyboardMarkup:
        if back:
            rows = [
                [
                    self.ikb(text=_lang["back"], callback_data="help back"),
                    self.ikb(text=_lang["close"], callback_data="help close"),
                ]
            ]
        else:
            cbs = [
                "ʏᴏɴᴇᴛɪᴄɪ", "ʏᴇᴛᴋɪʟɪ", "ʙ-ʟɪsᴛ",
                "ᴅɪʟ", "ᴘɪɴɢ", "ᴏʏɴᴀᴛ",
                "ᴋᴜʏʀᴜᴋ", "sᴛᴀᴛs", "sᴜᴅᴏ",
                "ᴇᴛɪᴋᴇᴛ", "ᴇɢʟᴇɴᴄᴇ"
            ]

            buttons = []
            for cb in cbs:
                text = _lang.get(f"help_{cb}", cb.capitalize())
                buttons.append(self.ikb(text=text, callback_data=f"help {cb}"))

            rows = [buttons[i:i+3] for i in range(0, len(buttons), 3)]

        return self.ikm(rows)

    def lang_markup(self, _lang: str) -> types.InlineKeyboardMarkup:
        langs = lang.get_languages()

        buttons = [
            self.ikb(
                text=f"{name} ({code}) {'✔️' if code == _lang else ''}",
                callback_data=f"lang_change {code}",
            )
            for code, name in langs.items()
        ]
        rows = [buttons[i:i+2] for i in range(0, len(buttons), 2)]
        return self.ikm(rows)

    def ping_markup(self, text: str) -> types.InlineKeyboardMarkup:
        return self.ikm([[self.ikb(text="˹ 𝐃єѕᴛєᴋ ˼", url=config.SUPPORT_CHAT)]])

    def play_queued(
        self, chat_id: int, item_id: str, _text: str
    ) -> types.InlineKeyboardMarkup:
        return self.ikm(
            [
                [
                    self.ikb(
                        text="⚡ sɪᴍᴅɪ ᴄᴀʟ",
                        callback_data=f"controls force {chat_id} {item_id}"
                    )
                ]
            ]
        )

    def queue_markup(
        self, chat_id: int, _text: str, playing: bool
    ) -> types.InlineKeyboardMarkup:
        _action = "pause" if playing else "resume"
        return self.ikm(
            [[self.ikb(text=_text, callback_data=f"controls {_action} {chat_id} q")]]
        )

    def settings_markup(
        self, lang: dict, admin_only: bool, cmd_delete: bool, language: str, chat_id: int
    ) -> types.InlineKeyboardMarkup:
        return self.ikm(
            [
                [
                    self.ikb(text="𝐎ʏɴᴀᴛᴍᴀ 𝐌ᴏᴅᴜ ➜", callback_data="settings"),
                    self.ikb(text=admin_only, callback_data="settings play"),
                ],
                [
                    self.ikb(text="𝐊ᴏᴍᴜᴛ 𝐒ɪʟᴍᴇ ➜", callback_data="settings"),
                    self.ikb(text=cmd_delete, callback_data="settings delete"),
                ],
                [
                    self.ikb(text="🌐 𝐃ɪʟ 𝐒ᴇᴄ̧ɪɴ ➜", callback_data="settings play"),
                    self.ikb(text=lang_codes[language], callback_data="language"),
                ],
            ]
        )

    # 🔥 START MENÜ (BUTONLAR YAN YANA)
    def start_key(
        self, lang: dict, private: bool = False
    ) -> types.InlineKeyboardMarkup:

        rows = [
            [
                self.ikb(
                    text="✙ ʙᴇɴɪ ɢʀᴜʙᴜɴᴀ ᴇᴋʟᴇ ✙",
                    url=f"https://t.me/{app.username}?startgroup=true",
                ),
                self.ikb(text="˹ ʏᴀʀᴅɪᴍ ᴋᴏᴍᴜᴛʟᴀʀ ˼", callback_data="help"),
            ],
            [
                self.ikb(text="˹ ᴅᴇsᴛᴇᴋ ˼", url=config.SUPPORT_CHAT),
                self.ikb(text="˹ 𝐆ϋηᴄєʟʟєᴍєʟєʀ ˼", url=config.SUPPORT_CHANNEL),
            ],
        ]

        if private:
            rows.append(
                [
                    self.ikb(text="sᴀʜɪᴘ ˼", user_id=config.OWNER_ID),
                    self.ikb(
                        text="˹ ᴋᴀʏɴᴀᴋ ᴋᴏᴅ ˼",
                        url="https://github.com/KumsalTR63/KumsalXMusic",
                    ),
                ]
            )
        else:
            rows.append(
                [
                    self.ikb(text="🌐 𝐃іʟ", callback_data="language")
                ]
            )

        return self.ikm(rows)

    def yt_key(self, link: str) -> types.InlineKeyboardMarkup:
        return self.ikm(
            [
                [
                    self.ikb(text="❐ 𝐊ᴏᴘʏᴀʟᴀ", copy_text=link),
                    self.ikb(text="𝐘ᴏᴜᴛᴜʙᴇ", url=link),
                ],
            ]
        )