from DBC import User,Mp
from load_all import _

class DBCtext:
    async def textset(self, x):
        u = await User.query.where(User.chat_id == x).gino.first()
        text = _("Ваш ник: {k1}.\n").format(k1=u.full_name)
        if u.mpinvite == 0:
            textp = _("1)Вас нельзя пригашать в пвп сражения.\n")
            text = text+textp
        else:
            textp = _("1)Вас можно приглашать в пвп сражения.\n")
            text = text+textp
        #if u.mpvision == 0:
        #    textp = _("2)Ваш ник не отображается в списке игроков мультиплеера.\n")
        #    text = text+textp
        #else:
        #    textp = _("2)Ваш ник отображается в списке игроков мультиплеера.\n")
        #    text = text+textp
        if u.leader == 0:
            textp = _("2)Ваш ник не отображается в списке лидеров.\n")
            text = text+textp
        else:
            textp = _("2)Ваш ник отображается в списке лидеров.\n")
            text = text+textp
        if u.lang == 'ru':
            text += "Язык: Русский\n"
        else:
            text +="Language: English\n"

        textp = _("Какой пункт вы хотите изменить?")
        text = text + textp
        return text