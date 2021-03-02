try:
    import time
    
    start_time = time.time()
    
    import discord
    from discord.ext import commands
    from Bandera_cfg import settings
    from Bandera_Quotes import quotes
    from Bandera_PyChton_quotes import Quotes1
    import json
    import requests
    import os
    import sys
    import random
    from urllib.request import urlopen
    import lxml
    from lxml import etree
    from lxml import html
    from collections import Counter
    import asyncio
    from asyncio import sleep
    
    client = discord.Client()
    t12 = [", козаче", ", хлопче", ", друже", ", вуйко", ""]
    t11 = ['Випадковий птах для тебе' + random.choice(t12),
           'Тримай птаха' + random.choice(t12), 'Випадковий птах, як ти й просив' + random.choice(t12),
           'Світлина випадкового птаха' + random.choice(t12), 'Світлина птаха, як ти й просив' + random.choice(t12),
           'Тримай пташку' + random.choice(t12), 'Тримай світлину птаха' + random.choice(t12), 'Птах, як ти й побажав' + random.choice(t12),
           'Світлина птаха' + random.choice(t12)]
    bot = commands.Bot(command_prefix = settings['prefix'])
    attention = ("\n///Спам розпочнеться через 5 секунд, для завершення - введіть **b!stop**")
    w = ("Bandera_bot.py")

    @bot.command()
    async def slava_ukraine(ctx):
        author = ctx.message.author
        await ctx.send(f'Героям слава, {author.mention}!')

    @bot.command(pass_context = True)
    async def test(ctx, *, msg):
        await ctx.send(msg)
        await ctx.message.delete()

    @bot.command()
    async def info(ctx: commands.Context):
        zaha_emoji = ("<:Admin_Ebalo:698661524247412826>")
        await ctx.send(f'Патріотичий бот, який вміє робити деякі прикольні штуки:\n\n**b!slava_ukraine** - Головна функція Бандери\n**b!birb** - Світлина випадкового птаха\n**b!kick (Нікнейм)** - Заслання до Сибіру {zaha_emoji}\n**b!clear (Кількість повідомлень)** - Видалення повідомлень  {zaha_emoji}\n**b!quote** - Надішлю вам випадковий вислів Степана Андрійовича\n**b!pasta (Number 1-4)** - Один з крилатих висловів про так званий "Колюмбокс"\n**b!spam_info** - Інформація про належне використання вибухової спам програми\n**b!mute_info** - Інформація про використання b!mute  {zaha_emoji}\n**b!stop** - Зупинити виконання усіх операцій\n\n||Команди з поміткою {zaha_emoji} може використовувати тільки модерація||\n\n\n*Розробник:* **@dani4feedyt#5200**\n*ver.1.2.7*')

    @bot.command()
    async def birb(ctx):
        response = requests.get("https://some-random-api.ml/img/birb")
        json_data = json.loads(response.text)
        embed = discord.Embed(color = 0xff9900, title = (random.choice(t11)) + ":") 
        embed.set_image(url = json_data["link"])
        await ctx.send(embed = embed)
        
    @bot.command(pass_context = True)
    @commands.has_permissions(kick_members=True)
    async def kick(ctx, user: discord.Member, *, reason = None):
        await user.kick(reason = reason)

    @bot.command()
    async def pasta(ctx, pa: int):
        if pa < 5:
            await ctx.send(Quotes1[pa])
        else:
            await ctx.send("**Помилка.** Вислів під цим номером ще не було вигадано, або не було занесено до моєї бази даних. *Для детальної інформації звертайтеся до @dani4feedyt#5200*")      

    @bot.command()
    async def quote(ctx: commands.Context):
        await ctx.send((f'Випадковий вислів Бандери: \n\n')+(random.choice(quotes)))
        
    @bot.command(aliases=['myroles'])
    async def _myroles(ctx):
        member = ctx.message.author 
        member_roles = member.roles 
        await ctx.send(f"{member.mention} перелік твоїх ролей:\n{(member_roles).join(' ')}")

    @bot.command()
    @commands.has_permissions(manage_messages=True)
    async def mute_info(ctx):
        await ctx.send("Щоб накласти мут, введіть ім'я користувача, час муту та причину у форматі: **b!mute (Нікнейм) (Час у хвилинах) (Причина)**\nЛюдина, на яку було накладено мут, буде виключена із більшості голосових та текстових каналів, і отримає особисте повідомлення з причиною муту\nДля зняття муту скористайтеся командою **b!unmute**\n\n||*Наприклад: b!mute @user#5234 10 Порушення порядку на сервері*||")

    @bot.command(pass_context = True)
    @commands.has_permissions(manage_messages=True)
    async def mute(ctx, member: discord.Member, time: int, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")
        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")
            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=True, read_message_history=True, read_messages=True, view_channel=False)
        embed = discord.Embed(title="Мут", description=f"{member.mention} відлетів до муту на **{time}** хвилин", colour=discord.Colour.light_gray())
        embed.add_field(name="причина:", value=reason, inline=False)
        await ctx.send(embed=embed)
        await member.add_roles(mutedRole, reason=reason)
        await member.edit(voice_channel=None)
        await member.send(f" На вас було накладено мут на сервері {guild.name} на {time} хвилин, по причині: {reason}")
        await asyncio.sleep(time * 60)
        await member.remove_roles(mutedRole)
            
    @bot.command(pass_context = True)
    @commands.has_permissions(manage_messages=True)
    async def unmute(ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(mutedRole)
        await member.send(f" З вас було знято мут на сервері: - {ctx.guild.name}")
        embed = discord.Embed(title="Мут знято", description=f" Було знято мут з -{member.mention}",colour=discord.Colour.light_gray())
        await ctx.send(embed=embed)
    
    @bot.command(pass_context=True)
    async def clear(ctx, amount = 8192):
        await ctx.send(f'Ви дійсно бажаєте видалити {amount} повідомлень?')
        await ctx.channel.purge(limit=100)
        if amount == 8192:
            amount = 'дуууууже багато'
        time.sleep(0.75)    
        await ctx.send(f'Будо видалено {amount} повідомлень!')

    @bot.command()
    async def spam_info(ctx):
        await ctx.send("Щоб розпочати спам, введіть параметри швидкості та кількості слів у форматі: **b!spam (Швидкість відправки в секундах) (Кількість повідомлень) (Слово для спаму)**\n\n||*Наприклад: b!spam 0.5 5 Бандера Бот - найкращий!*||")

    @bot.command()
    async def spam(ctx, intr: float = 1, count: int = 10, *ar):
        ar = list(ar)
        ar = (' '.join(ar))
        a = 0
        if intr < 0.5:
            await ctx.send('Увага! За швидкості спаму меншої ніж 0.5 секунд, деякі повідомлення можуть надсилатися з затримкою')
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
        os.system('cls')
        os.execl(sys.executable, os.path.abspath(w), *sys.argv)
        quit()
    
    @bot.command()
    async def ping(ctx):       
        await ctx.send(f'Моя затримка складає {round(bot.latency, 3)} мс')
        
    st = ("--- %s секунд ---" % round((time.time() - start_time), 3))
    
    @bot.command()
    async def start_time(ctx):       
        await ctx.send(f'Цього разу, час мого запуску склав ' + st)
        
    print(st)
    bot.run(settings['token'])
    
except Exception:
    print("Error")
