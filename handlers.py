import random
import DBC
from aiogram.dispatcher import FSMContext
from load_all import bot, dp, _
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from DBC import User,Mp
from keyboardru import kblang, kblistp
import keyboard
import time
import textdef
from config import admin_id
db = DBC.DBCommands()
kb = keyboard.kbf()
tx = textdef.DBCtext()
class Inv(StatesGroup):
    I1 = State()
    I2 = State()
    I3 = State()
class MpState(StatesGroup):
    M1 = State()
    M2 = State()
class Reg(StatesGroup):
    R1 = State()
    R2 = State()
class Photo(StatesGroup):
    P1 = State()
    P3 = State()
    PD = State()
class Listp(StatesGroup):
    L1 = State()
@dp.message_handler(commands=["start"])
async def register_user(message: types.Message):
    chat_id = message.from_user.id
    await db.add_new_user()
    text = "Выберите язык.\n Select a language."
    await Reg.R1.set()
    await bot.send_message(chat_id, text, reply_markup=kblang)

@dp.callback_query_handler(text_contains="ru",state=Reg.R1)
async def cancelinv(call: CallbackQuery, state: FSMContext):
    chat_id =call.from_user.id
    await db.up_lang('ru')
    text = "Введите ник."
    await Reg.R2.set()
    await bot.send_message(chat_id, text)

@dp.callback_query_handler(text_contains="en",state=Reg.R1)
async def cancelinv(call: CallbackQuery, state: FSMContext):
    chat_id =call.from_user.id
    await db.up_lang('en')
    text = "Enter your nickname."
    await Reg.R2.set()
    await bot.send_message(chat_id, text)
@dp.message_handler(state=Reg.R2)
async def regname(message: Message, state: FSMContext):
    name = message.text
    e = await db.get_user_forname(name)
    if (e == None):
        await db.up_full_name(name)
        text = _('Ваш ник доступен, вы можете начать игру /click.')
        await state.finish()
    else:
        text = _("Ваш ник занят, введите другой.")
        await Reg.R2.set()
    await message.answer(text)
@dp.message_handler(commands=["restart"])
async def register_user(message: types.Message):
    chat_id = message.from_user.id
    text = ""
    await db.up_score(0)
    await db.up_plus(1)
    u = await db.get_user(message.from_user.id)
    await db.up_acre(u.acre+1)
    if u.acscore100 == 1:
        await db.up_acscore100(2)
    if u.acre+1==1:
            p=await db.get_photo('acre')
            tex = _("Поздравляю! Вы выполнили достижение сбросить игру!")
            await message.answer(tex)
            await message.answer_photo(photo=p.achivephoto)
    textp = _("Начать  игру /click ")
    text = text+textp
    await bot.send_message(chat_id, text)
@dp.message_handler(user_id=admin_id,commands=["delphoto"])
async def delphoto1(message: types.Message):
    await message.answer("Введите название.")
    await Photo.PD.set()
@dp.message_handler(user_id=admin_id, state=Photo.PD)
async def delphoto2(message: types.Message,state: FSMContext):
    p = await db.get_photo(message.text)
    name = "nophototdeliteasdasdasdasdas"
    await p.update(achivename=name).apply()
    await message.answer("удалено")
    await state.finish()
@dp.message_handler(commands=["restartall"])
async def register_user(message: types.Message):
    u = await db.get_user(message.from_user.id)
    await u.update(score=0).apply()
    await u.update(plus =1).apply()
    await u.update(acscore100=0).apply()
    await u.update(acre=0).apply()
    await u.update(acrescore100=0).apply()
    await u.update(mpvision =0).apply()
    await u.update(mpactive=0).apply()
    await u.update(mpinvite=0).apply()
    await u.update(podbor =0).apply()
    await u.update(leader=0).apply()



@dp.message_handler(Command("click"))
async def cl(message: Message):
    text = _("Старт")
    u = await db.get_user(message.from_user.id)
    kbclick = await kb.kbclickf(u.lang)
    await message.answer(text, reply_markup=kbclick)
@dp.message_handler(Text(equals=["Author","Автор"]))
async def author(message: Message):
    text="https://www.fl.ru/users/kir219q/portfolio/#/"
    await message.answer(text)
    text="https://freelance.ru/kir219q"
    await message.answer(text)
    text="https://kwork.ru/user/kirillprom"
    await message.answer(text)
@dp.message_handler(Text(equals=["Выход","Exit"]))
async def close(message: Message):

    text = _('Продолжить /click.\n Начать заново, обнулив счет /restart')
    await message.answer(text,reply_markup=ReplyKeyboardRemove())
@dp.message_handler(Text(equals=["Клик","Click"]))
async def plus(message: Message):
    u= await db.get_user(message.from_user.id)
    await db.up_score(u.score+u.plus)
    if (u.acscore100==1)or(u.acscore100==2):
        pass
    else:
        if (u.score+u.plus>99):
            await db.up_acscore100(1)
            p = await db.get_photo('acscore100')
            text = _("Поздравляю! Вы выполнили достижение набрать 100 очков!")
            await message.answer(text)
            await message.answer_photo(photo=p.achivephoto)
    if (u.acrescore100==1):
        pass
    else:
        if (u.score+u.plus>99)and(u.acscore100==2):
            await db.up_acrescore100(1)
            p = await db.get_photo('acrescore100')
            text = _("Поздравляю! Вы выполнили достижение набрать 100 очков во второй раз!")
            await message.answer(text)
            await message.answer_photo(photo=p.achivephoto)
    text = _('Счет {k}').format(k=u.score+u.plus)
    await message.answer(text)

@dp.message_handler(Text(equals=["Достижения","Achievements"]))
async def ac(message: Message):
    text = _("Ваши достижения")
    u = await db.get_user(message.from_user.id)

    if (u.acscore100==1)or(u.acscore100==2):
        textp=_("\n Набрать 100 очков: Выполнено.")
        text = text+textp
    else:
        textp=_("\n Набрать 100 очков: Не выполнено")
        text = text+textp
    if u.acre>0:
        textp=_("\n Сбросить игру: Выполнено")
        text = text+textp
    else:
        textp=_("\n Сбросить игру: Не выполнено")
        text = text+textp
    if u.acrescore100==1:
        textp=_("\n Набрать 100 очков во второй раз (после сброса игры): Выполнено")
        text = text+textp
    else:
        textp=_("\n Набрать 100 очков во второй раз (после сброса игры): Не выполнено")
        text = text+textp
    kbclick = await kb.kbclickf(u.lang)
    await message.answer(text, reply_markup=kbclick)

@dp.message_handler(Text(equals=["Улучшить","Improve"]))
async def plus1(message: Message):
    u = await db.get_user(message.from_user.id)
    text = _("Сейчас вас счет = {k1}. Увеличение количества очков которые прибавляются за клик на один стоит {k2}. Вы хотите улучшить?").format(k1=u.score,k2=u.plus*10)
    kbplus = await kb.kbplusf(u.lang)
    await message.answer(text, reply_markup=kbplus)

@dp.callback_query_handler(text_contains="mpplusyes")
async def singplusyes(call: CallbackQuery):

    u = await db.get_user(call.from_user.id)
    if u.score > (u.plus * 10 - 1):
        await db.up_score(u.score - 10 * u.plus)
        await db.up_plus(u.plus + 1)
        text = _("Прибавление очков увеличено на один. Теперь оно = {k1}. Счет теперь равен {k2}").format(k1=u.plus + 1,k2=u.score - u.plus * 10)
        await call.message.edit_text(text)
    else:
        text = _("На счете слишком мало очков.")
        await call.message.edit_text(text)
@dp.message_handler(Text(equals=["Поддержать автора","Support the author"]))
async def pat(message: Message):
    text = "www.patreon.com/KirillBots"
    await message.answer(text)

@dp.message_handler(Text(equals=["Лидеры","Leaderboard"]))
async def ac(message: Message):
    k = await db.count_users()
    l = [[-1,'v']]
    i = 1
    n = 0
    while i<k+1:
        user = await User.query.where(User.id == i).where(User.leader == 1).gino.first()
        if user ==None:
            pass
        else:
            lp = [[user.score, user.full_name]]
            l.extend(lp)
            n=n+1
        i = i+1
    text =_('Топ 5:')
    l.sort()
    i = 0
    if n>4:
        while i<5:
            textp=_('\n {k1}  {k2}').format(k1=l[n-i][1],k2=l[n-i][0])
            text = text+textp
            i = i+1
    else:
        while i<n:
            textp=_('\n {k1}  {k2}').format(k1=l[n-i][1],k2=l[n-i][0])
            text = text+textp
            i=i+1
    await message.answer(text)
@dp.message_handler(Text(equals="Список игроков"))
async def mplist(message:Message):
    k = await db.count_users()
    l = [["f"]]
    i = 1
    text=_("Пять случайных игроков:")
    n= 0
    while i<k+1:
        user = await User.query.where(User.id == i).where(User.mpvision==1).gino.first()
        if user == None:
            pass
        else:
            lp = [user.full_name]
            l.extend(lp)
            n=n+1
        i=i+1
    i = 0
    while i<5:
        r = random.randint(1, n)
        text+=('\n {k1}').format(k1=l[r])
        i = i+1
    await message.answer(text)
@dp.message_handler(user_id=admin_id, commands=['photolist'])
async def photolist1(message:types.Message, state: FSMContext):
    i=1
    text=""
    c =await db.count_photo()
    if i+4<c:
        while i<6:
            p=await db.listphoto(i)
            text+=f"\n{p.achivename}\n{p.achivephoto} \n КОНЕЦ\n"
            i=i+1
        await message.answer(text,reply_markup=kblistp)
        await Listp.L1.set()
        await state.update_data(i=i)
    else:
        while i<c+1:
            p=await db.listphoto(i)
            text+=f"\n{p.achivename}\n{p.achivephoto} \n КОНЕЦ\n"
            i=i+1
        await message.answer(text)
@dp.callback_query_handler(text_contains="nextp",state=Listp.L1)
async def photolist2(call: CallbackQuery, state: FSMContext):
    id= call.from_user.id
    data = await state.get_data()
    i=data.get("i")
    text=""
    c =await db.count_photo()
    if i+4<c:
        i2=i+5
        while i<i2:
            p=await db.listphoto(i)
            text+=f"\n{p.achivename}\n{p.achivephoto} \n КОНЕЦ\n"
            i=i+1
        await bot.send_message(id,text,reply_markup=kblistp)
        await state.update_data(i=i)
    else:
        while i<c+1:
            p=await db.listphoto(i)
            text+=f"\n{p.achivename}\n{p.achivephoto} \n КОНЕЦ\n"
            i=i+1
            await state.finish()
        await bot.send_message(id,text)
@dp.callback_query_handler(text_contains="exitp",state=Listp.L1)
async def photolistexit(call: CallbackQuery, state: FSMContext):
    id=call.from_user.id
    await state.finish()
    await bot.send_message(id,"/click")
@dp.message_handler(user_id=admin_id, commands=['addphoto'])
async def add_photo1(message:types.Message, state: FSMContext):
    await Photo.P1.set()
    await message.answer("Скинь название")

@dp.message_handler(user_id=admin_id, state=Photo.P1)
async def add_photo2(message:types.Message, state: FSMContext):
    name = message.text
    await message.answer("Скинь фото.")
    await state.update_data(name=name)
    await Photo.P3.set()
@dp.message_handler(user_id=admin_id,state=Photo.P3, content_types=types.ContentType.PHOTO)
async def add_photo(message: types.Message,state: FSMContext):
    photo = message.photo[-1].file_id
    data = await state.get_data()
    name = data.get("name")
    await db.add_new_photo(name, photo)
    await message.answer("Фото полученно.")
    await state.finish()
@dp.message_handler(Command("adm"),user_id=admin_id)
async def adm(message: types.Message):
    await message.answer("+")
@dp.message_handler(Command("add"),user_id=admin_id)
async def add(message: types.Message):
    await db.add()
@dp.message_handler(Text(equals=["PvP"]))
async def ac(message: Message):
    id = message.from_user.id
    u = await db.get_user(id)
    text = _("Выберите пункт в меню ")
    kbpvp = await kb.kbpvpf(u.lang)
    await message.answer(text,reply_markup=kbpvp)

@dp.message_handler(Text(equals=["Настройки","Settings"]))
async def seting(message:Message):
    id = message.from_user.id
    u = await db.get_user(id)
    text = await tx.textset(message.from_user.id)
    kbseting = await kb.kbsetingf(u.lang)
    await message.answer(text, reply_markup=kbseting)
@dp.callback_query_handler(text_contains="seting1")
async def setmpinvite(call: CallbackQuery):
    id = call.from_user.id
    u = await db.get_user(id)
    if u.mpinvite == 0:
        await db.up_mpinvite(1)
    else:
        await db.up_mpinvite(0)
        await db.up_mpvision(0)
    text = await tx.textset(id,id)
    kbseting = await kb.kbsetingf(u.lang)
    await call.message.edit_text(text, reply_markup=kbseting)
@dp.callback_query_handler(text_contains="seting2")
async def setmpvision(call: CallbackQuery):
    id = call.from_user.id
    u = await db.get_user(id)
    if u.mpvision == 0:
        await db.up_mpvision(1)
        await db.up_mpinvite(1)
    else:
        await db.up_mpvision(0)
    text = await tx.textset(id,id)
    kbseting = await kb.kbsetingf(u.lang)
    await call.message.edit_text(text, reply_markup=kbseting)
@dp.callback_query_handler(text_contains="seting3")
async def setlead(call: CallbackQuery):
    id = call.from_user.id
    u = await db.get_user(id)
    if u.leader == 0:
        await db.up_leader(1)
    else:
        await db.up_leader(0)
    text = await tx.textset(id,id)
    kbseting = await kb.kbsetingf(u.lang)
    await call.message.edit_text(text, reply_markup=kbseting)

@dp.callback_query_handler(text_contains="setinglang")
async def setlang(call: CallbackQuery):
    id = call.from_user.id
    u = await db.get_user(id)
    if u.lang == 'ru':
        await db.up_lang('en')
        text = "The language has been changed."
        kbclick= await kb.kbclickf('en')
    else:
        await db.up_lang('ru')
        text = "Язык изменен."
        kbclick= await kb.kbclickf('ru')
    await call.message.delete()
    await bot.send_message(id,text, reply_markup=kbclick)

@dp.callback_query_handler(text_contains="setingname")
async def setlead(call: CallbackQuery):
    text = _('Введите новый ник.')
    await Reg.R2.set()
    await bot.send_message(call.from_user.id,text, reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(Text(equals=["PvP сражение по нику","PvP battle by nickname"]))
async def mpinv0(message: Message):
    u = await db.get_user(message.from_user.id)
    if u.mpinvite == 0:
        text = _("Чтобы пригласить другого игрока, вам нужно разрешить приглашать себя. Вы можете сделать это в настройках")
        await message.answer(text)
        id = message.from_user.id
        text = await tx.textset(id,id)
        kbseting = await kb.kbsetingf(u.lang)
        await message.answer(text, reply_markup=kbseting)
    else:
        text = _("Введите длительность боя в секундах (рекомендуется 60 секунд).")
        await Inv.I1.set()
        await message.answer(text, reply_markup=None)

@dp.message_handler(state=Inv.I1)
async def mpinv2(message: Message, state: FSMContext):
    u = await db.get_user(message.from_user.id)
    t = int(message.text)
    await db.add_new_mp(u.chat_id,-1)
    f = await Mp.query.where(Mp.fighter1 == u.chat_id).where(Mp.fighter2==-1).gino.first()
    await f.update(timer=t).apply()
    await f.update(finish1=2).apply()
    await f.update(finish2=2).apply()
    text = _("Введите ник (в игре) игрока с которым хотите сразиться.")
    await Inv.I2.set()
    await message.answer(text)

@dp.message_handler(state=Inv.I2)
async def mpinv2(message: Message, state: FSMContext):
    name = message.text
    e = await db.get_user_forname(name)
    u = await db.get_user(message.from_user.id)
    f = await Mp.query.where(Mp.fighter1 == u.chat_id).where(Mp.fighter2 == -1).gino.first()
    if e == None:
        text = _("Данный пользователь не существует, либо не разрешает приглашать себя в сражения.")
        await state.finish()
        await f.delete()
        kbpvp = await kb.kbpvpf(u.lang)
        await message.answer(text, reply_markup=kbpvp)
    else:
        if e.mpactive == 1:
            text = _("Данный пользователь сейчас находится в другом пвп сражении. Отправьте ему приглашение позднее.")
            await state.finish()
            await f.delete()
            kbpvp = await kb.kbpvpf(u.lang)
            await message.answer(text, reply_markup=kbpvp)
        else:
            if e.mpinvite == 1:
                await f.update(fighter2=e.chat_id).apply()
                text = _("Вас приглашают в PvP сражение. Длительностью в {k1} секунд. Имя игрока:").format(k1=f.timer)
                await bot.send_message(e.chat_id,text)
                text =f'{u.full_name}'
                kbmpinv = await kb.kbmpinvf(u.lang)
                await bot.send_message(e.chat_id, text, reply_markup=kbmpinv)
                text = _("Ваше приглашение отправлено дождитесь ответа.")
                await Inv.I3.set()
                kbinvcancel = await kb.kbinvcancelf(u.lang)
                await message.answer(text,reply_markup=kbinvcancel)
            else:
                text = _("Данный пользователь не существует, либо не разрешает приглашать себя в сражения.")
                await state.finish()
                await f.delete()
                kbpvp = await kb.kbpvpf(u.lang)
                await message.answer(text,reply_markup=kbpvp)
@dp.callback_query_handler(text_contains="mpinvcancel",state=Inv.I3)
async def cancelinv(call: CallbackQuery, state: FSMContext):
    u = await db.get_user(call.from_user.id)
    f = await Mp.query.where(Mp.fighter1 == u.chat_id).where(Mp.finish1 == 2).gino.first()
    await f.delete()
    text = _("Приглашение отмененно")
    await state.finish()
    await bot.send_message(u.chat_id,text)
@dp.callback_query_handler(text_contains="mpyes",state=Inv.I3)
async def yesinv(call: CallbackQuery, state: FSMContext):
    u = await db.get_user(call.from_user.id)
    name=call.message.text
    e = await db.get_user_forname(name)
    f = await Mp.query.where(Mp.fighter1 == e.chat_id).where(Mp.finish1 == 2).where(Mp.fighter2 ==u.chat_id).gino.first()
    await f.update(finish1=0).apply()
    await f.update(finish2=0).apply()
    text = _("Начать игру.")
    kbmpstart = await kb.kbmpstartf(u.lang)
    await bot.send_message(e.chat_id, text, reply_markup=kbmpstart)
    kbmpstart = await kb.kbmpstartf(e.lang)
    await bot.send_message(u.chat_id, text, reply_markup=kbmpstart)

@dp.callback_query_handler(text_contains="mpno",state=Inv.I3)
async def cancelinv(call: CallbackQuery, state: FSMContext):
    u = await db.get_user(call.from_user.id)
    name=call.message.text
    e = await db.get_user_forname(name)
    f = await Mp.query.where(Mp.fighter1 == e.chat_id).where(Mp.finish1 == 2).where(Mp.fighter2 ==u.chat_id).gino.first()
    await f.delete()
    text= _("Приглашение отклоненно.")
    await bot.send_message(u.chat_id,text)
    kbok = await kb.kbokf(u.lang)
    await bot.send_message(e.chat_id,text,reply_markup=kbok)



@dp.callback_query_handler(text_contains="mpok",state=Inv.I3)
async def mpok(call: CallbackQuery, state: FSMContext):
    u = await db.get_user(call.from_user.id)
    await call.message.delete()
    text = _("Счет: {k1}").format(k1=u.score)
    await state.finish()
    kbclick = await kb.kbclickf(u.lang)
    await bot.send_message(u.chat_id,text,reply_markup=kbclick)
@dp.message_handler(Text(equals=["Подбор игроков PvP сражения", "Selection of PvP battle players"]))
async def pod(messege:Message):
    u = await db.get_user(messege.from_user.id)
    if u.podbor == 1:
        text = _("Вы уже начали подбор.")
        await messege.answer(text)
        text = _("Отменить поиск.")
        kbcancelpodbor = await kb.kbcancelpodborf(u.lang)
        await messege.answer(text, reply_markup=kbcancelpodbor)
    else:
        e = await User.query.where(User.podbor == 1).gino.first()
        if e == None:
            await db.up_podbor(1)
            text = _("Бой длится 60 секунд. Ожидайте. Пока ваш соперник не найден. В это время вы можете поиграть в одиночном режиме")
            kbclick = await kb.kbclickf(u.lang)
            await messege.answer(text,reply_markup=kbclick)
            text = _("Отменить поиск.")
            kbcancelpodbor = await kb.kbcancelpodborf(u.lang)
            await messege.answer(text,reply_markup=kbcancelpodbor)
        else:
            await e.update(podbor=1).apply()
            text = _("Соперник найден. Бой длиться 60 секунд.")
            await db.up_mpactive(1)
            await e.update(mpactive=1).apply()
            await db.add_new_mp(e.chat_id,u.chat_id)
            await bot.send_message(e.chat_id, text, reply_markup=None)
            await messege.answer(text, reply_markup=None)
            text = _("Начать игру.")
            kbmpstart = await kb.kbmpstartf(e.lang)
            await bot.send_message(e.chat_id, text, reply_markup=kbmpstart)
            kbmpstart = await kb.kbmpstartf(u.lang)
            await messege.answer(text, reply_markup=kbmpstart)
@dp.callback_query_handler(text_contains="cancelpodbor")
async def cancelpodbor(call: CallbackQuery):
    u = await db.get_user(call.from_user.id)
    await u.update(podbor=0).apply()
    text=_("Подбор отменён")
    await bot.send_message(u.chat_id,text)
@dp.callback_query_handler(text_contains="mpstart")
async def mpstart(call:CallbackQuery):
    u= await db.get_user(call.from_user.id)
    t = round(time.time())
    f = await Mp.query.where(Mp.fighter1 == u.chat_id).where(Mp.finish1==0).gino.first()
    if f == None:
        f = await Mp.query.where(Mp.fighter2 == u.chat_id).where(Mp.finish2 == 0).gino.first()
        if f==None:
            pass
        else:
            await MpState.M2.set()
            await f.update(time2=t+f.timer).apply()
            text=_("Счет {k1}").format(k1=f.score2)
            kbmp = await kb.kbmpf(u.lang)
            await bot.send_message(f.fighter2,text,reply_markup=kbmp)
    else:
        await MpState.M1.set()
        await f.update(time1=t + f.timer).apply()
        await call.message.delete()
        text = _("Счет {k1}").format(k1=f.score1)
        kbmp = await kb.kbmpf(u.lang)
        await bot.send_message(f.fighter1, text, reply_markup=kbmp)
@dp.callback_query_handler(text_contains="mpstart",state=Inv.I3)
async def mpstart(call:CallbackQuery):
    u= await db.get_user(call.from_user.id)
    t = round(time.time())
    f = await Mp.query.where(Mp.fighter1 == u.chat_id).where(Mp.finish1==0).gino.first()
    if f == None:
        f = await Mp.query.where(Mp.fighter2 == u.chat_id).where(Mp.finish2 == 0).gino.first()
        if f==None:
            pass
        else:
            await MpState.M2.set()
            await f.update(time2=t+f.timer).apply()
            text=_("Счет {k1}").format(k1=f.score2)
            kbmp = await kb.kbmpf(u.lang)
            await bot.send_message(f.fighter2,text,reply_markup=kbmp)
    else:
        await MpState.M1.set()
        await f.update(time1=t + f.timer).apply()
        await call.message.delete()
        text = _("Счет {k1}").format(k1=f.score1)
        kbmp = await kb.kbmpf(u.lang)
        await bot.send_message(f.fighter1, text, reply_markup=kbmp)

@dp.message_handler(Text(equals=["Клик","Click"]),state=MpState.M1)
async def mpcl1(message: Message,state: FSMContext):
    u= await db.get_user(message.from_user.id)
    t = round(time.time())
    f = await Mp.query.where(Mp.fighter1 == u.chat_id).where(Mp.finish1==0).gino.first()
    if t > f.time1:
        await state.finish()
        await f.update(finish1=1).apply()
        text = _("Время вышло. Ваш счет {k1}.").format(k1=f.score1)
        if f.finish2 == 0:
            textp= _('\n Ваш соперник еще не закончил игру. Когда он сделает это вам придёт сообщение.')
            text=text+textp
            kbclick = await kb.kbclickf(u.lang)
            await message.answer(text, reply_markup=kbclick)
        else:
            texte = _('Ваш соперник {k1} закончил.').format(k1=u.full_name)
            textp= _('\n Счет вашего соперника {k1}').format(k1=f.score2)
            text= text+textp
            textep= _('\n Счет вашего соперника {k1}').format(k1=f.score1)
            texte=texte+textep
            if f.score1 > f.score2:
                textp= _('\n Вы победили.')
                text =text+textp
                textep= _('\n Вы проиграли.')
                texte=texte+textep
                await f.update(wins=1).apply()
            if f.score1 < f.score2:
                textp = _('\n Вы проиграли.')
                text = text+textp
                textep = _('\n Вы победили.')
                texte=texte+textep
                await f.update(wins=2).apply()
            if f.score1 == f.score2:
                textp= _('\n Ничья.')
                text =text+textp
                textep= _('\n Ничья.')
                texte=texte+textep
                await f.update(wins=3).apply()
            kbclick = await kb.kbclickf(u.lang)
            await message.answer(text, reply_markup=kbclick)
            await bot.send_message(f.fighter2, texte)
    else:
        await f.update(score1=f.score1 + f.plus1).apply()
        text = _('Счет {k1}').format(k1=f.score1)
        await message.answer(text)
@dp.message_handler(Text(equals=["Клик","Click"]),state=MpState.M2)
async def mpcl2(message: Message,state: FSMContext):
    u= await db.get_user(message.from_user.id)
    t = round(time.time())
    f = await Mp.query.where(Mp.fighter2 == u.chat_id).where(Mp.finish2==0).gino.first()
    if t > f.time2:
        await db.up_mpactive(0)
        await state.finish()
        await f.update(finish2=1).apply()
        text = _('Время вышло ваш счет {}.').format(k1=f.score2)
        if f.finish1 == 0:
            textp= _('\n Ваш соперник еще не закончил игру. Когда он сделает это вам придёт сообщение.')
            text = text+textp
            kbclick = await kb.kbclickf(u.lang)
            await message.answer(text, reply_markup=kbclick)
        else:
            texte = _('Ваш соперник {k1} закончил .').format(k1=u.full_name)
            textp= _('\n Счет вашего соперника {k1}').format(k1=f.score1)
            textep= _('\n Счет вашего соперника {k1}').format(k1=f.score2)
            text = text+textp
            texte = texte+textep
            if f.score2 > f.score1:
                textp= _('\n Вы победили.')
                textep= _('\n Вы проиграли.')
                text = text + textp
                texte = texte + textep
                await f.update(wins=2).apply()
            if f.score2 < f.score1:
                textp = _('\n Вы проиграли.')
                textep = _('\n Вы победили.')
                text = text + textp
                texte = texte + textep
                await f.update(wins=1).apply()
            if f.score2 == f.score1:
                textp = _('\n Ничья.')
                textep = _('\n Ничья.')
                text = text + textp
                texte = texte + textep
                await f.update(wins=3).apply()
            kbclick = await kb.kbclickf(u.lang)
            await message.answer(text, reply_markup=kbclick)
            await bot.send_message(f.fighter1, texte)
    else:
        await f.update(score2=f.score2 + f.plus2).apply()
        text = _('Счет {k1}').format(k1=f.score2)
        await message.answer(text)


@dp.message_handler(Text(equals=["Улучшить","Improve"]),state=MpState.M1)
async def mpplus1(message: Message,state: FSMContext):
    u= await db.get_user(message.from_user.id)
    f = await Mp.query.where(Mp.fighter1 == u.chat_id).where(Mp.finish1==0).gino.first()
    text = _("Сейчас вас счет = {k1}. Увеличение количества очков которые прибавляются за клик на один стоит {k2}. Вы хотите улучшить?").format(k1=f.score1,k2=f.plus1*10)
    kbplus = await kb.kbplusf(u.lang)
    await message.answer(text, reply_markup=kbplus)
@dp.message_handler(Text(equals=["Улучшить","Improve"]),state=MpState.M2)
async def mpplus2(message: Message,state: FSMContext):
    u= await db.get_user(message.from_user.id)
    f = await Mp.query.where(Mp.fighter2 == u.chat_id).where(Mp.finish2==0).gino.first()
    text = _("Сейчас вас счет = {k1}. Увеличение количества очков которые прибавляются за клик на один стоит {k2}. Вы хотите улучшить?").format(k1=f.score2,k2=f.plus2*10)
    kbplus = await kb.kbplusf(u.lang)
    await message.answer(text, reply_markup=kbplus)


@dp.callback_query_handler(text_contains="mpplusyes",state=MpState.M1)
async def mpplusyes1(call: CallbackQuery):
    u = await db.get_user(call.from_user.id)
    f = await Mp.query.where(Mp.fighter1 == u.chat_id).where(Mp.finish1==0).gino.first()
    if f.score1 > (f.plus1 * 10 - 1):
        await db.up_score(f.score1 - 10 * f.plus1)
        await f.update(score1=f.score1-f.plus1*10).apply()
        await f.update(plus1=f.plus1+1).apply()
        text = _("Прибавление очков увеличено на один. Теперь оно = {k1}. Счет теперь равен {k2}").format(k1=f.plus1,k2=f.score1)
        await call.message.edit_text(text)
    else:
        text = _("На счете слишком мало очков.")
        await call.message.edit_text(text)
@dp.callback_query_handler(text_contains="mpplusyes",state=MpState.M2)
async def mpplusyes2(call: CallbackQuery):
    u = await db.get_user(call.from_user.id)
    f = await Mp.query.where(Mp.fighter2 == u.chat_id).where(Mp.finish2==0).gino.first()
    if f.score2 > (f.plus2 * 10 - 1):
        await db.up_score(f.score2 - 10 * f.plus2)
        await f.update(score2=f.score2-f.plus2*10).apply()
        await f.update(plus2=f.plus2+1).apply()
        text = _("Прибавление очков увеличено на один. Теперь оно = {k1}. Счет теперь равен {k2}").format(k1=f.plus2,k2=f.score2)
        await call.message.edit_text(text)
    else:
        text = _("На счете слишком мало очков.")
        await call.message.edit_text(text)