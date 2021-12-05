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
    
    client = discord.Client()
    t12 = [", козаче", ", хлопче", ", друже", ", вуйко", ""]
    sfx = "ь"
    t11 = ['Випадковий птах для тебе' + random.choice(t12),
           'Тримай птаха' + random.choice(t12), 'Випадковий птах, як ти й просив' + random.choice(t12),
           'Світлина випадкового птаха' + random.choice(t12), 'Світлина птаха, як ти й просив' + random.choice(t12),
           'Тримай пташку' + random.choice(t12), 'Тримай світлину птаха' + random.choice(t12), 'Птах, як ти й побажав' + random.choice(t12),
           'Світлина птаха' + random.choice(t12)]
    bot = commands.Bot(command_prefix = settings['prefix'])
    attention = ("\n///Спам розпочнеться через 5 секунд, для завершення - введіть **b!stop**")
    w = ("Bandera_bot.py")
    fi = open("data.txt","w+")
    data_filename = "data.txt"
    
    @bot.event
    async def on_member_join(member):
        await member.send(f"Вітаємо вас на сервері!\nЯ - **Бандера бот**, ваш персональний помічник, створений *dani4feedyt#5200*, який допоможе вам швидко зрозуміти правила та порядки серверу.\nДля отримання більш розгорнутої інформації, перейдіть до каналу **#info**")
        await member.send("https://media.discordapp.net/attachments/618165831943061791/819546666272161802/CSuO7F_wPr0.png?width=541&height=676")
        
    @bot.event
    async def on_ready():
        await bot.change_presence(activity = discord.Game('очке своим пальчиком | b!info'))

    @bot.command()
    async def id(ctx, member: discord.User):
        await ctx.send(member.id)

    @bot.command()
    async def save(ctx, *, msg):
        fi = open("data.txt","a+") ######Аппенд всместо написания######
        fi.write(msg + " ")
        fi.close

    @bot.command()
    async def read(ctx):
        fi = open("data.txt", "r")
        if fi.mode == 'r':
            contents = fi.read()
            await ctx.send(contents)
    
    @bot.command()
    async def c_save(ctx):
        fi = open("data.txt", "w").close()
            
    @bot.command()
    async def rg8421(ctx):
        author = ctx.message.author
        await ctx.send("<@" + str(696670757794742322) + ">," + f" {author.mention}" + " посягнул на великую тайну кала, и обнаружил рецепт сверхчистого говна:" + "\n||Гавно + Гавно - Гавно + Капелька поноса и три капельки говна высокой концентрации||")

    @bot.command(name='rates')
    async def rates(ctx, rate, amount=None):
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
        print(_dict1, _dict2, _dict3, _dict4, _dict5)
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
            await ctx.send("Курс даної валюти ще не було внесено до бази даних")
        bot.dispatch('rates_command', ctx, val, name, amount, rate)
    
    @bot.event
    async def on_rates_command(ctx, val, name, amount, rate):
        if amount is None:
            print('1')
            await ctx.send(f"Козаче, курс {name} становить **{val}** грн!")  
        else:
            rt = float(val) * float(amount)
            rt = round(rt, 2)
            rt = str(rt)
            if rt.endswith('0'):
                rt = rt[:-2]
            await ctx.send(f"{amount} {rate} становить **{rt}** грн!")

    @bot.command(name='kanava')
    @commands.has_permissions(manage_messages=True)
    async def kanava(ctx, member: discord.Member, t = 10, chance: int = 30, *, message = ''):
        channel1 = discord.utils.get(ctx.guild.voice_channels, name="ГУЛАГ (AFK)")
        channel2 = discord.utils.get(ctx.guild.voice_channels, name="Канава/МАрк (Марк и Марк)")
        print('1')
        bot.dispatch('kanava_command', ctx, channel1, channel2, member, t, chance, message)
        
    @bot.event
    async def on_kanava_command(ctx, channel1, channel2, member, t, chance, message):
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
                    await member.send("Бомбы, рупии есть? " + message)
                    def check(m):
                        return (m.content.lower() == 'есть' or m.content.lower() == 'да' or m.content.lower() == 'yes' or m.content.lower() == 'y' or m.content.lower() == 'так')
                    try:
                        m = await bot.wait_for("message", check=check, timeout = 1.5)
                    except asyncio.TimeoutError:
                        continue
                    else:
                        if rn <= ch:
                            await member.send("Хорошо, верю. Парни, вытаскивайте его!")
                            break
                        elif rn > ch:
                            await member.send("Не верю. Парни, окунайте его!")
                            continue
                if member.voice is None:
                    for nt in range(35):
                        if member.voice is not None:
                            break
                    
        await member.send("Ладно уж, иди своей дорогой")

    @bot.command()
    async def test11(ctx, member: discord.Member):
        guild = ctx.guild
        await ctx.send(f'{member}')
        await member.send(f"Вітаємо вас на сервері {ctx.guild.name}!\nЯ - **Бандера бот**, ваш персональний помічник, створений *@dani4feedyt#5200*, який допоможе вам швидко зрозуміти правила та порядки серверу.\nДля отримання більш розгорнутої інформації, перейдіть до каналу **#info**")
        await member.send("https://media.discordapp.net/attachments/618165831943061791/819546666272161802/CSuO7F_wPr0.png?width=541&height=676")

    @bot.command()
    async def invite_beta(ctx, member: discord.Member, age: int = 60):
        guild = ctx.guild
        message = discord.Message
        author = ctx.message.author
        link = await ctx.channel.create_invite(max_age = age*60)
        await member.send(f"{author.mention}запрошує вас на сервер {ctx.guild.name}!\n{link}")

    @bot.command(name="invite")
    async def invite(ctx, age: int = 60):
        link = await ctx.channel.create_invite(max_age = age*60)
        await ctx.send(f"Посилання для запрошення ваших друзів на {age} хв!\n{link}")

    @bot.command()
    async def slava_ukraine(ctx):
        author = ctx.message.author
        await ctx.send(f'Героям слава, {author.mention}!')

    @bot.command(pass_context = True)
    async def echo(ctx, *, msg):
        await ctx.send(msg)
        await ctx.message.delete()

    @bot.command(name="info")
    async def info(ctx: commands.Context, inline=False):
        zaha_emoji = ("<:Admin_Ebalo:698661524247412826>")
        embed = discord.Embed(title=f"Бандера бот", description=f"Патріотичий бот, який вміє робити деякі прикольні штуки:\n*Працює цілодобово!*", color=0x013ADF)
        embed.add_field(name=f"**b!slava_ukraine**", value=f"Головна функція Бандери", inline=inline)
        embed.add_field(name=f"**b!birb**", value=f"Світлина випадкового птаха", inline=inline)
        embed.add_field(name=f"**b!kick @(Нікнейм) (Порушення)** {zaha_emoji}", value=f"Вигнання на Соловки", inline=inline)
        embed.add_field(name=f"**b!clear (Кількість повідомлень)** {zaha_emoji}", value=f"Видалення повідомлень", inline=inline)
        embed.add_field(name=f"**b!quote**", value=f"Надішлю вам випадковий вислів Степана Андрійовича", inline=inline)
        embed.add_field(name=f"**b!pasta (Number 1-4)**", value=f'Один з крилатих висловів про так званий "Колюмбас"', inline=inline)
        embed.add_field(name=f"**b!spam_info**", value=f"Інформація про належне використання вибухової спам програми", inline=inline)
        embed.add_field(name=f"**b!mute_info** {zaha_emoji}", value=f"Інформація про використання b!mute", inline=inline)
        embed.add_field(name=f"**b!invite**", value=f"Створити запрошення на сервер для ваших друзів", inline=inline)
        embed.add_field(name=f"**b!kanava_info**", value=f"Інформація про покарання методом занурення до канави", inline=inline)
        embed.add_field(name=f"**b!rates (Валюта) (Кількість)**", value=f"Найактуальніший курс валют", inline=inline)
        embed.add_field(name=f"**b!stop**", value=f"Зупинити виконання усіх операцій", inline=inline)
        embed.add_field(name=f"**b!rg8421**", value=f"???", inline=inline)
        embed.set_image(url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/%D0%A2%D1%80%D0%B0%D0%B4%D0%B8%D1%86%D1%96%D1%8F_%D1%96_%D0%9F%D0%BE%D1%80%D1%8F%D0%B4%D0%BE%D0%BA.jpg/200px-%D0%A2%D1%80%D0%B0%D0%B4%D0%B8%D1%86%D1%96%D1%8F_%D1%96_%D0%9F%D0%BE%D1%80%D1%8F%D0%B4%D0%BE%D0%BA.jpg")
        embed.add_field(name=f"**Запрошення на найбазованіший сервер**", value=f"https://discord.gg/Ty5FcmEQkj", inline=inline)
        embed.add_field(name=f"||Команди з поміткою {zaha_emoji} може використовувати тільки модерація||\n\n\n*Розробник:* **@dani4feedyt#5200**", value='*ver 2.2.6C*', inline=inline)
        
        await ctx.send(embed=embed)
        
    @bot.command(name="birb")
    async def birb(ctx):
        response = requests.get("https://some-random-api.ml/img/birb")
        json_data = json.loads(response.text)
        embed = discord.Embed(color = 0x013ADF, title = (random.choice(t11)) + ":") 
        embed.set_image(url = json_data["link"])
        await ctx.send(embed = embed)

    @bot.command(pass_context = True)
    async def test12(message):
        channel = message.channel
        await channel.send("Чи бажаєте ви {String}?")
        def check(m):
            return (m.content.lower() == 'так' or m.content.lower() == 'да' or m.content.lower() == 'yes' or m.content.lower() == 'y') and m.channel == channel
        try:
            m = await bot.wait_for("message", check=check, timeout = 30)
        except asyncio.TimeoutError:
            print("Error")
        else:
            await channel.send("Підтверджено")
                
    @bot.command(pass_context = True) ###########################################Доработать rule в кике###########################################
    @commands.has_permissions(kick_members=True)
    async def kick(ctx, user: discord.Member, rule_n = None, *, reason = None):
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
            return (m.content.lower() == 'так' or m.content.lower() == 'да' or m.content.lower() == 'yes' or m.content.lower() == 'y')
        try:
            m = await bot.wait_for("message", check=check, timeout = 30)
        except asyncio.TimeoutError:
            print("Error")
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
        if 1 <= num <= len(links):
            await ctx.send(links[num])
        else:
            await ctx.send("**Помилка.** Правила під таким номером не існує")    
            
    @bot.command(name="pasta")
    async def pasta(ctx, pa: int):
        if 1 <= pa < 5:
            await ctx.send(Quotes1[pa])
        else:
            await ctx.send("**Помилка.** Вислів під цим номером ще не було вигадано, або не було занесено до моєї бази даних. *Для детальної інформації звертайтеся до @dani4feedyt#5200*")      

    @bot.command()
    async def quote(ctx: commands.Context):
        _dict = random.choice(Quotes2)
        await ctx.send (f'Випадковий вислів Степана Андрійовича: \n\n***{_dict}***')
        
    @bot.command(aliases=['myroles'])
    async def _myroles(ctx):
        member = ctx.message.author 
        member_roles = member.roles 
        await ctx.send(f"{member.mention} перелік твоїх ролей:\n{(member_roles).join(' ')}")

    @bot.command()
    @commands.has_permissions(manage_messages=True)
    async def kanava_info(ctx):
        await ctx.send("•Щоб почати занурювати користувача у канаву, введіть його нікнейм, кількість занурень та поблажливість бота у форматі: **b!kanava @(Нікнейм) (Кількість) (Довіра бота)**\n•Людина, що знаходиться під впливом цієї команди, буде занурюватися в канаву та допрошуватися особисто Бандерою\n\n||*Наприклад: b!kanava @user#5234 50*||")

    @bot.command()
    @commands.has_permissions(manage_messages=True)
    async def mute_info(ctx):
        await ctx.send("•Щоб накласти мут, введіть нікнейм користувача, час муту та порушене правило у форматі: **b!mute @(Нікнейм) (Час у хвилинах) (Номер порушеного правила) (Деталі порушення)**\n•Людина, на яку було накладено мут, буде виключена із більшості голосових та текстових каналів і отримає особисте повідомлення з причиною муту\n•При закінченні терміну дії, мут буде автоматично знято\n•Для дострокового зняття муту скористайтеся командою **b!unmute**\n\n||*Наприклад: b!mute @user#5234 10 2 Порушення порядку на сервері*||")

    
    @bot.command(name="mute")
    @commands.has_permissions(manage_messages=True)
    async def mute(ctx, member: discord.Member, time: int, rule_n: int, *, reason=None):
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
        await member.send(f'На вас було накладено мут на сервері **{guild.name}** модератором **{author.mention}** на **{time}** хвилин, за причиною: **"{reason}"**\n{rule}')
        print(member.roles, mutedRole)
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
        await ctx.send(member.roles)
    
            
    @bot.command(pass_context = True)
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
        else:
            await ctx.send("Помилка. Неможливо зняти мут з користувача, який його не має.")
    
    @bot.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def clear(ctx, amount = 100):
        if 11<=amount<=14:
            sfx = "ь"
        elif (str(amount).endswith("1") or str(amount).endswith("2") or str(amount).endswith("3") or str(amount).endswith("4")):
            sfx = "ня"
        else:
            sfx = "ь"
        await ctx.send(f"Ви дійсно бажаєте очистити **{amount}** повідомлен{sfx}?", delete_after=60)
        def check(m):
            return (m.content.lower() == 'так' or m.content.lower() == 'да' or m.content.lower() == 'yes' or m.content.lower() == 'y')
        try:
            m = await bot.wait_for("message", check=check, timeout = 30)
        except asyncio.TimeoutError:
            print("Error")
        else:
            if int(amount) <= 150:
                await ctx.channel.purge(limit=int(amount+3))
                if int(amount) >= 100:
                    amount = 'дуууууже багато'
                time.sleep(0.75)    
                await ctx.send(f'Було видалено **{amount}** повідомлен{sfx}!', delete_after=60)
            else:
                await ctx.send("Ви не можете видаляти більше 150 повідомлень!", delete_after=60)
            
    @bot.command()
    async def spam_info(ctx):
        await ctx.send("•Щоб розпочати спам, введіть параметри швидкості та кількості слів у форматі: **b!spam (Кулдаун між повідомленнями) (Кількість повідомлень) (Слово для спаму)**\n\n||*Наприклад: b!spam 0.5 5 Бандера Бот - найкращий!*||")

    @bot.command()
    async def spam(ctx, intr: float = 1, count: int = 10, *ar):
        ar = list(ar)
        ar = (' '.join(ar))
        a = 0
        if intr < 0.5:
            await ctx.send('Увага! За швидкості спаму більшої за одне слово у 0.5 секунд, деякі повідомлення можуть надсилатися з затримкою')
            if intr <= 0.3:
                intr = 0.3
        time.sleep(2)
        await ctx.send(attention)
        time.sleep(5)
        while a < count:
            await ctx.send(ar)
            time.sleep(intr)
            a+=1
        await ctx.send("///Спам було завершено")       
                
    @bot.command()
    async def stop(ctx: commands.Context):
        os.system('python "Bandera_bot.py"')
        quit()
    
    @bot.command()
    async def ping(ctx):       
        await ctx.send(f'Моя затримка складає {round(bot.latency, 3)} с')
        
 ###############################################ErrorHandling###############################################

    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Помилка. Даної команди не існує")
    
    @rates.error
    async def rates_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Помилка. Будь ласка, введіть назву бажаної валюти.\nНа даний момент доступний курс: Долару, Євро, Шекеля, Рубля та Єни\n||**b!rates (Валюта)**||")
            
    @kanava.error
    async def kanava_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Помилка. Будь ласка, введіть усі необхідні параметри.\n||**b!kanava @(Нікнейм) (Кількість) (Довіра бота)**||")
        if isinstance(error, commands.MemberNotFound):
            await ctx.send("Помилка. Користувача з таким нікнеймом не будо знайдено. Можливо, нікнейм будо введено некоректно")
        if isinstance(error, discord.HTTPException):
            await ctx.send("Помилка. Користувач не знаходиться в голосовому каналі")

    @kick.error
    async def kick_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Помилка. Будь ласка, введіть усі необхідні параметри.\n||**b!kick @(Нікнейм) (Причина)**||")
        if isinstance(error, commands.MemberNotFound):
            await ctx.send("Помилка. Користувача з таким нікнеймом не будо знайдено. Можливо, нікнейм будо введено некоректно, або цього користувача немає на сервері")

    @pasta.error
    async def pasta_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Помилка. Будь ласка, введіть номер бажаної пасти")

    @mute.error
    async def mute_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Помилка. Будь ласка, введіть усі необхідні параметри.\n||**b!mute @(Нікнейм) (Час у хвилинах) (Порушене правило) (Причина)**||")
        if isinstance(error, commands.MemberNotFound):
            await ctx.send("Помилка. Користувача з таким нікнеймом не будо знайдено. Можливо, нікнейм будо введено некоректно")

    @unmute.error
    async def unmute_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Помилка. Будь ласка, введіть нікнейм користувача")
        if isinstance(error, commands.MemberNotFound):
            await ctx.send("Помилка. Користувача з таким нікнеймом не будо знайдено. Можливо, нікнейм будо введено некоректно")

    @spam.error
    async def spam_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Помилка. Будь ласка, введіть усі необхідні параметри\n||**b!spam (Кулдаун між повідомленнями) (Кількість повідомлень) (Слово для спаму)**||")
    
  ###############################################ErrorHandling###############################################      

    st = ("--- %s секунд ---" % round((time.time() - start_time), 3))
    
    @bot.command()
    async def start_time(ctx):       
        await ctx.send(f'Цього разу, час мого запуску склав ' + st)
        
    print(st)
    bot.run(settings['token'])
    
except GeneratorExit:
    print("Error12")
