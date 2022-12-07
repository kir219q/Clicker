import random
import string
from gino import Gino
from gino.schema import GinoSchemaVisitor
from sqlalchemy import (Column, Integer, BigInteger, String,
                        Sequence)
from sqlalchemy import sql
from config import db_pass, db_user, host
from aiogram import types,Bot
from config import TOKEN
db = Gino()
bot = Bot(token=TOKEN, parse_mode="HTML")


class User(db.Model):
    __tablename__ = 'click'
    id = Column(Integer, Sequence('userscl'), primary_key=True)

    chat_id = Column(BigInteger)
    lang = Column(String(2))
    full_name = Column(String(100))
    score = Column(Integer)
    plus = Column(Integer)
    acscore100 = Column(Integer)
    acre = Column(Integer)
    acrescore100 = Column(Integer)
    mpvision = Column(Integer)
    mpactive = Column(Integer)
    mpinvite = Column(Integer)
    podbor = Column(Integer)
    leader = Column(Integer)
    query: sql.Select

    def __repr__(self):
        return "<click(id='{}', chat_id='{}', lang='{}', fullname='{}', score='{}', plus='{}', ascroer100='{}', " \
               "acre='{}', acrescore='{}',mpvision='{}',mpactive='{}',mpinvite='{}', leader='{}'>".format(
            self.id, self.chat_id, self.lang, self.full_name, self.score, self.plus, self.acscore100, self.acre,
            self.acrescore100, self.mpvision, self.mpactive, self.mpinvite,self.leader)


class Photo(db.Model):
    __tablename__ = 'photoclick'
    query: sql.Select

    id = Column(Integer, Sequence('photo'), primary_key=True)
    achivename = Column(String(50))
    achivephoto = Column(String(2500))


class Mp(db.Model):
    __tablename__ = 'mpclick'
    id = Column(Integer, Sequence('m'), primary_key=True)
    fighter1 = Column(BigInteger)
    fighter2 = Column(BigInteger)
    score1 = Column(Integer)
    score2 = Column(Integer)
    plus1 = Column(Integer)
    plus2 = Column(Integer)
    timer = Column(Integer)
    time1 = Column(Integer)
    time2 = Column(Integer)
    finish1 = Column(Integer)
    finish2 = Column(Integer)
    wins = Column(Integer)



class DBCommands:

    async def get_user(self, chat_id):
        user = await User.query.where(User.chat_id == chat_id).gino.first()
        return user
    async def get_user_forname(self, name):
        user = await User.query.where(User.full_name == name).gino.first()
        return user
    async def get_photo(self, x):
        y = await Photo.query.where(Photo.achivename == x).gino.first()
        return y
    async def listphoto(self, x):
        y = await Photo.query.where(Photo.id == x).gino.first()
        return y

    async def lb(self, chat_id):
        await bot.send_message(chat_id, await User.query.gino.all())

    async def add(self):
        def randomword(length):
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for i in range(length))
        new_user = User()
        new_user.full_name = randomword(13)
        new_user.score = random.randint(0, 4000)
        new_user.plus = 1
        new_user.lang = "ru"
        new_user.acscore100 = 0
        new_user.acre = 0
        new_user.acrescore100 = 0
        new_user.chat_id = -1
        new_user.leader = 1
        new_user.mpinvite = 0
        new_user.mpactive = 0
        new_user.mpvision = 1
        new_user.podbor = 0
        await new_user.create()
        return new_user

    async def add_new_user(self):
        user = types.User.get_current()
        old_user = await self.get_user(user.id)
        if old_user:
            return old_user
        new_user = User()
        new_user.chat_id = user.id
        new_user.full_name = 'nonick'
        new_user.score = 0
        new_user.plus = 1
        new_user.lang = "ru"
        new_user.acscore100 = 0
        new_user.acre = 0
        new_user.acrescore100 = 0
        new_user.mpinvite = 0
        new_user.mpactive = 0
        new_user.mpvision = 0
        new_user.leader = 0
        new_user.podbor = 0
        await new_user.create()
        return new_user
        return user

    async def add_new_photo(self, n,p):
        new_photo = Photo()
        new_photo.achivename = n
        new_photo.achivephoto = p
        await new_photo.create()
        return new_photo

    async def add_new_mp(self, u1,u2):
        new_mp = Mp()
        new_mp.fighter1 = u1
        new_mp.fighter2 = u2
        new_mp.score1 = 0
        new_mp.score2 = 0
        new_mp.plus1 = 1
        new_mp.plus2 = 1
        new_mp.timer = 60
        new_mp.finish1 = 0
        new_mp.finish2 = 0
        new_mp.wins = 0
        await new_mp.create()
        return new_mp

    async def check_cid(self, x):
        y = await User.select('chat_id').where(User.full_name == x).gino.scalar()
        return y

    async def up_score(self, x):
        user_id = types.User.get_current().id
        user = await self.get_user(user_id)
        await user.update(score=x).apply()

    async def up_lang(self, x):
        user_id = types.User.get_current().id
        user = await self.get_user(user_id)
        await user.update(lang=x).apply()

    async def up_plus(self, x):
        user_id = types.User.get_current().id
        user = await self.get_user(user_id)
        await user.update(plus=x).apply()

    async def up_full_name(self, x):
        user_id = types.User.get_current().id
        user = await self.get_user(user_id)
        await user.update(full_name=x).apply()

    async def up_lang(self, x):
        user_id = types.User.get_current().id
        user = await self.get_user(user_id)
        await user.update(lang=x).apply()

    async def up_acscore100(self, x):
        user_id = types.User.get_current().id
        user = await self.get_user(user_id)
        await user.update(acscore100=x).apply()

    async def up_acrescore100(self, x):
        user_id = types.User.get_current().id
        user = await self.get_user(user_id)
        await user.update(acrescore100=x).apply()

    async def up_acre(self, x):
        user_id = types.User.get_current().id
        user = await self.get_user(user_id)
        await user.update(acre=x).apply()

    async def up_leader(self, x):
        user_id = types.User.get_current().id
        user = await self.get_user(user_id)
        await user.update(leader=x).apply()

    async def up_mpactive(self, x):
        user_id = types.User.get_current().id
        user = await self.get_user(user_id)
        await user.update(mpactive=x).apply()

    async def up_mpinvite(self, x):
        user_id = types.User.get_current().id
        user = await self.get_user(user_id)
        await user.update(mpinvite=x).apply()

    async def up_mpvision(self, x):
        user_id = types.User.get_current().id
        user = await self.get_user(user_id)
        await user.update(mpvision=x).apply()

    async def up_podbor(self, x):
        user_id = types.User.get_current().id
        user = await self.get_user(user_id)
        await user.update(podbor=x).apply()


    async def count_users(self) -> int:
        total = await db.func.count(User.id).gino.scalar()
        return total
    async def count_photo(self) -> int:
        total = await db.func.count(Photo.id).gino.scalar()
        return total

async def create_db():
    await db.set_bind(f'postgresql://{db_user}:{db_pass}@{host}/postgres')
    db.gino: GinoSchemaVisitor
    db.gino.drop_all()
    await db.gino.create_all()

