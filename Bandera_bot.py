try:
    import time
    
    start_time = time.time()

    import datetime
    import discord
    from discord.ext import commands
    from Bandera_cfg import settings
    from Bandera_Quotes import _dict0, n_1
    from Bandera_PyChton_quotes import Quotes1, links, Quotes2
    from sys import argv, executable
    import json
    import requests
    import os
    import sys
    import random
    from random import randint
    from urllib.request import urlopen
    import lxml
    from lxml import etree
    from lxml import html
    from collections import Counter
    import asyncio
    from asyncio import sleep
    from selenium import webdriver
    from bs4 import BeautifulSoup
    import pandas as pd
    from datetime import date

    #############################################__ИДЕИ__#############################################
    #1. Сделать предварительный выбор языка в b!info
    #############################################__ИДЕИ__#############################################

    ############Global var############
    client = discord.Client()
    bot = commands.Bot(command_prefix = settings['prefix'], intents = discord.Intents.all())
    version = 'release 2.3.5A'
    patch_note = '•minor bug fixes; •improved crash reports'
    w = ("Bandera_bot.py")
    fi = open("data.txt","w+")
    data_filename = "data.txt"
    today = datetime.date.today()
    print(today)
    months = {'jan': 31, 'feb': 28, 'mar': 31, 'apr': 30, 'may': 31, 'jun': 30, 'jly': 31, 'aug': 31, 'sep': 30, 'oct': 31, 'nov': 30, 'dec': 31}
    if today.year % 4 == 0:
        months['feb'] = 29
    appeal = ["козаче", "хлопче", "друже", "вуйко", "брате", "дядьку"]
    ############Global var############
    
    @bot.event
    async def on_member_join(member):
        guild = bot.get_guild(695715313911857186)
        member_count = len(guild.members)
        await member.send(f"**Вітаємо вас на сервері {guild.name}**!" +
                          "\n\n•Я - **Бандера бот**, ваш персональний помічник, створений *dani4feedyt#5200*, який допоможе вам швидко зрозуміти правила та порядки серверу." +
                          "\n•Для отримання більш розгорнутої інформації щодо мого функціоналу перейдіть до каналу **#info**" +
                          "\n•Для ознайомлення з правилами серверу перейдіть до каналу **#правила**")
        await member.send("https://media.discordapp.net/attachments/810509408571359293/919313856159965214/kolovrat1.gif")
        await bot.get_channel(695715314696061072).send(f"Ласкаво просимо на сервер **{guild.name}**, {member.mention}. Наші ряди поповнилися ще одним націоналістом. Нас вже **{member_count}**!")
    
    @bot.event
    async def on_ready():
        await bot.change_presence(activity = discord.Game('очке своим пальчиком | b!info'))

    @bot.event##################Намутить онмесседжи, что будут сканировать по правилам#########################
    async def on_message(message):
        if "бандер" in message.content.lower():
            if message.author.id == 783069117602857031:
                await bot.process_commands(message)
            else:
                await message.channel.send("Мене хтось кликав?")
                def check(m):############Ответ Да
                    return (m.content.lower() == 'так' or m.content.lower() == 'да' or m.content.lower() == 'ага' or m.content.lower() == 'yes' or m.content.lower() == 'y')
                try:
                    m = await bot.wait_for("message", check=check, timeout = 15)
                except asyncio.TimeoutError:
                    await message.channel.send("Гаразд, мені певно здалося...")
                else:
                    await message.channel.send("Що сталося?")
                    def check(m):############Поздравление с др
                        return (m.content.lower() == 'з днем народження' or m.content.lower() == 'с днем рождения' or m.content.lower() == 'с др' or m.content.lower() == 'з др') #########################ДОПИЛИТЬ НОРМАЛЬНЫЙ КОНТЕНТ
                    try:
                        m = await bot.wait_for("message", check=check, timeout = 15)
                    except asyncio.TimeoutError:
                        a_list = [0, 1]
                        distribution = [.9, .1]
                        rand = random.choices(a_list, distribution)
                        print(rand)
                        await message.channel.send("Я взагалі-то маю свої справи, прошу не відволікати! Якщо є якісь проблеми, напишіть **b!info**, або зверніться до " + "<@" + str(486176412953346049) + ">")
                        if rand == [1]:
                            await message.channel.send(file=discord.File('b1.png'))    
                    else:
                        if str(today) == "2022-01-01":
                            await message.channel.send(f"**Дякую тобі, {random.choice(appeal)}!** Не думав, що хтось згадає про мене...")
                        else:
                            await message.channel.send(f"Вельми дякую, але ти, певно, помилився. Мій день народження **1 січня**.")
                        await asyncio.sleep(7)
                        await message.channel.send("Гаразд, пішов я по своїх справах...")
        else:
            await bot.process_commands(message)
    
    @bot.command()
    async def id(ctx, member: discord.User):
        print("Triggered... id; server: ctx.guild.name")
        await ctx.send(member.id)

    @bot.command()
    async def fetch(ctx, msgID: int):
        print("Triggered... fetch; server: ctx.guild.name")
        msg = await ctx.fetch_message(msgID)
        timestamp = msg.created_at
        await ctx.send(timestamp)

    @bot.command()####'fi' - Global var####
    async def save(ctx, *, msg):
        print("Triggered... save; server: ctx.guild.name")
        fi = open("data.txt","a+") ######Пофиксить очистку каждый день######
        fi.write(msg + " ")
        fi.close

    @bot.command()####'fi' - Global var####
    async def read(ctx):
        print("Triggered... read; server: ctx.guild.name")
        fi = open("data.txt", "r")
        if fi.mode == 'r':
            contents = fi.read()
            await ctx.send(contents)
    
    @bot.command()####'fi' - Global var####
    async def c_save(ctx):
        print("Triggered... c_save; server: ctx.guild.name")
        fi = open("data.txt", "w").close()
            
    @bot.command()
    async def rg8421(ctx):
        print("Triggered... rg8421; server: ctx.guild.name")
        author = ctx.message.author
        await ctx.send("<@" + str(696670757794742322) + ">," + f" {author.mention}" + " зазіхнув на головну тайну калу, та дізнався рецепт надчистого лайна:" + "\n||Гівно + Гівно - Гівно + Крапелька поносу та три крапельки гівна високої концентрації||")

    @bot.command(name='rates')
    async def rates(ctx, rate, amount=None):
        print("Triggered... rates; server: ctx.guild.name")
        counter = 0
        page1 = requests.get("https://bank.gov.ua/ua/markets/exchangerates?date=today&period=daily")
        soup = BeautifulSoup(page1.content, 'html.parser')
        _dict1 = soup.find_all('td', {"data-label":"Офіційний курс"})[6].get_text()
        _dict1 = round(float(_dict1.replace(',', '.')),2)
        _dict2 = soup.find_all('td', {"data-label":"Офіційний курс"})[7].get_text()
        _dict2 = round(float(_dict2.replace(',', '.')),2)
        _dict3 = soup.find_all('td', {"data-label":"Офіційний курс"})[16].get_text()
        _dict3 = round(float(_dict3.replace(',', '.')),2)
        _dict4 = soup.find_all('td', {"data-label":"Офіційний курс"})[20].get_text()
        _dict4 = round(float(_dict4.replace(',', '.'))/10,2)
        _dict5 = soup.find_all('td', {"data-label":"Офіційний курс"})[9].get_text()
        _dict5 = round(float(_dict5.replace(',', '.'))/10,2)
        rate = rate.lower() 
        if rate == ("долар") or rate == ("доларів") or rate == ("долари") or rate == ("доллар") or rate == ("долларов") or rate == ("доллара") or rate == ("usd") or rate == ("dollars") or rate == ("dollar") :
            val = _dict1
            name = ("долару")
            counter = 1
        elif rate == ("євро") or rate == ("евро") or rate == ("eur") or rate == ("euro"):
            val = _dict2
            name = ("євро")
        elif rate ==("шекель") or rate ==("шекелей") or rate ==("шекеля") or rate ==("шекелів") or rate ==("шекелі") or rate == ("ils"):
            val = _dict3
            name = ("шекеля")
        elif rate == ("рубль") or rate ==("рубля") or rate ==("рублей") or rate ==("рублі") or rate ==("рублів") or rate == ("rub") or rate == ("ruble") or rate == ("rubles"):
            val = _dict4
            name = ("рубля")
        elif rate == ("єна") or rate == ("єни") or rate == ("єн") or rate == ("йена") or rate == ("йены") or rate == ("йен") or rate == ("jpy"):
            val = _dict5
            name = ("єни")
        else:
            await ctx.send("**Помилка.** Курс даної валюти ще не було внесено до бази даних")
        bot.dispatch('rates_command', ctx, val, name, amount, rate)
    
    @bot.event
    async def on_rates_command(ctx, val, name, amount, rate):
        if amount is None:
            await ctx.send(f"{random.choice(appeal).capitalize}, курс {name} становить **{val}** грн!")  
        else:
            if ',' in amount:
                amount = str(amount).replace(',', '.')
            amount = float(amount)
            rt = float(val) * float(amount)
            rt = round(rt, 2)
            rt = str(rt)
            if rt.endswith('0'):
                rt = rt[:-2]
            await ctx.send(f"{amount} {rate} становить **{rt}** грн!")

    @bot.command(name='kanava')
    @commands.has_permissions(manage_messages=True)
    async def kanava(ctx, member: discord.Member, t = 10, chance: int = 30):
        print("Triggered... kanava; server: ctx.guild.name")
        channel1 = discord.utils.get(ctx.guild.voice_channels, name="ГУЛАГ (AFK)")
        channel2 = discord.utils.get(ctx.guild.voice_channels, name="Канава/МАрк (Марк и Марк)")
        bot.dispatch('kanava_command', ctx, channel1, channel2, member, t, chance)
        
    @bot.event
    async def on_kanava_command(ctx, channel1, channel2, member, t, chance):
        if member.voice is None:
            for nt in range(25):
                time.sleep(1)
                if member.voice is not None:
                    return
        else:
            for i in range(t):
                if member.voice is not None:
                    rn = randint(0, 10)
                    ch = round(chance/10)
                    await member.edit(voice_channel=channel1)
                    time.sleep(0.5)
                    await member.edit(voice_channel=channel2)
                    time.sleep(0.5)
                    await member.send("**АНУ, СЕПАРАТЮГА, ТИ КАЄШСЯ В СВОЇХ ЗЛОЧИНАХ ПРОТИ НЕЗАЛЕЖНОСТІ НАШОЇ ДЕРЖАВИ, ЧИ НІ?**")
                    def check(m):
                        return (m.content.lower() == 'да' or m.content.lower() == 'да' or m.content.lower() == 'ага' or m.content.lower() == 'yes' or m.content.lower() == 'y' or m.content.lower() == 'так' or m.content.lower() == 'ні' or m.content.lower() == 'нет' or m.content.lower() == 'no')
                    try:
                        m = await bot.wait_for("message", check=check, timeout = 1.5)
                    except asyncio.TimeoutError:
                        continue
                    else:
                        if rn <= ch:
                            await member.send("Гаразд. На цей раз я тобі повірю. Ти отримаєш волю. Хлопці, витягайте його!")
                            break
                        elif rn > ch:
                            await member.send("Ти кажеш це не щиро. Хлопці, занурюйте його!")
                            await member.send("https://tenor.com/view/bandera-ussr-russia-ukraine-%D1%81%D1%81%D1%81%D1%80-gif-22544933")
                            continue
                if member.voice is None:
                    for nt in range(35):
                        if member.voice is not None:
                            break
                    
        await member.send("Ти вільний, {random.choice(appeal)}. Іди по своїx справаx.")
        await member.send("https://media.discordapp.net/attachments/810509408571359293/919313856159965214/kolovrat1.gif")

    @bot.command()
    async def t_greeting(ctx, member: discord.Member):
        print("Triggered... t_greeting; server: ctx.guild.name")
        guild = ctx.guild
        await ctx.send(f'{member}')
        await member.send(f"Вітаємо вас на сервері {ctx.guild.name}!\nЯ - **Бандера бот**, ваш персональний помічник, створений *@dani4feedyt#5200*, який допоможе вам швидко зрозуміти правила та порядки серверу.\nДля отримання більш розгорнутої інформації, перейдіть до каналу **#info**")
        await member.send("https://media.discordapp.net/attachments/618165831943061791/819546666272161802/CSuO7F_wPr0.png?width=541&height=676")

    @bot.command()
    async def t_invite(ctx, member: discord.Member, age: int = 60):
        print("Triggered... t_invite; server: ctx.guild.name")
        guild = ctx.guild
        message = discord.Message
        author = ctx.message.author
        link = await ctx.channel.create_invite(max_age = age*60)
        await member.send(f"{author.mention}запрошує вас на сервер **{ctx.guild.name}!**\n{link}")

    @bot.command(name="invite")
    async def invite(ctx, age: int = 60):
        print("Triggered... invite; server: ctx.guild.name")
        link = await ctx.channel.create_invite(max_age = age*60)
        await ctx.send(f"Посилання для запрошення ваших друзів на {age} хв!\n{link}")

    @bot.command()
    async def slava_ukraine(ctx):
        print("Triggered... slava_ukraine; server: ctx.guild.name")
        author = ctx.message.author
        await ctx.send(f"**Героям слава, {author.mention}!**")

    @bot.command(pass_context = True)
    async def echo(ctx, *, msg):
        print("Triggered... echo; server: ctx.guild.name")
        await ctx.send(msg)
        await ctx.message.delete()

    @bot.command(name="info")
    async def info(ctx: commands.Context, inline=False):
        print("Triggered... info; server: ctx.guild.name")
        zaha_emoji = ("<:Admin_Ebalo:698661524247412826>")
        embed = discord.Embed(title=f"Бандера бот", description=f"Патріотичий бот, який вміє робити деякі прикольні штуки:\n*Працює цілодобово!*", color=0x013ADF)
        embed.add_field(name=f"**b!slava_ukraine**", value=f"Головна функція Бандери", inline=inline)
        embed.add_field(name=f"**b!birb**", value=f"Світлина випадкового птаха", inline=inline)
        embed.add_field(name=f"**b!kick @(Нікнейм) (Порушення)** {zaha_emoji}", value=f"Вигнання на Соловки", inline=inline)
        embed.add_field(name=f"**b!clear (Кількість повідомлень)** {zaha_emoji}", value=f"Видалення повідомлень", inline=inline)
        embed.add_field(name=f"**b!clear_t (День) (Місяць) (Година) (Хвилина)** {zaha_emoji}", value=f"Видалення повідомлень починаючи з заданої дати", inline=inline)
        embed.add_field(name=f"**b!quote**", value=f"Надішлю вам випадковий вислів Степана Андрійовича", inline=inline)
        embed.add_field(name=f"**b!pasta (Number 1-4)**", value=f'Один з крилатих висловів про так званий "Колюмбас"', inline=inline)
        embed.add_field(name=f"**b!spam_info**", value=f"Інформація про належне використання вибухової спам програми", inline=inline)
        embed.add_field(name=f"**b!mute_info** {zaha_emoji}", value=f"Інформація про використання b!mute", inline=inline)
        embed.add_field(name=f"**b!invite**", value=f"Створити запрошення на сервер для ваших друзів", inline=inline)
        embed.add_field(name=f"**b!pfp @(Нікнейм)**", value=f"Отримати аватар зазначеного користувача", inline=inline)
        embed.add_field(name=f"**b!kanava_info**", value=f"Інформація про покарання методом занурення до канави", inline=inline)
        embed.add_field(name=f"**b!rates (Валюта) (Кількість)**", value=f"Найактуальніший курс валют", inline=inline)
        embed.add_field(name=f"**b!stop**", value=f"Зупинити виконання усіх операцій", inline=inline)
        embed.add_field(name=f"**b!rg8421**", value=f"???", inline=inline)
        embed.set_image(url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/%D0%A2%D1%80%D0%B0%D0%B4%D0%B8%D1%86%D1%96%D1%8F_%D1%96_%D0%9F%D0%BE%D1%80%D1%8F%D0%B4%D0%BE%D0%BA.jpg/200px-%D0%A2%D1%80%D0%B0%D0%B4%D0%B8%D1%86%D1%96%D1%8F_%D1%96_%D0%9F%D0%BE%D1%80%D1%8F%D0%B4%D0%BE%D0%BA.jpg")
        embed.add_field(name=f"**Запрошення на найбазованіший сервер**", value=f"https://discord.gg/Ty5FcmEQkj", inline=inline)
        embed.add_field(name=f"||Команди з поміткою {zaha_emoji} може використовувати тільки модерація||\n\n\n*Розробник:* **@dani4feedyt#5200**", value=(f'*{version}*\n||*{patch_note}*||'), inline=inline)
        
        await ctx.send(embed=embed)

    @bot.command()
    async def pfp(ctx, member: discord.Member):
        print("Triggered... pfp; server: ctx.guild.name")
        c = 0
        if member.id == 783069117602857031:
            pfp = "**Традиція і Порядок!**"
        elif member.id == 486176412953346049:
            pfp = ("О НІ! МЕНІ НЕ БУЛО ДОЗВОЛЕНО РОЗГОЛОШУВАТИ ІНФОРМАЦІЮ ПРО СВОГО ТВОРЦЯ! Проводжу екстренне видалення даних")
        else:
            t3 = ["Сподіваюся що він гарненький!",
               "Аніме на аві - здоров'я мамі!", "Йой, хлопче, да ти ж красунчик!",
               "Маєш привабливу фотокартку!", "Одразу видно, справжнісінький українець!",
               "Йой, як файно!", "Де ж бо такі красунчики родяться?", "11/10!"]
            pfp = random.choice(t3)
        avatarUrl = member.avatar_url
        pfp_a = await ctx.send(f"Аватар користувача {member.mention}:")
        pfp_u = await ctx.send(avatarUrl) ##################Конвертер с webp в png
        pfp_t = await ctx.send(pfp)
        if member.id == 486176412953346049:
            while c <= 9:
                await asyncio.sleep(0.5)
                await pfp_t.edit(content="0 НІ! МеНІ НЕ БУЛО ДОЗВ ЛЕНО РОЗГОЛОШУВАТИ ІНФОРМА ІЮ ПРО СВОГО Т̶̲̏̐͛В̴̞̯̄О̵̢̩̠̦̳͉̾̋̏͛̕͝Р̴̛̟̱̦͉̭̹̱͖̓͆̀͐́̕͝Ц̴̳̞̍̋Я̷͚̣͉́̚! Проводжу екстренне ~~видалення~~ даних.")
                await asyncio.sleep(0.5)
                await pfp_t.edit(content="о НІ! МЕНІ НЕ БУЛО ДОЗВОлЕНО РОЗГОЛОШУВА И ІНФОРМАЦ1Ю ПРО СВОГО Т̶̖̳͙̦̰̘̐̊͗́̓̒̊̆̑В̶̢̬͈̗̙̒̆̆̊͛͠ͅО̶̜̗̲̙̝̝̪͊̂͗̔̾̈̄̚̚̚Р̸͖̒͛̊̓͊̄̑̿͝Ц̴̡̛̺̹̮͓̥̟͈̦͙̗̪̽́͋̿͌͌̇̇̌͠Я̵̫̤̞̽̾̈́͠! Проводжу екстренне видалення даних..")
                await asyncio.sleep(0.5)
                await pfp_t.edit(content="О НІ! МЕНі НЕ Б ЛО ДО3ВОЛЕНО РОЗГОЛОШУ8АТИ ІНФОРМАЦІЮ ПРО СВОГО Т̷͕͍͓̼̓̈В̷̪̳̩̯͑О̸̧̛̞͓̪̳̗͉̟Р̵̛̱̺̌̐̀͂̉̊͝Ц̸̱͎̦̘͈̈͋͛͆̒̄ͅͅЯ̷̢̇̐̇̈̄̏! Проводжу екстренне ~~видалення~~ даних...")
                c += 1
                if c == 3:
                    await pfp_a.delete()
                if c == 6:
                    await pfp_u.delete()
                if c == 9:
                    await pfp_t.delete()
                    await ctx.send("**Доступ відхилено.**")
            
    @bot.command(name="birb")
    async def birb(ctx):
        print("Triggered... birb; server: ctx.guild.name")
        t2 = ['Випадковий птах для тебе',
               'Тримай птаха', 'Випадковий птах, як ти й просив',
               'Світлина випадкового птаха', 'Світлина птаха, як ти й просив',
               'Тримай пташку', 'Тримай світлину птаха', 'Птах, як ти й побажав',
               'Світлина птаха']
        response = requests.get("https://some-random-api.ml/img/birb")
        json_data = json.loads(response.text)
        embed = discord.Embed(color = 0x013ADF, title = (f"{random.choice(t2)}, {random.choice(appeal)}:")) 
        embed.set_image(url = json_data["link"])
        await ctx.send(embed = embed)

    @bot.command(pass_context = True)
    async def t_check(message):
        print("Triggered... t_check; server: ctx.guild.name")
        channel = message.channel
        await channel.send("Чи бажаєте ви {String}?")
        def check(m):
            return (m.content.lower() == 'так' or m.content.lower() == 'да' or m.content.lower() == 'ага' or m.content.lower() == 'yes' or m.content.lower() == 'y') and m.channel == channel
        try:
            m = await bot.wait_for("message", check=check, timeout = 30)
        except asyncio.TimeoutError:
            print("TimeoutError")
        else:
            await channel.send("Підтверджено")
                
    @bot.command(pass_context = True)
    @commands.has_permissions(kick_members = True)
    async def kick(ctx, user: discord.Member, rule_n = None, *, reason = None):
        print("Triggered... kick; server: ctx.guild.name")
        if user == ctx.message.author:
            await ctx.send("**Помилка.** Ви не можете виключити себе.")
        else:
            reasonT = 0
            reasonA = 0
            author = ctx.message.author
            guild = ctx.guild
            if rule_n is None:
                rule_n = 0
            rule_n = int(rule_n)
            if 1 <= rule_n <= len(links):
                rule = (links[rule_n])
                ruleA = (f'**№{rule_n}**')
            else:
                rule = '⁣'
                ruleA = 'None'
            guild = ctx.guild
            author = ctx.message.author
            if reason == None:
                reasonT = ("**Без будь-якого приводу**")
                reasonA = '⁣'
            else:
                reasonT = 'Порушення:'
                reasonA = reason
            await ctx.send(f"Ви дійсно бажаєте виключити **{user}** з сереверу?", delete_after=60)
            def check(m):
                return (m.content.lower() == 'так' or m.content.lower() == 'да' or m.content.lower() == 'ага' or m.content.lower() == 'yes' or m.content.lower() == 'y')
            try:
                m = await bot.wait_for("message", check=check, timeout = 30)
            except asyncio.TimeoutError:
                print("TimeoutError")
            else:
                embed = discord.Embed(title="Вигнання", description=f'**{user}** був виключений з серверу модератором **{author.mention}**', color=0x013ADF)
                embed.add_field(name=reasonT, value=reasonA, inline=False)
                embed.add_field(name="Порушене правило:", value=ruleA, inline=False)
                await ctx.send(embed=embed)
                await ctx.send(rule)
                await user.send(f'Ви були виключені з серверу **{guild.name}** модератором **{author.mention}**, **{reasonT}** {reasonA}')
                await user.send(rule)
                await user.kick(reason = reason)
            
            
    @bot.command(name="rule")
    async def rule(ctx, num: int):
        print("Triggered... rule; server: ctx.guild.name")
        if 1 <= num <= len(links):
            await ctx.send(links[num])
        else:
            await ctx.send("**Помилка.** Правила під таким номером не існує")    
            
    @bot.command(name="pasta")
    async def pasta(ctx, pa: int):
        print("Triggered... pasta; server: ctx.guild.name")
        if 1 <= pa < 5:
            await ctx.send(Quotes1[pa])
        else:
            await ctx.send("**Помилка.** Вислів під цим номером ще не було вигадано, або не було занесено до моєї бази даних. \n*Для детальної інформації звертайтеся до @dani4feedyt#5200*")      

    @bot.command()
    async def quote(ctx: commands.Context):
        print("Triggered... quote; server: ctx.guild.name")
        _dict = random.choice(Quotes2)
        await ctx.send (f'Випадковий вислів Степана Андрійовича: \n\n***{_dict}***')
        
    @bot.command(aliases=['myroles'])
    async def _myroles(ctx):
        print("Triggered... _myroles; server: ctx.guild.name")
        member = ctx.message.author 
        member_roles = member.roles 
        await ctx.send(f"{member.mention} перелік твоїх ролей:\n{(member_roles).join(' ')}")

    @bot.command()
    @commands.has_permissions(manage_messages=True)
    async def kanava_info(ctx):
        print("Triggered... kanava_info; server: ctx.guild.name")
        await ctx.send("•Щоб почати занурювати користувача у **канаву**, введіть його нікнейм, кількість занурень та поблажливість бота у форматі: **b!kanava @(Нікнейм) (Кількість) (Довіра бота)**\n•Людина, що знаходиться під впливом цієї команди, буде занурюватися в канаву та допрошуватися особисто Бандерою\n\n||*Наприклад: b!kanava @user#5234 50*||")

    @bot.command()
    @commands.has_permissions(manage_messages=True)
    async def mute_info(ctx):
        print("Triggered... mute_info; server: ctx.guild.name")
        await ctx.send("•Щоб накласти **мут**, введіть нікнейм користувача, час муту та порушене правило у форматі: **b!mute @(Нікнейм) (Час у хвилинах) (Номер порушеного правила) (Деталі порушення)**\n•Людина, на яку було накладено мут, буде виключена із більшості голосових та текстових каналів і отримає особисте повідомлення з причиною муту\n•При закінченні терміну дії, мут буде автоматично знято\n•Для дострокового зняття муту скористайтеся командою **b!unmute**\n\n||*Наприклад: b!mute @user#5234 10 2 Порушення порядку на сервері*||")

    @bot.command()
    async def spam_info(ctx):
        print("Triggered... spam_info; server: ctx.guild.name")
        await ctx.send("•Щоб розпочати **спам**, введіть параметри швидкості та кількості слів у форматі: **b!spam (Кулдаун між повідомленнями) (Кількість повідомлень) (Слово для спаму)**\n\n||*Наприклад: b!spam 0.5 5 Бандера Бот - найкращий!*||")
    
    @bot.command(name="mute")
    @commands.has_permissions(manage_messages=True)
    async def mute(ctx, member: discord.Member, time: int, rule_n: int, *, reason=None):
        print("Triggered... mute")
        if 1 <= rule_n <= len(links):
            rule = (links[rule_n])
        else:
            rule = None
        guild = ctx.guild
        author = ctx.message.author
        mutedRole = discord.utils.get(guild.roles, name="Muted")
        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")
            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=True, read_message_history=True, read_messages=True, view_channel=False)
        embed = discord.Embed(title="Мут", description=f"**{member.mention}** був відправлений до муту модератором **{author.mention}** на **{time}** хвилин", color=0x013ADF)
        embed.add_field(name="Порушення:", value=reason, inline=False)
        embed.add_field(name="Порушене правило:", value=f'**№{rule_n}**', inline=False)
        await ctx.send(embed=embed)
        await ctx.send(rule)
        await member.add_roles(mutedRole)
        await asyncio.sleep(1)
        await member.edit(voice_channel=None)
        await member.send(f'На вас було накладено мут на сервері **{guild.name}** модератором **{author.mention}** на **{time}** хвилин, за причиною: **"{reason}"**')
        await member.send(rule)
        await asyncio.sleep(time * 60)
        bot.dispatch('mute_command', ctx, member, rule, reason, mutedRole, guild)

    @bot.event
    async def on_mute_command(ctx, member, rule, reason, mutedRole, guild):
        id1 = member.id
        user = await ctx.message.guild.query_members(user_ids=[id1])
        user = user[0]
        mutedRole = discord.utils.get(guild.roles, name="Muted")
        if mutedRole in user.roles:
            await member.remove_roles(mutedRole)
            await member.send(f"Час муту на сервері **{ctx.guild.name}** вийшов. Ви можете вільно продовжити спілкування!")
            embed = discord.Embed(title="Мут знято", description=f"Час муту **{member.mention}** вийшов. Приємного спілкування!", color=0x013ADF)
            await ctx.send(embed=embed)

    @bot.command()
    @commands.has_permissions(manage_messages=True)
    async def roles(ctx, member: discord.Member):
        print("Triggered... roles; server: ctx.guild.name")
        await ctx.send(member.roles)
            
    @bot.command(pass_context = True)
    @commands.has_permissions(manage_messages=True)
    async def unmute(ctx, member: discord.Member):
        print("Triggered... unmute; server: ctx.guild.name")
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
        else:
            await ctx.send("**Помилка.** Неможливо зняти мут з користувача, який його не має.")
            
    @bot.command()####################################ДОДЕЛАТЬ ТАЙМШТАМП ДЛЯ КЛИРА#################################
    async def t_time(ctx):
        print("Triggered... t_time; server: ctx.guild.name")
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

    @bot.command()
    async def t_count(ctx, d: int, m: int, h: int, mi: int):
        print("Triggered... t_count; server: ctx.guild.name")
        count = 0
        h-=2
        date = datetime.datetime(year = 2021, month=m, day=d, hour=h, minute=mi)
        async for message in ctx.channel.history(limit = None, after=date):
            count += 1
        await ctx.send(count)
        
    @bot.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def clear(ctx, amount = 100):
        print("Triggered... clear; server: ctx.guild.name")
        sfx = "ь"
        if 11<=amount<=14:
            sfx = "ь"
        elif (str(amount).endswith("1") or str(amount).endswith("2") or str(amount).endswith("3") or str(amount).endswith("4")):
            sfx = "ня"
        else:
            sfx = "ь"
        await ctx.send(f"Ви дійсно бажаєте очистити **{amount}** повідомлен{sfx}?", delete_after=60)
        def check(m):
            return (m.content.lower() == 'так' or m.content.lower() == 'да' or m.content.lower() == 'ага' or m.content.lower() == 'yes' or m.content.lower() == 'y')
        try:
            m = await bot.wait_for("message", check=check, timeout = 60)
        except asyncio.TimeoutError:
            print("TimeoutError")
        else:
            if int(amount) <= 150:
                await ctx.channel.purge(limit=int(amount+3))
                if int(amount) >= 100:
                    amount = 'дуууууже багато'
                time.sleep(0.75)    
                await ctx.send(f'Було видалено **{amount}** повідомлен{sfx}!', delete_after=60)
            else:
                await ctx.send("**Помилка.** Ви не можете видаляти більше 150 повідомлень!", delete_after=60)

    @bot.command(pass_context=True) ##########################################СДЕЛАТЬ ЧАСЫ И МИНУТЫ ОПЦИОНАЛЬНЫМИ, если оставляешь пропуск, ставится 00 00 #########################
    @commands.has_permissions(manage_messages=True)####'today' - Global var####
    async def clear_t(ctx, d: str, m: str, h: str, mi: str):
        print("Triggered... clear_t; server: ctx.guild.name")
        mi = int(mi)
        try:
            d = int(d)
        except ValueError:
            d = today.day
        try:
            m = int(m)
        except ValueError:
            m = today.month
        ye = today.year
        count = 0
        h = int(h)
        ho = h-2
        da = int(d)
        mo = int(m)
        if ho == -2:
            ho = 22
            da = int(d)-1
        if ho == -1:
            ho = 23
            da = int(d)-1
        if da == 0:
            mo -= 1
            da = list(months.values())[mo-1]
        if mo == 0:
            mo = 12
            ye -= 1
        h = str(h)
        mi = str(mi)
        d = str(d)
        m = str(m)
        date = datetime.datetime(year = int(ye), month=int(mo), day=int(da), hour=int(ho), minute=int(mi))
        await ctx.send("*Зачекайте, підраховую повідомлення…*", delete_after=60)
        async for message in ctx.channel.history(limit = None, after=date):
            count += 1
        amount = count
        sfx = "ь"
        if 11<=amount<=14:
            sfx = "ь"
        elif (str(amount).endswith("1") or str(amount).endswith("2") or str(amount).endswith("3") or str(amount).endswith("4")):
            sfx = "ня"
        else:
            sfx = "ь"
        if len(h) == 1:
            h = '0' + h################Возможно заменить функцией?
        if len(mi) == 1:
            mi = '0' + mi
        if len(d) == 1:
            d = '0' + d
        if len(m) == 1:
            m = '0' + m
        await ctx.send(f"Ви дійсно бажаєте очистити **{amount}** повідомлен{sfx} починаючи з **{h}:{mi} {d}-{m}-{ye}**?", delete_after=60)
        def check(m):
            return (m.content.lower() == 'так' or m.content.lower() == 'да' or m.content.lower() == 'ага' or m.content.lower() == 'yes' or m.content.lower() == 'y')
        try:
            m = await bot.wait_for("message", check=check, timeout = 60)
        except asyncio.TimeoutError:
            print("TimeoutError")
        else:
            if int(amount) <= 500:
                await ctx.channel.purge(limit=int(amount)+2)
                await ctx.send(f'Було видалено **{amount}** повідомлен{sfx}!', delete_after=60)
            else:
                await ctx.send("**Помилка.** Ви не можете видаляти більше 500 повідомлень!", delete_after=60)
    
    @bot.command()
    async def spam(ctx, intr: float = 1, count: int = 10, *ar):
        print("Triggered... spam; server: ctx.guild.name")
        attention = ("\n**Спам** розпочнеться через **5** секунд, для завершення - введіть **b!stop**")
        ar = list(ar)
        ar = (' '.join(ar))
        a = 0
        if intr < 0.5:
            await ctx.send("**Увага!** За швидкості спаму більшої за одне слово у **0.5** секунд, повідомлення можуть надсилатися некоректно.", delete_after=29)
            await ctx.send("Бажаєте продовжити операцію? Швидкість буде змінена на **0.5**", delete_after=29)
            def check(m):
                return (m.content.lower() == 'так' or m.content.lower() == 'да' or m.content.lower() == 'ага' or m.content.lower() == 'yes' or m.content.lower() == 'y')
            try:
                m = await bot.wait_for("message", check=check, timeout = 30)
            except asyncio.TimeoutError:
                os.system('python "Bandera_bot.py"')
                quit()
            else:
                if intr <= 0.3:
                    intr = 0.3
        await ctx.send(attention)
        time.sleep(5)
        while a < count:
            await ctx.send(ar)
            time.sleep(intr)
            a+=1
        await ctx.send("**Спам** було завершено")       
                
    @bot.command()
    async def stop(ctx: commands.Context):
        print("Triggered... stop; server: ctx.guild.name")
        os.system('python "Bandera_bot.py"')
        quit()
    
    @bot.command()
    async def ping(ctx):
        print("Triggered... ping; server: ctx.guild.name")
        await ctx.send(f'Моя затримка складає **{round(bot.latency, 3)}** с')
        
 ###############################################ErrorHandling###############################################

    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            print("Error... command: CommandNotFound")
            await ctx.send("**Помилка.** Даної команди не існує")
    
    @rates.error
    async def rates_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            print("Error... rates: MissingRequiredArgument")
            await ctx.send("**Помилка.** Будь ласка, введіть назву бажаної валюти.\nНа даний момент доступні курси: Долару, Євро, Шекеля, Рубля та Єни\n||**b!rates (Валюта)**||")
            
    @kanava.error
    async def kanava_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            print("Error... kanava: MissingRequiredArgument")
            await ctx.send("**Помилка.** Будь ласка, введіть усі необхідні параметри.\n||**b!kanava @(Нікнейм) (Кількість) (Довіра бота)**||")
        if isinstance(error, commands.MemberNotFound):
            print("Error... kanava: MemberNotFound")
            await ctx.send("**Помилка.** Користувача з таким нікнеймом не будо знайдено. Можливо, нікнейм будо введено некоректно")
        if isinstance(error, discord.HTTPException):
            print("Error... kanava: HTTPException")
            await ctx.send("**Помилка.** Користувач не знаходиться в голосовому каналі")

    @clear_t.error
    async def clear_t_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            print("Error... clear_t: MissingRequiredArgument")
            await ctx.send("**Помилка.** Будь ласка, введіть дату та час у коректному форматі.\n||**b!clear_t (День) (Місяць) (Години) (Хвилини)**||")
        if isinstance(error, commands.CommandInvokeError):
            print("Error... clear_t: CommandInvokeError")
            await ctx.send("**Помилка.** Введена дата некоректна.")

    @pfp.error
    async def pfp_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            print("Error... pfp: MissingRequiredArgument")
            await ctx.send("**Помилка.** Необхідний нікнейм користувача.")
        if isinstance(error, commands.MemberNotFound):
            print("Error... pfp: MemberNotFound")
            await ctx.send("**Помилка.** Користувача з таким нікнеймом не будо знайдено. Можливо, нікнейм будо введено некоректно.")
    
    @kick.error
    async def kick_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            print("Error... kick: MissingRequiredArgument")
            await ctx.send("**Помилка.** Будь ласка, введіть усі необхідні параметри.\n||**b!kick @(Нікнейм) (Причина)**||")
        if isinstance(error, commands.MemberNotFound):
            print("Error... kick: MemberNotFound")
            await ctx.send("**Помилка.** Користувача з таким нікнеймом не будо знайдено. Можливо, нікнейм будо введено некоректно, або цього користувача немає на сервері")

    @pasta.error
    async def pasta_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            print("Error... pasta: MissingRequiredArgument")
            await ctx.send("**Помилка.** Будь ласка, введіть номер бажаної пасти")

    @mute.error
    async def mute_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            print("Error... mute: MissingRequiredArgument")
            await ctx.send("**Помилка.** Будь ласка, введіть усі необхідні параметри.\n||**b!mute @(Нікнейм) (Час у хвилинах) (Порушене правило) (Причина)**||")
        if isinstance(error, commands.MemberNotFound):
            print("Error... mute: MemberNotFound")
            await ctx.send("**Помилка.** Користувача з таким нікнеймом не будо знайдено. Можливо, нікнейм будо введено некоректно")

    @unmute.error
    async def unmute_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            print("Error... unmute: MissingRequiredArgument")
            await ctx.send("**Помилка.** Будь ласка, введіть нікнейм користувача")
        if isinstance(error, commands.MemberNotFound):
            print("Error... unmute: MemberNotFound")
            await ctx.send("**Помилка.** Користувача з таким нікнеймом не будо знайдено. Можливо, нікнейм будо введено некоректно")

    @spam.error
    async def spam_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            print("Error... spam: MissingRequiredArgument")
            await ctx.send("**Помилка.** Будь ласка, введіть усі необхідні параметри\n||**b!spam (Кулдаун між повідомленнями) (Кількість повідомлень) (Слово для спаму)**||")
    
  ###############################################ErrorHandling###############################################      

    st = ("--- %s секунд ---" % round((time.time() - start_time), 3))
    
    @bot.command()
    async def start_time(ctx):
        print("Triggered... start_time; server: ctx.guild.name")
        await ctx.send(f'Цього разу, час мого запуску склав' + ' ' + st)
        
    print(st)
    bot.run(settings['token'])
    
except GeneratorExit:
    print("Error_12.1 (Generator_Error)")
