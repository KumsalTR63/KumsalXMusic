# @The_Team_kumsal tarafından yasal olarak geliştirildi keyifli kullanımlar #kumsalteam

from pyrogram import types
from KumsalTR import app, config, lang
from KumsalTR.core.lang import lang_codes


class Inline:
    def __init__(self):
        self.ikm = types.InlineKeyboardMarkup
        self.ikb = types.InlineKeyboardButton

    # ❌ İndirme iptal
    def cancel_dl(self, text):
        return self.ikm(
            [[self.ikb(text="❌ ɪ̇ᴘᴛᴀʟ ᴇᴛ", callback_data="cancel_dl")]]
        )

    # ▶️ Kontroller
    def controls(self, chat_id: int, status=None, timer=None, remove=False):

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
                        text="➕ ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ",
                        url=f"https://t.me/{app.username}?startgroup=true",
                    )
                ]
            )

            keyboard.append(
                [
                    self.ikb(text="📢 ᴅᴇsᴛᴇᴋ", url="https://t.me/The_Team_Kumsal"),
                    self.ikb(text="❌ ᴋᴀᴘᴀᴛ", callback_data="help close"),
                ]
            )

        return self.ikm(keyboard)

    # 📚 Help Menü
    def help_markup(self, _lang: dict, back=False):

        if back:
            rows = [
                [
                    self.ikb(text="⬅️ ɢᴇʀɪ", callback_data="help back"),
                    self.ikb(text="❌ ᴋᴀᴘᴀᴛ", callback_data="help close"),
                ]
            ]
        else:

            cbs = [
                "👤 ʏᴏɴᴇᴛɪᴄɪ",
                "🔑 ʏᴇᴛᴋɪ",
                "🚫 ᴇɴɢᴇʟ",
                "🌐 ᴅɪʟ",
                "🚀 ᴘɪɴɢ",
                "🎵 ᴏʏɴᴀᴛ",
                "📜 ᴋᴜʏʀᴜᴋ",
                "📊 sᴛᴀᴛs",
                "👑 sᴜᴅᴏ",
                "🏷 ᴇᴛɪᴋᴇᴛ",
                "🎮 ᴇɢ̆ʟᴇɴᴄᴇ",
            ]

            buttons = []

            for cb in cbs:
                text = _lang.get(f"help_{cb}", cb.capitalize())
                buttons.append(
                    self.ikb(text=text, callback_data=f"help {cb}")
                )

            rows = [buttons[i : i + 3] for i in range(0, len(buttons), 3)]

        return self.ikm(rows)

    # 🌍 Dil menüsü
    def lang_markup(self, _lang: str):

        langs = lang.get_languages()

        buttons = [
            self.ikb(
                text=f"{name} ({code}) {'✔️' if code == _lang else ''}",
                callback_data=f"lang_change {code}",
            )
            for code, name in langs.items()
        ]

        rows = [buttons[i : i + 2] for i in range(0, len(buttons), 2)]

        return self.ikm(rows)

    # 🏓 Ping
    def ping_markup(self, text: str):

        return self.ikm(
            [[self.ikb(text="📢 ᴅᴇsᴛᴇᴋ", url=config.SUPPORT_CHAT)]]
        )

    # ⚡ Şimdi oynat
    def play_queued(self, chat_id: int, item_id: str, _text: str):

        return self.ikm(
            [
                [
                    self.ikb(
                        text="⚡ şɪᴍᴅɪ ᴏʏɴᴀᴛ",
                        callback_data=f"controls force {chat_id} {item_id}",
                    )
                ]
            ]
        )

    # ⏯ Queue
    def queue_markup(self, chat_id: int, _text: str, playing: bool):

        action = "pause" if playing else "resume"

        return self.ikm(
            [[self.ikb(text=_text, callback_data=f"controls {action} {chat_id} q")]]
        )

    # ⚙️ Ayarlar
    def settings_markup(self, lang: dict, admin_only, cmd_delete, language, chat_id):

        return self.ikm(
            [
                [
                    self.ikb(text="🎵 ᴏʏɴᴀᴛᴍᴀ ᴍᴏᴅᴜ", callback_data="settings"),
                    self.ikb(text=admin_only, callback_data="settings play"),
                ],
                [
                    self.ikb(text="🗑 ᴋᴏᴍᴜᴛ sɪʟᴍᴇ", callback_data="settings"),
                    self.ikb(text=cmd_delete, callback_data="settings delete"),
                ],
                [
                    self.ikb(text="🌍 ᴅɪʟ sᴇᴄ̧", callback_data="settings play"),
                    self.ikb(text=lang_codes[language], callback_data="language"),
                ],
            ]
        )

    # 🚀 Start menü
    def start_key(self, lang: dict, private=False):

        rows = [
            [
                self.ikb(
                    text="➕ ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ",
                    url=f"https://t.me/{app.username}?startgroup=true",
                )
            ],
            [
                self.ikb(
                    text="📚 ʏᴀʀᴅɪᴍ ᴠᴇ ᴋᴏᴍᴜᴛʟᴀʀ",
                    callback_data="help",
                )
            ],
            [
                self.ikb(text="🔮 ᴅᴇsᴛᴇᴋ", url=f"https://t.me/The_Team_Kumsal"),
                self.ikb(text="📨 ᴅᴜʏᴜʀᴜ", url=f"https://t.me/The_Team_Kumsal"),
            ],
        ]

        if private:
            rows.append(
                [
                    self.ikb(text="👑 sᴀʜɪʙɪ", user_id=config.OWNER_ID),
                    self.ikb(text="📡 ᴋᴀʏɴᴀᴋ ᴋᴏᴅ", url="https://t.me/kaygisizlarsohbet"),
                ]
            )

        else:
            rows.append(
                [self.ikb(text="🌍 ᴅɪʟ", callback_data="language")]
            )

        return self.ikm(rows)