from txt_f import irritation_levels
import random
import asyncio


class Irritation:
    def __init__(self, engine, cursor):
        self.cur = cursor
        self.engine = engine
        self.interaction = None
        self.my_tasks = {}

    async def check_irritation(self, interaction):
        user_id = interaction.user.id

        self.cur.execute(
            f"SELECT irritation FROM irritator WHERE server_id = %s AND user_id = %s",
            [interaction.guild.id, interaction.user.id])
        result = self.cur.fetchone()

        if user_id in self.my_tasks:
            old_task = self.my_tasks[user_id]
            if not old_task.done():
                old_task.cancel()
                try:
                    await old_task
                except asyncio.CancelledError:
                    pass

        task = asyncio.create_task(self.clear(interaction))
        self.my_tasks[user_id] = task

        print(f"Active tasks: {list(self.my_tasks.keys())}")
        if result[0] == 0:
            return None
        elif 1 <= result[0] < 5:
            return random.choice(irritation_levels.get("low"))
        elif 5 <= result[0] < 9:
            return random.choice(irritation_levels.get("medium"))
        elif 9 <= result[0] < 13:
            return random.choice(irritation_levels.get("high"))
        else:
            self.cur.execute(
                f"UPDATE irritator SET irritation = 0 WHERE user_id = %s AND server_id = %s",
                [user_id, interaction.guild.id])
            self.engine.commit()
            return "*Тут має бути трігер команди мут, ворк ін прогрес, Даня пачіні((*"

    async def clear(self, interaction):
        try:
            await asyncio.sleep(60)
            self.cur.execute(f"DELETE FROM irritator WHERE server_id = %s AND user_id = %s",
                             [interaction.guild.id, interaction.user.id])
            self.engine.commit()
            print(f"Removed inst for {interaction.user.id}")
        except asyncio.CancelledError:
            print(f"Reset cancelled for {interaction.user.id}")
            raise
        finally:
            self.my_tasks.pop(interaction.user.id, None)


