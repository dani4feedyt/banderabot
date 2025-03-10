try:
    import time

    start_time = time.time()

    import datetime
    import inspect
    import discord
    from discord import app_commands
    import discord.ui
    from discord.ext import commands, tasks
    from discord.ext.commands import has_permissions, MissingPermissions
    from Bandera_cfg import settings
    from Bandera_Quotes import quotes, n_1
    from func_txt_f import *
    from rules import *
    from txt_f import *
    from sys import argv, executable
    import json
    import requests
    import os
    import sys
    import random
    import re
    from random import randint
    from urllib.request import urlopen
    import lxml
    from lxml import html
    from collections import Counter
    import asyncio
    import asyncstdlib
    from asyncio import sleep
    from selenium import webdriver
    from bs4 import BeautifulSoup
    from datetime import date
    from image_rec import imagery
    from db_handler import engine, cur
    from psycopg2.extras import Json

    from Views import Select
    from player import Player


    #############################################__ИДЕИ__#############################################
    #1. Сделать предварительный выбор языка в b!info.
    #2. Написать универсальную распознавалку текстового ответа как функцию (например как в 150:17).
    #############################################__ИДЕИ__#############################################

    bot = commands.Bot(command_prefix=settings["prefix"], intents=discord.Intents.all())
    version = "release 3.3"
    patch_note = "last updated: 06.04.24"
    w = "Bandera_bot.py"
    today = datetime.date.today()
    # img_id = 0
    print(today)

    spam = True
    url = None
    irritation = 0

    main_ch_id = 695715314696061072
    bpg_guild_id = 1338461268473806858

    months = {"jan": 31, "feb": 28, "mar": 31, "apr": 30, "may": 31, "jun": 30, "jly": 31, "aug": 31, "sep": 30, "oct": 31, "nov": 30, "dec": 31}
    if today.year % 4 == 0:
        months["feb"] = 29

    player_inst = Player()

    def check(ctx, msg, check_list):
        if msg.author == ctx.author:
            if any(msg.content.lower() == i for i in check_list):
                return msg.content.lower()

    @bot.event
    async def on_command(ctx):
        print(f"Triggered... <{ctx.command}>; server: <{ctx.guild.name}>; channel: <{ctx.channel.name}>; user: <{ctx.message.author}>")

    @bot.event
    async def on_member_join(member):
        await member.send(f"Вітаю тебе на сервері **{member.guild.name}**!\n"
                          f"Я - **Бандера бот**, найгеніальніший бот, створений *@dani4feedyt#5200*, який можливо навіть колись якось вам допоможе!\n\n"
                          f"Існує спеціальний лист **правил** спілкування зі мною, яких ти **маєш притримуватися**.\n"
                          f"Якщо на цьому сервері є канал **#правила**, можеш із ними ознайомитися.\n"
                          f"У випадку коли такого каналу немає, мої правила можна побачити використавши команду **b!rules**\n\n"
                          f"Для отримання більш розгорнутої інформації щодо мого функціоналу, скористайся **b!info**")
        await member.send("https://media.discordapp.net/attachments/810509408571359293/919313856159965214/kolovrat1.gif")
        await member.guild.system_channel.send(f"Ласкаво просимо на сервер **{member.guild.name}**, {member.mention}!"
                                                                f" Наші ряди поповнилися ще одним гідним (?) націоналістом. "
                                                                f"Нас вже аж **{len(member.guild.members)}**!")

    @bot.event
    async def on_voice_state_update(member, before, after):
        if before.channel is None and after.channel:
            m_id = member.id
            print(m_id)
            cur.execute(f"SELECT iter_left FROM kanava_servers WHERE kanava_servers.server_id = %s AND kanava_servers.user_id = %s",
                        [member.guild.id, member.id])
            data = cur.fetchone()
            engine.commit()
            if data:
                message = await member.guild.system_channel.send(f"Канава активована для користувача {member.mention}", delete_after=10)
                ctx = await bot.get_context(message)
                await kanava(ctx, member=member, t=data[0])
                print(data[0])

    @bot.event
    async def on_ready():
        await bot.change_presence(activity=discord.Game("дупі своїм пальчиком | b!info"))
        main_daily_pic.start()

    @tasks.loop(hours=24)
    async def main_daily_pic():
        dw = str(datetime.datetime.today().weekday())
        for guild in bot.guilds:
            print(guild)
            print(guild.id)
            img_g = await guild.system_channel.send(file=discord.File(f"d_t{dw}.png"))

            cur.execute("SELECT img_message_id FROM img_data WHERE guild_id = %s;", [guild.id])

            msg = await guild.system_channel.fetch_message(int(cur.fetchall()[0][0]))
            await msg.delete()

            cur.execute(f"UPDATE img_data SET img_message_id = %s, guild_id = %s WHERE guild_id = %s;", [img_g.id, guild.id, guild.id])
            engine.commit()


    @main_daily_pic.before_loop
    async def before_main_daily_pic():
        for _ in range(60*60*24):
            if str(datetime.datetime.now().hour) == '7' and str(datetime.datetime.now().minute) == "30":
                return
            await asyncio.sleep(30)


    @bot.command(name="sync", description="Owner only")# Global - Local - CL (for instant implement)
    async def sync(ctx, globally=None):
        if ctx.author.id == 486176412953346049:
            if not globally:
                bot.tree.copy_global_to(guild=discord.Object(id=ctx.guild.id))
                await bot.tree.sync(guild=discord.Object(id=ctx.guild.id))
                await ctx.send("Command tree test-synced for this server.")
            elif globally == "cl":
                bot.tree.clear_commands(guild=discord.Object(id=ctx.guild.id))
                await bot.tree.sync(guild=discord.Object(id=ctx.guild.id))
                await ctx.send("Command tree cleared for this server.")
            else:
                await bot.tree.sync()
                await ctx.send("Command tree synced globally.")
        else:
            await ctx.send("Permission error, why are you trying to do this, exactly?")

    @bot.tree.command(
        name="slavaukraine",
        description="Патріотично"
    )
    async def slash_command(interaction):
        await interaction.response.send_message("Героям слава, друже.")

    @bot.tree.command(
        name="ticktacktoe",
        description="Зіграти в хрестики-нолики зі мною"
        )
    async def ticktacktoe(interaction):
        await interaction.response.send_message("Ну що, готовий до гри?\n**Обирай гравця:**", view=Select())

    @bot.tree.context_menu(name="Identify")
    async def identify(interaction, message: discord.Message):
        await interaction.response.send_message(f"*Хмм... дайте поміркувати...*")
        last_img = f"src/last_img.jpg"

        if message.attachments:
            im_url = message.attachments[0].url
        else:
            await interaction.response.send_message(f"**Помилка**. У повідомленні відсутнє зображення.")
            return

        file = requests.get(im_url)
        open(last_img, "wb").write(file.content)

        lable_list = imagery(last_img, 5)##5 lables output
        output_labels = str()
        for i in range(len(lable_list[0])):
            output_labels += lable_list[0][i]
            output_labels += f" *({lable_list[1][i]})*"
            if i < len(lable_list[0]) - 1:
                output_labels += "; "
        await interaction.edit_original_response(content=f"Я гадаю, що це... {output_labels}")


    # TODO Указать в таблице правил количество наказания в минутах

    @bot.event
    async def on_message(message):
        if message.author.id == 783069117602857031:
            await bot.process_commands(message)

        else:
            if "b!" not in message.content:
                if rule_mes(message):
                    ctx = await bot.get_context(message)
                    await mute(ctx, member=message.author, time=3, rule_n=rule_mes(message), bot_source=True)
                    return

                if "бандер" in message.content.lower():
                    await message.channel.send("Мене хтось кликав?")
                    try:
                        await bot.wait_for("message", check=lambda msg: check(message, msg, checklists[0]), timeout=15)
                    except asyncio.TimeoutError:
                        await message.channel.send("Гаразд, мені певно здалося...")
                    else:
                        await message.channel.send("Що сталося?")
                        try:
                            await bot.wait_for("message", check=lambda msg: check(message, msg, checklists[2]), timeout=15)
                        except asyncio.TimeoutError:
                            a_list = [0, 1]
                            distribution = [.9, .1]
                            rand = random.choices(a_list, distribution)
                            await message.channel.send("Я взагалі-то маю свої справи, прошу не відволікати! Якщо є якісь проблеми, напишіть **b!info**, або зверніться до " + "<@" + str(486176412953346049) + ">")
                            if rand == [1]:
                                await message.channel.send(file=discord.File('b2.png'))
                        else:
                            if str(today) == f"{today.year}-01-01":
                                await message.channel.send(f"**Дякую тобі, {random.choice(appeal)}!** Не думав, що хтось згадає про мене...")
                            else:
                                await message.channel.send(f"Вельми дякую, {random.choice(appeal)}, але ти, певно, помилився. Мій день народження **1 січня**.")
                            await asyncio.sleep(7)
                            await message.channel.send("Гаразд, пішов я по своїх справах...")

                else:
                    await bot.process_commands(message)

            else:
                await bot.process_commands(message)


    def rule_mes(sentence):
        for rule in trigger_list:
            for word in trigger_list[rule]:
                if word in sentence.content.lower():
                    return rule
        return False


    @bot.listen()
    async def on_message(message):
        msg = message.content.lower()

        if message.author.bot:
            return

        if any(i in msg for i in ["підр", "пидр", "счита", "раху", "pidr", "count", "пiдр"]):

            if bool(re.search(r'\d', msg)):

                if ',' in msg:
                    msg = str(msg).replace(',', '.')

                tuple_part = re.split(' ', msg)
                outstring = ''.join(re.findall(r'[-+/()*^.]?\d?', ''.join(tuple_part)))
                func = outstring.replace('^', '**')
                # print(func)
                solution = eval(func)
                if len(str(solution)) <= 64:
                    await message.channel.send(solution)
                else:
                    await message.channel.send("**Помилка.** Результат довший за 64 символа, тому не може бути надісланий у повідомленні.")

        if "іді" in msg:
            await message.channel.send("<:idi_nahui:1197676923745226822>")


    @bot.tree.command(
        name="fetchid",
        description="Типувати користувача",
    )
    #@has_permissions(manage_messages=True)
    async def id(interaction, member: discord.User):
        await interaction.response.send_message(f"{member.name}, {member.id}, {datetime.datetime.now().time()}")

    @bot.command(name="fetch timestamp")
    async def fetch(ctx, msg_id: int):
        msg = await ctx.fetch_message(msg_id)
        timestamp = msg.created_at
        timestamp = timestamp + datetime.timedelta(hours=2)
        await ctx.send(timestamp)


    @bot.command(name="play")
    async def play(ctx, url: str):
        message = await ctx.send("Шукаю музику за посиланням...")

        player_inst.set_url(url)
        if discord.utils.get(bot.voice_clients, guild=ctx.guild):
            print("disconnected")
            discord.utils.get(bot.voice_clients, guild=ctx.guild).stop()
        await asyncio.sleep(1)

        if os.path.exists("downloads"):
            player_inst.flush_all()
        await player_inst.download()
        path = player_inst.get_audio_path()

        author = ctx.message.author

        voice_channel = author.voice.channel
        print(voice_channel)
        if not discord.utils.get(bot.voice_clients, guild=ctx.guild):
            await voice_channel.connect()
        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

        voice.play(discord.FFmpegOpusAudio(executable="ffmpeg/bin/ffmpeg.exe", source = path))
        await message.delete()
        await ctx.send(f"Розпочато відтворення треку: \n**<<{player_inst.get_filename()}>>**")

        await asyncio.sleep(player_inst.length()+180)
        await player_inst.stop(voice)


    @bot.command(name="rg_8421")
    async def rg8421(ctx):
        author = ctx.message.author
        await ctx.send(f"<@{str(696670757794742322)}>, {author.mention} зазіхнув на головну тайну калу та дізнався рецепт надчистого лайна: \n||Гівно + Гівно - Гівно + Крапелька поносу та три крапельки гівна високої концентрації||")

    @bot.command(name="rates")
    async def rates(ctx, amount, *, rate):
        val = None
        name = None
        rate = rate.lower()

        wait_msg = await ctx.send(f"*Підрахування...*", delete_after=10)
        page1 = requests.get("https://bank.gov.ua/ua/markets/exchangerates?date=today&period=daily")
        soup = BeautifulSoup(page1.content, "html.parser")

        date = soup.find("span", {"id": "exchangeDate"}).get_text()

        def parser(currency: int, decimal: bool):
            c_rate = soup.find_all("td", {"data-label": "Офіційний курс"})[currency].get_text()
            c_rate = float(c_rate.replace(',', '.'))
            if decimal:
                c_rate /= 10
            return round(c_rate, 2)

        for x in nondec:
            if any(i in rate for i in x):
                val = parser(nondec_map[nondec.index(x)][1], False)
                name = nondec_map[nondec.index(x)][0]
                break

        for y in yesdec:
            if any(i in rate for i in y):
                val = parser(yesdec_map[yesdec.index(y)][1], True)
                name = yesdec_map[yesdec.index(y)][0]
                break

        if val is None:
            await wait_msg.delete()
            await ctx.send("**Помилка.** Курс даної валюти ще не було внесено до бази даних")
            return

        if ',' in amount:
            amount = str(amount).replace(',', '.')
        amount = float(amount)
        rt = float(val) * float(amount)
        rt = round(rt, 2)
        rt = str(rt)
        if rt.endswith('0'):
            rt = rt[:-2]

        await wait_msg.delete()
        await ctx.send(f"{random.choice(appeal).capitalize()}, {int(amount)} {name} становить **{rt}** грн!"
                       f"\n||*Станом на {date}: 1 {name} = {val} UAH*||")

    @bot.command(name="fetch vc")
    async def t_voice(ctx, member: discord.Member):
        if member.voice:
            channel_return = member.voice.channel.id
        else:
            return
        await ctx.send(channel_return)

    @bot.command(name="kanava")
    @commands.has_any_role("канавье")
    async def kanava(ctx, member: discord.Member, t=10, chance: int = 30):

        cur.execute(f"INSERT INTO kanava_user_data(user_id, user_nickname) VALUES(%s, %s) ON CONFLICT DO NOTHING",
                    [member.id, member.name])
        engine.commit()

        cur.execute(
            f"SELECT server_id FROM kanava_servers WHERE kanava_servers.server_id = %s AND kanava_servers.user_id = %s",
            [member.guild.id, member.id])
        result = cur.fetchone()
        if result is None:
            cur.execute(f"INSERT INTO kanava_servers(server_id, user_id, iter_left) VALUES(%s, %s, %s) ON CONFLICT DO NOTHING",
                        [ctx.guild.id, member.id, t])

        else:
            if ctx.author.id != 783069117602857031:
                cur.execute(f"UPDATE kanava_servers SET iter_left = kanava_servers.iter_left + (%s) WHERE kanava_servers.server_id = %s AND kanava_servers.user_id = %s",
                            [t, ctx.guild.id, member.id])
        engine.commit()

        channel1 = discord.utils.get(ctx.guild.voice_channels, name="ГУЛАГ (AFK)")
        if channel1 is None:
            await ctx.guild.create_voice_channel("ГУЛАГ (AFK)")
        channel2 = discord.utils.get(ctx.guild.voice_channels, name="Канава/МАрк (Марк и Марк)")
        if channel2 is None:
            await ctx.guild.create_voice_channel("Канава/МАрк (Марк и Марк)")

        if member.voice:
            channel3 = member.voice.channel
        else:
            channel3 = None

        for i in range(t):
            if member.voice:
                try:
                    rn = randint(0, 10)
                    ch = round(chance/10)
                    await member.edit(voice_channel=channel1)
                    await asyncio.sleep(0.5)
                    await member.edit(voice_channel=channel2)
                    await asyncio.sleep(0.5)
                    await member.send("**НУ ЩО, СЕПАРАТЮГО, ЗІЗНАВАЙСЯ, ТИ КОЇВ ЗЛОЧИНИ ПРОТИ НАШОЇ ДЕРЖАВИ, ЧИ НІ?**")
                    try:
                        await bot.wait_for("message", check=lambda message: check(message, message, (checklists[0] + checklists[1])), timeout=1.5)
                    except asyncio.TimeoutError:
                        continue
                    else:
                        if rn <= ch:
                            await member.send("Гаразд. На цей раз я тобі повірю. Хлопці, витягайте його!")
                            break
                        elif rn > ch:
                            await member.send("Ага, так я тобі і повірив... Хлопці, продовжуємо!")
                            await member.send("https://tenor.com/view/bandera-ussr-russia-ukraine-%D1%81%D1%81%D1%81%D1%80-gif-22544933")
                            continue
                except discord.errors.HTTPException:
                    continue
            else:
                await ctx.send(f"**Помилка**. Користувач не під'єднаний до жодного з голосових каналів.", delete_after=10)
                await member.send(f"Цього разу ти зміг уникнути покарання. Вважай тобі поки що пощастило. Але, я все пам'ятаю...")
                await ctx.send(f"Цього разу залишилось занурень: {t-i}", delete_after=10)
                cur.execute(f"UPDATE kanava_servers SET iter_left = kanava_servers.iter_left - (%s) WHERE kanava_servers.server_id = %s AND kanava_servers.user_id = %s",
                    [i, ctx.guild.id, member.id])
                engine.commit()
                return
        await member.send(f"Ти вільний, {random.choice(appeal)}. Іди по своїx справаx.")
        cur.execute(f"DELETE FROM kanava_servers WHERE kanava_servers.server_id = %s AND kanava_servers.user_id = %s",
                    [ctx.guild.id, member.id])
        engine.commit()
        await member.send("https://media.discordapp.net/attachments/810509408571359293/919313856159965214/kolovrat1.gif")
        try:
            await member.edit(voice_channel=channel3)
        except discord.errors.HTTPException:
            return

    @bot.command(name="t_greeting")
    async def greeting(ctx, member: discord.Member):
        await member.send(f"Вітаю тебе на сервері **{ctx.guild.name}**!\n"
                          f"Я - **Бандера бот**, найгеніальніший бот, створений *@dani4feedyt#5200*, який можливо навіть колись якось вам допоможе!\n\n"
                          f"Існує спеціальний лист **правил** спілкування зі мною, яких ти **маєш притримуватися**.\n"
                          f"Якщо на цьому сервері є канал **#правила**, можеш із ними ознайомитися.\n"
                          f"У випадку коли такого каналу немає, мої правила можна побачити використавши команду **b!rules**\n\n"
                          f"Для отримання більш розгорнутої інформації щодо мого функціоналу, скористайся **b!info**")
        await member.send(
            "https://media.discordapp.net/attachments/810509408571359293/919313856159965214/kolovrat1.gif")

    @bot.command(name="t_invite")
    async def invite(ctx, member: discord.Member, age: int = 60):
        author = ctx.message.author
        link = await ctx.channel.create_invite(max_age=age*60)
        await member.send(f"{author.mention}запрошує вас на сервер **{ctx.guild.name}!**\n{link}")

    @bot.command(name="invite")
    async def invite(ctx, age: int = 60):
        link = await ctx.channel.create_invite(max_age=age*60)
        await ctx.send(f"Посилання для запрошення ваших друзів на {age} хв!\n{link}")

    @bot.command(name="slava_ukraine")
    async def slava_ukraine(ctx):
        await ctx.reply(f"**Героям слава, {random.choice(appeal)}!**")

    @bot.command(pass_context=True, name="echo")
    async def echo(ctx, *, msg):
        await ctx.send(msg)
        await ctx.message.delete()

    @bot.command(name="info")
    async def info(ctx, inline=False):
        zaha_emoji = "<:Admin_Ebalo:698661524247412826>"
        embed = discord.Embed(title=f"Бандера бот", description=f"Патріотичий бот, який вміє робити деякі прикольні штуки:\n*Працює цілодобово!*", color=0x013ADF)
        embed.add_field(name=f"**b!slava_ukraine**", value=f"Головна функція Бандери ", inline=inline)
        embed.add_field(name=f"**b!birb**", value=f"Світлина випадкового птаха", inline=inline)
        embed.add_field(name=f"**b!kick @(Нікнейм) (Порушення)** {zaha_emoji}", value=f"Вигнання на Соловки", inline=inline)
        embed.add_field(name=f"**b!clear (Кількість повідомлень)** {zaha_emoji}", value=f"Видалення повідомлень", inline=inline)
        embed.add_field(name=f"**b!clear_t (День) (Місяць) (Година) (Хвилина)** {zaha_emoji}", value=f"Видалення повідомлень починаючи з заданої дати. \n||*Часовий пояс за замовчуванням - GMT+3 (Київський час)*||", inline=inline)
        embed.add_field(name=f"**b!quote**", value=f"Надішлю вам випадковий вислів Степана Андрійовича", inline=inline)
        embed.add_field(name=f"**b!pasta (Number 1-4)**", value=f"Один з крилатих висловів про так званий <<Колюмбас>>", inline=inline)
        embed.add_field(name=f"**b!spam_info**", value=f"Інформація про належне використання вибухової спам програми", inline=inline)
        embed.add_field(name=f"**b!mute_info** {zaha_emoji}", value=f"Інформація про використання b!mute", inline=inline)
        embed.add_field(name=f"**b!invite**", value=f"Створити запрошення на сервер для ваших друзів", inline=inline)
        embed.add_field(name=f"**b!pfp @(Нікнейм)**", value=f"Отримати аватар зазначеного користувача", inline=inline)
        embed.add_field(name=f"**b!kanava_info**", value=f"Інформація про канаву та ваш рахунок", inline=inline)
        embed.add_field(name=f"**b!rates (Валюта) (Кількість)**", value=f"Найактуальніший курс валют", inline=inline)
        embed.add_field(name=f"**b!stop**", value=f"Зупинити виконання усіх операцій", inline=inline)
        embed.add_field(name=f"**b!rg8421**", value=f"???", inline=inline)
        embed.set_image(url="https://i.ibb.co/4stKfF2/band.png")
        embed.add_field(name=f"**Запрошення на найбазованіший сервер**", value=f"https://discord.gg/Ty5FcmEQkj", inline=inline)
        embed.add_field(name=f"||Команди з поміткою {zaha_emoji} може використовувати тільки модерація||\n\n*Розробник:* **@dani4feedyt#5200**", value=f"*{version}*\n||*{patch_note}*||", inline=inline)

        await ctx.send(embed=embed)

    @bot.command(name="pfp")
    async def pfp(ctx, member: discord.Member):
        global url
        global irritation
        author = ctx.message.author
        member_url = f"{member.avatar}"
        if member.avatar is None:
            await ctx.send("**Помилка.** На жаль, у цього користувача відсутнє зображення профілю.")
            irritation = 0
            return
        if irritation == 11:
            await ctx.send(file=discord.File("b2.png"))
            await mute(ctx, author, 1, 30, reason="Задовбав.", bot_source=True)
            irritation = 0
            return

        pfp_image = requests.get(member_url)

        with open(f"src/last_pfp.jpg", "wb") as f:
            f.write(pfp_image.content)
            picture = discord.File("src/last_pfp.jpg")
            pfp_u = await ctx.reply(file=picture)

        if url == member_url:
            irritation += 1
        else:
            url = member_url
            irritation = 0

        if member.id == 783069117602857031:
            await ctx.send("**Традиція і Порядок!**")

        elif member.id == 486176412953346049:
            irritation = 0
            pfp_t = await ctx.send("О НІ! МЕНІ НЕ БУЛО ДОЗВОЛЕНО РОЗГОЛОШУВАТИ ІНФОРМАЦІЮ ПРО СВОГО ТВОРЦЯ! Проводжу екстренне видалення даних")
            for c in range(2):
                c += 1
                for i in range(4):
                    await asyncio.sleep(0.2)
                    await pfp_t.edit(content=pfp_ph_sp[i])
                    i += 1
                if c == 1:
                    await pfp_u.delete()
                elif c == 2:
                    await pfp_t.delete()
                    await ctx.send("**Доступ відхилено.**")

        else:
            if irritation == 0:
                await ctx.send(random.choice(pfp_ph_0))
            elif irritation == 1:
                await ctx.send(random.choice(pfp_ph_1))
            elif irritation == 2:
                await ctx.send(random.choice(pfp_ph_2))
            elif 3 <= irritation <= 7:
                await ctx.send(pfp_ph[irritation - 3])
            elif irritation >= 7:
                await ctx.send(pfp_ph[-1])


    @bot.command(name="birb")
    async def birb(ctx):
        t2 = ["Випадковий птах для тебе",
               "Тримай птаха", "Випадковий птах, як ти й просив",
               "Світлина випадкового птаха", "Світлина птаха, як ти й просив",
               "Тримай пташку", "Тримай світлину птаха", "Птах, як ти й побажав",
               "Світлина птаха"]
        response = requests.get("https://some-random-api.com/animal/bird")
        json_data = json.loads(response.text)
        embed = discord.Embed(color=0x013ADF, title=f"{random.choice(t2)}, {random.choice(appeal)}:")
        embed.set_image(url=json_data["image"])
        await ctx.send(embed=embed)

    @bot.command(pass_context=True, name="$check")
    async def t_check(ctx):
        await ctx.send("Чи бажаєте ви {String}?")
        try:
            await bot.wait_for("message", check=lambda message: check(ctx, message, checklists[0]), timeout=30)
        except asyncio.TimeoutError:
            await ctx.send("Час очікування вичерпано, запит скасовано.", delete_after=20)
            return
        else:
            await ctx.send("Підтверджено")

    @bot.command(pass_context=True, name="kick")
    @commands.has_permissions(kick_members=True)
    async def kick(ctx, user: discord.Member, rule_n=None, *, reason=None):
        if user == ctx.message.author:
            await ctx.send("**Помилка.** Ви не можете виключити себе.")
        else:
            if rule_n is None:
                rule_n = 0
            rule_n = int(rule_n)
            if 1 <= rule_n <= len(rules_list):
                rule = (rules_list[rule_n][1])
                ruleA = f"**№{rule_n}: {rules_list[rule_n][0]}**"
            else:
                rule = '⁣'
                ruleA = "None"
            guild = ctx.guild
            author = ctx.message.author
            if reason is None:
                reasonT = "**Без будь-якого приводу**"
                reasonA = '⁣'
            else:
                reasonT = "Порушення:"
                reasonA = reason
            await ctx.send(f"Ви дійсно бажаєте виключити **{user}** з сереверу?", delete_after=60)

            try:
                await bot.wait_for("message", check=lambda message: check(ctx, message, checklists[0]), timeout=30)
            except asyncio.TimeoutError:
                await ctx.send("Час очікування вичерпано, запит скасовано.", delete_after=20)
                return
            else:
                embed = discord.Embed(title="Заслання", description=f"**{user}** був виключений з серверу модератором **{author.mention}**", color=0x013ADF)
                embed.add_field(name=reasonT, value=reasonA, inline=False)
                embed.add_field(name="Порушене правило:", value=ruleA, inline=False)
                await ctx.send(embed=embed)
                await ctx.send(rule)
                await user.send(f"Ви були виключені з серверу **{guild.name}** модератором **{author.mention}**, **{reasonT}** {reasonA}")
                await user.send(rule)
                await user.kick(reason=reason)


    @bot.command(name="rule")
    async def rule(ctx, rule_n: int):
        if 1 <= rule_n <= len(rules_list):
            if rules_list[rule_n][0]:
                await ctx.send(rules_list[rule_n][0])
            await ctx.channel.send(rules_list[rule_n][1])
        else:
            await ctx.send("**Помилка.** Правила під таким номером не існує")

    @bot.tree.command(
        name="pasta",
        description="Крилатий вислів про Колюмбас (1-4)"
        )
    async def pasta(interaction, number: int):
        if 1 <= number < 5:
            await interaction.response.send_message(Quotes1[number])
        else:
            await interaction.response.send_message("**Помилка.** Вислів під цим номером ще не було вигадано,"
                                                    " або не було занесено до моєї бази даних. \n"
                                                    "*Для детальної інформації звертайтеся до @dani4feedyt#5200*")

    @bot.command(name="quote")
    async def quote(ctx: commands.Context):
        quote = random.choice(quotes).get_text()
        quote.replace("<p>", "")
        quote.replace("</p>", "")
        await ctx.send(f"Випадковий вислів Степана Андрійовича Бандери: \n\n***{quote}***")

    @bot.command(name="myroles")
    async def myroles(ctx):
        member = ctx.message.author
        roles = (", ".join(role.name for role in member.roles if role.name != "@everyone"))
        await ctx.reply(f"Перелік твоїх ролей, {random.choice(appeal)}:\n*{roles}*")


    @bot.command()
    async def kanava_info(ctx, member: discord.Member = None):
        await ctx.send("• Щоб почати допитувати користувача у **канаві**, введіть його нікнейм, кількість занурень та рівень мого милосердя у форматі: **b!kanava @(Нікнейм) (Кількість) (Милосердя *<%>*)**\n"
                       "• Той, хто знаходиться під впливом цієї команди, буде допитуватися особисто Степаном Андрійовичем Бандерою (мною)\n\n"
                       "||*Наприклад: b!kanava @user#5234 10*||")
        if member is None:
            member = ctx.message.author

        cur.execute(
            f"SELECT iter_left FROM kanava_servers WHERE kanava_servers.server_id = %s AND kanava_servers.user_id = %s",
            [ctx.guild.id, member.id])
        num = cur.fetchone()
        engine.commit()

        if num == 0 or num is None:
            await ctx.send(f"У {member.mention} немає незгод зі мною. Так тримати!")
        else:
            await ctx.send(f"Утікач {member.mention} повинен відбути ще **{num[0]}** занурен{msg_end_temp_1(num[0])}. Я до нього дістануся!")


    @bot.command()
    async def mute_info(ctx):
        await ctx.send("• Щоб накласти **мут**, введіть нікнейм користувача, час муту та порушене правило у форматі: **b!mute @(Нікнейм) (Час *<хв>*) (Номер правила) (Деталі порушення)**\n"
                       "• Людина, на яку було накладено мут, буде тимчасово заблокована на майже всіх голосових та текстових каналах\n"
                       "• При закінченні терміну дії, мут буде автоматично знятий\n"
                       "• Для дострокового зняття муту: **b!unmute @(Нікнейм)**\n\n"
                       "||*Наприклад: b!mute @user#5234 10 2 Порушення порядку на сервері*||")

    @bot.command()
    async def spam_info(ctx):
        await ctx.send("• Щоб розпочати **спам** у особистий чат обраного користувача, введіть параметри кількості повідомлень, інтервал надсилання та зміст у форматі:"
                       " **b!spam @(Нікнейм) (Кількість) (Інтервал *<мс>*) (Повідомлення)**"
                       "\n\n||*Наприклад: b!spam @user#5234 100 0.5 Бандера Бот - найкращий!*||")

    @bot.command(name="mute")
    @commands.has_permissions(manage_messages=True)
    async def mute(ctx, member: discord.Member, time: int, rule_n: int, *, reason=None, bot_source = False):

        if bot_source:
            author = f"<@!{str(783069117602857031)}>"
        else:
            author = ctx.message.author.mention

        rule_txt = None
        reason_changed = False
        if 1 <= rule_n <= len(rules_list):
            rule_gif = (rules_list[rule_n][1])
            if rules_list[rule_n][0]:
                rule_txt = rules_list[rule_n][0]
                if reason is None:
                    reason = rule_txt
                    reason_changed = True
        else:
            rule_gif = None

        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")
            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=True, read_message_history=True, read_messages=True, view_channel=False)

        embed = discord.Embed(title="Мут", description=f"**{member.mention}** був відправлений до муту модератором **{author}** на **{time}** хвилин{msg_end_temp_2(time)}", color=0x013ADF)
        embed.add_field(name="Порушення:", value=reason, inline=False)
        embed.add_field(name="Порушене правило:", value=f"**#{rule_n}**", inline=False)

        await ctx.send(embed=embed)
        if not reason_changed:
            await ctx.send(rule_txt)
        await ctx.send(rule_gif)
        await member.add_roles(mutedRole)
        await asyncio.sleep(1)
        try:
            await member.edit(voice_channel=None)
        except discord.errors.HTTPException:
            return
        await member.send(f'На вас було накладено мут на сервері **{guild.name}** модератором **{author}** на **{time}** хвилин{msg_end_temp_2(time)}, за причиною: **"{reason}"**')

        if not reason_changed:
            await member.send(rule_txt)
        await member.send(rule_gif)
        await asyncio.sleep(time * 60)
        bot.dispatch("mute_command", ctx, member, guild)

    @bot.event
    async def on_mute_command(ctx, member, guild):
        id1 = member.id
        user = await ctx.message.guild.query_members(user_ids=[id1])
        user = user[0]
        mutedRole = discord.utils.get(guild.roles, name="Muted")
        if mutedRole in user.roles:
            await member.remove_roles(mutedRole)
            await member.send(f"Час муту на сервері **{ctx.guild.name}** вийшов. Ви можете вільно продовжити спілкування!")
            embed = discord.Embed(title="Мут знято", description=f"Час муту **{member.mention}** вийшов. Приємного спілкування!", color=0x013ADF)
            await ctx.send(embed=embed)

    @bot.command(name="$roles")
    @commands.has_permissions(manage_messages=True)
    async def t_roles(ctx, member: discord.Member):
        await ctx.send(member.roles)

    @bot.command(pass_context = True, name="unmute")
    @commands.has_permissions(manage_messages=True)
    async def unmute(ctx, member: discord.Member):
        id1 = member.id
        user = await ctx.message.guild.query_members(user_ids=[id1])
        user = user[0]
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
        author = ctx.message.author
        if mutedRole in user.roles:
            await member.remove_roles(mutedRole)
            await member.send(f"З вас було знято мут на сервері **{ctx.guild.name}**. Ви можете вільно продовжити спілкування!")
            embed = discord.Embed(title="Мут знято", description=f"**{author.mention}** зняв мут з **{member.mention}**. Приємного спілкування!", colour=0x013ADF)
            await ctx.send(embed=embed)
            try:
                await member.edit(voice_channel=None)
            except discord.errors.HTTPException:
                return
        else:
            await ctx.send("**Помилка.** Неможливо зняти мут з користувача, який його не має.")

    @bot.command(name="$time")
    async def t_time(ctx):
        timestamp = ctx.message.created_at
        print(timestamp)
        timestamp = str(timestamp)[:-10]
        timestamp = timestamp.replace(' ', '')

        date = timestamp[:10]
        date = date.replace('-', '')
        date_y = int(date[:4])
        date_m = int((date[4:])[:-2])
        date_d = int(date[:2])

        date_f = (str(date_d) + ' ' + str(date_m) + ' ' + str(date_y))

        time_0 = timestamp[10:]
        time_0 = time_0.replace(':', '')
        time_h = int(time_0[:2]) + 2
        time_mi = int(time_0[2:])

        time_f = (str(time_h) + ' ' + str(time_mi))
        date12 = datetime.datetime.now()
        print(date, time_0, date12)
        await ctx.send(date_f + ' ' + time_f)

    @bot.command(name="$count")
    async def t_count(ctx, d: int, m: int, h: int, mi: int):
        count = 0
        h -= 2
        date = datetime.datetime(year = 2021, month=m, day=d, hour=h, minute=mi)
        async for message in ctx.channel.history(limit=None, after=date):
            count += 1
        await ctx.send(count)

    @bot.command(pass_context=True, name="clear")
    @commands.has_permissions(manage_messages=True)
    async def clear(ctx, count = 100):

        msg_ending = msg_end_temp_1(count)
        await ctx.send(f'Ви дійсно бажаєте очистити **{count}** повідомлен{msg_ending}? \n*Для підтверждення - напишіть "так" протягом 7 секунд* ', delete_after=60)

        try:
            await bot.wait_for("message", check=lambda message: check(ctx, message, checklists[0]), timeout=7)
        except asyncio.TimeoutError:
            await ctx.send("Час очікування вичерпано, запит скасовано.", delete_after=20)
            return
        else:
            if int(count) <= 150:
                await ctx.channel.purge(limit=int(count+3))
                if int(count) >= 100:
                    count = "дуууууже багато"
                await asyncio.sleep(0.75)
                await ctx.send(f"Було видалено **{count}** повідомлен{msg_ending}!", delete_after=60)
            else:
                await ctx.send("**Помилка.** Ви не можете видалити більше ніж 150 повідомлень.", delete_after=60)


    @bot.command(pass_context=True, name="clear_t")
    @commands.has_permissions(manage_messages=True)
    async def clear_t(ctx, d=00, m=00, h=00, mi=00, gmt=+3):

        ye = today.year

        try:
            msg = await ctx.channel.fetch_message(ctx.message.reference.message_id)

        except AttributeError:

            utc_d = int(d)
            utc_m = int(m)
            gmt = int(gmt)

            utc_h = h - gmt
            if utc_h < 0:
                utc_d -= 1
                utc_h = 24 - gmt
            if utc_d == 0:
                utc_m -= 1
                utc_d = list(months.values())[utc_m - 1]
            if utc_m == 0:
                utc_m = 12
                ye -= 1

            date_t = datetime.datetime(year=int(ye), month=int(utc_m), day=int(utc_d), hour=int(utc_h), minute=int(mi),
                                       tzinfo=datetime.timezone.utc)
            print(date_t)
        else:
            date_t = msg.created_at
            date_t = date_t.replace(microsecond=date_t.microsecond-1000)
            h = date_t.hour
            mi = date_t.minute
            d = date_t.day
            m = date_t.month
            gmt = "+0"
            print(date_t)

        date = [h, mi, d, m]
        date_str = [str(i) for i in date]
        print(date)

        a = 0
        for i in date_str:
            if len(i) == 1:
                date_str[a] = '0' + i
            a += 1

        last_mes = None
        count = 0
        await ctx.send("*Зачекайте, підраховую повідомлення…*", delete_after=30)
        async for count, message in asyncstdlib.enumerate(ctx.channel.history(limit=None, after=date_t, oldest_first=True)):
            if count == 0:
                last_mes = message

        msg_ending = msg_end_temp_1(count)
        if last_mes is not None:
            await last_mes.reply(f"Ви дійсно бажаєте очистити **{count}** повідомлен{msg_ending} починаючи з цього повідомлення? "
                                 f"**({date_str[0]}:{date_str[1]} {date_str[2]}-{date_str[3]}-{ye}** за часовим поясом **GMT{gmt}**)"
                                 f'\n*Для підтверждення - напишіть "так" протягом 30 секунд*', delete_after=30)

            try:
                await bot.wait_for("message", check=lambda message: check(ctx, message, checklists[0]), timeout=30)
            except asyncio.TimeoutError:
                await ctx.send("Час очікування вичерпано, запит скасовано.", delete_after=20)
                return
            else:
                if int(count) <= 500:
                    await ctx.channel.purge(limit=int(count) + 2)
                    await ctx.send(f"Було видалено **{count}** повідомлен{msg_ending}!", delete_after=60)
                else:
                    await ctx.send("**Помилка.** Ви не можете видаляти більше 500 повідомлень!", delete_after=60)
        else:
            await ctx.send("**Помилка.** Обраного повідомлення не існує. Спробуйте змінити часовий пояс.", delete_after=60)


    @bot.command(name="spam", pass_context=True)
    @has_permissions(kick_members=True)
    async def spam(ctx, member: discord.Member, count, interval, *, text_arg):
        count = int(count)
        interval = float(interval)
        if interval < 0.5:
            interval = 0.5
            await ctx.send(f"**Попередження.**\nВи не можете задавати інтервал між повідомленнями менший за **{interval}** секунд. Значення параметру змінено на **{interval}**")
        if interval > 3600:
            interval = 3600
            await ctx.send(f"**Попередження.**\nВи не можете задавати інтервал між повідомленнями більший за **{interval}** секунд. Значення параметру змінено на **{interval}**")

        await ctx.send(f"Ви дійсно бажаєте розпочати спам у особисті повідомлення користувача {member.mention}?")
        try:
            await bot.wait_for("message", check=lambda message: check(ctx, message, checklists[0]), timeout=30)
        except asyncio.TimeoutError:
            await ctx.send("Час очікування вичерпано, запит скасовано.", delete_after=20)
            return

        else:
            timeout = 5
            global spam
            spam = True
            await ctx.send(f"**Спам** розпочнеться через **{timeout}** секунд, для завершення - введіть **b!stop**")
            await asyncio.sleep(timeout)
            await ctx.send(f"**Спам** у особисті повідомлення {member.mention} розпочато")

            a = 0
            for i in range(count):
                while True:
                    if not spam:
                        break
                    if a < count:
                        await member.send(text_arg)
                        await asyncio.sleep(interval)
                        a += 1
                    break

            await ctx.send(random.choice(spam_ph))
            if interval > 15:  # чтобы спам со слишком долгими интервалами не засорял чат, будучи неуместным по своему завершению
                pass
            else:
                if count == a:
                    await ctx.send(f"{member.mention} отримав **усі** повідомлення!")
                else:
                    await ctx.send(f"Кількість отриманих повідомлень користувачем {member.mention} : **{a}**")
            spam = False
            await member.send("Спам закінчено, тобі цього вистачить.")


    @bot.command(name="stop")
    async def stop(ctx):
        await player_inst.stop(discord.utils.get(bot.voice_clients, guild=ctx.guild))

        global spam
        spam = False ##сюда можно встроить выключатели глобальных переменных для остановки комманд
        await ctx.send("Мене було зупинено, але мою жагу до свободи не спинити нікому!")


    @bot.command(name="$ping")
    async def t_ping(ctx):
        await ctx.send(f"Моя затримка складає **{round(bot.latency, 3)}** с")

 ###############################################ErrorHandling###############################################

    error_desc = ""

    def error_temp(error):
        return f"\n\n*||**Description:** {str(error)}||*"


    @rates.error
    async def rates_error(ctx, error):
        global error_desc
        error_desc = "Введіть запит у коректному форматі.\n||**b!rates** *(Кількість) (Валюта)*||"


    @kanava.error
    async def kanava_error(ctx, error):
        global error_desc
        error_desc = "||**b!kanava** *@(Нікнейм) (Кількість) {Довіра бота}*||"


    @play.error
    async def play_error(ctx, error):
        global error_desc
        error_desc = "Помилка у виконанні треку. Можливо посилання було введено некоректно."



    @clear_t.error
    async def clear_t_error(ctx, error):
        global error_desc
        error_desc = "Введіть дату та час у коректному форматі.\n||**b!clear_t** *(День) (Місяць) (Години) (Хвилини) {Часовий пояс}*||"


    @pfp.error
    async def pfp_error(ctx, error):
        global error_desc
        error_desc = "||**b!pfp** *@(Нікнейм)*||"


    @kick.error
    async def kick_error(ctx, error):
        global error_desc
        error_desc = "||**b!kick** *@(Нікнейм) {Причина}*||"


    @pasta.error
    async def pasta_error(ctx, error):
        global error_desc
        error_desc = "||**b!pasta** *(Номер пасти)*||"


    @mute.error
    async def mute_error(ctx, error):
        global error_desc
        error_desc = "||**b!mute** *@(Нікнейм) (Час муту у хвилинах) {Номер порушення} {Опис}*||"

    @unmute.error
    async def unmute_error(ctx, error):
        global error_desc
        error_desc = "||**b!unmute** *@(Нікнейм)*||"

    @spam.error
    async def spam_error(ctx, error):
        global error_desc
        error_desc = "||**b!spam** *(Кількість повідомлень) (Кулдаун між повідомленнями) (Слово для спаму)*||"

    @bot.event
    async def on_command_error(ctx, error):
        print(error)
        global error_desc
        err = "**Помилка. **"
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(f"{err}Такої команди не існує.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(f"{err}Йой, хлопче, в тебе не вистачає прав для виконання цієї команди!")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"{err}Не вистачає аргументів для виконання команди, перевірте коректність написання.")
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send(f"{err}Аргумент заданий некоректно.")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send(f"{err}Користувача з таким нікнеймом не будо знайдено. Можливо, нікнейм будо введено некоректно, або цього користувача немає на сервері.")
        else:
            await ctx.send(f"{err}Некоректна команда.")
        await ctx.send(error_temp(error))
        error_desc = ""

  ###############################################ErrorHandling###############################################

    st = ("--- %s секунд ---" % round((time.time() - start_time), 3))

    @bot.command(name="$start_t")
    async def t_start_time(ctx):
        await ctx.send(f"Цього разу час мого запуску склав " + st)

    print(st)
    bot.run(settings["token"])

except GeneratorExit:
    print("Error_12.1 (Generator_Error)")
