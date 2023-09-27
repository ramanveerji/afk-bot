from bot import dp

from telegram.ext import CommandHandler, CallbackQueryHandler

from telegram import InlineKeyboardMarkup, InlineKeyboardButton

from strings import get_languages, get_string

from il import il

from secrets import SUDO_USERS


def language_buttons(languages):
    buttons = [
        InlineKeyboardButton(
            languages[language], callback_data=f"chatlang_{language}"
        )
        for language in languages
    ]
    return [buttons[i:i + 2] for i in range(0, len(buttons), 2)]


@il
def change_language(update, context, lang):
    cht, usr, msg = update.effective_chat, update.effective_user, update.effective_message

    if cht.type != "private":
        if cht.get_member(usr.id).status not in ("creator", "administrator"):
            if usr.id not in SUDO_USERS:
                return

    languages = get_languages()
    buttons = language_buttons(languages)
    msg.reply_text(get_string(lang, "clanguage"),
                   reply_markup=InlineKeyboardMarkup(buttons))


@il
def selected_language(update, context, lang):
    query = update.callback_query

    if query.message.chat.type != "private":
        if query.message.chat.get_member(query.from_user.id).status not in ("creator", "administrator"):
            if query.from_user.id not in SUDO_USERS:
                query.answer(get_string(lang, "not_admin"), show_alert=True)
                return

    data = query.data.split("_")
    selected_lang = data[1]
    context.chat_data["lang"] = selected_lang

    query.edit_message_text(get_string(selected_lang, "languagec"))


__handlers__ = [
    [CommandHandler("lang", change_language)],
    [CallbackQueryHandler(selected_language)]
]
