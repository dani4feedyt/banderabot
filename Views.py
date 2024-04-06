import random

import discord
import tictactoe as ttt
import time
from txt_f import ttt_titles, ttt_wins, ttt_loses, ttt_ties

import asyncio

X = "X"
O = "O"
EMPTY = None

user_player: int

current_label = [X, O]

wintxt = None
ai_turn = False
ai_win = -1


class Select(discord.ui.View):
    def __init__(self):
        super().__init__()


    @discord.ui.button(label=X, row=1, style=discord.ButtonStyle.success)
    async def x_callback(self, interaction, button: discord.ui.Button):
        button.disabled = True
        await interaction.response.edit_message(content="Ти обрав грати за **Х**, розпочинай!", view=self)
        global user_player
        user_player = 0
        player_select()
        Select.stop(self)
        msg = await interaction.original_response()
        await msg.edit(view=TicTacToe())

    @discord.ui.button(label=O, row=1, style=discord.ButtonStyle.danger)
    async def o_callback(self, interaction, button: discord.ui.Button):
        button.disabled = True
        await interaction.response.edit_message(content="Ти обрав грати за **0**, я розпочну.", view=self)
        global user_player
        user_player = 1
        player_select()
        Select.stop(self)
        msg = await interaction.original_response()
        await msg.edit(view=TicTacToe())


def clearup(view):
    global wintxt, ai_turn, ai_win
    if user_player == 1:
        view.board = ttt.initial_state(1)
    else:
        view.board = ttt.initial_state(0)
    ai_turn = False
    ai_win = -1
    wintxt = None
    ttt.generator()


def player_select():
    global user_player, current_label
    ai_p = 1
    if ai_p == user_player:
        ai_p = 0

    user_p = current_label[user_player]
    ai_p = current_label[ai_p]

    return user_p, ai_p


def ai_func(self, board, view):

    global ai_turn

    move = ()
    game_over = ttt.terminal(view.board)[0]
    player = ttt.player(view.board)

    if player_select()[0] != player and not game_over:
        if ai_turn:
            time.sleep(0.5)
            move = ttt.minimax(view.board)
            view.board = ttt.result(view.board, move)

            ai_turn = False
        else:
            ai_turn = True

        return view.board, move


class Button(discord.ui.Button['TicTacToe']):
    def __init__(self, x: int, y: int, label, style, disabled):
        super().__init__(style=style, label=label, row=y, disabled=disabled)
        self.x = x
        self.y = y

    async def callback(self, interaction: discord.Interaction):
        view: TicTacToe = self.view
        player = ttt.player(view.board)
        self.label = player
        view.board[self.y][self.x] = self.label
        self.disabled = True

        await interaction.response.edit_message(view=view)
        msg = await interaction.original_response()

        if not ttt.terminal(view.board)[0]:
            await msg.edit(content="Хмм... дай поміркувати...")
            view.recreate_board(view.board, True)
            await msg.edit(view=view)
            try:
                if ai_func(self, view.board, view)[0] is not None:
                    ai_func(self, view.board, view)
            except TypeError:
                await msg.edit(content="*Помилка* На ігровому полі виникла проблема, маю його очистити.")
                await asyncio.sleep(3)
                clearup(view)


        view.recreate_board(view.board, False)

        if wintxt is None:
            await msg.edit(content=f"{random.choice(ttt_titles)} Ходи.")
        else:
            await msg.edit(content=wintxt)
            if ai_win == 1:
                await msg.reply(content=random.choice(ttt_wins))
            elif ai_win == 0:
                await msg.reply(content=random.choice(ttt_loses))
            else:
                await msg.reply(content=random.choice(ttt_ties))

        await msg.edit(view=view)

class TicTacToe(discord.ui.View):
    children: list[Button]

    def __init__(self):
        super().__init__()

        self.board = ttt.initial_state(0)

        clearup(self)

        if user_player == 1:
            self.board = ttt.initial_state(1)

        self.recreate_board(self.board, False)

    def recreate_board(self, board, processing):
        self.clear_items()
        global wintxt, ai_win

        for x in range(3):
            for y in range(3):

                style = discord.ButtonStyle.secondary
                if board[y][x] is None:
                    label = 'ㅤ'
                    disabled = False
                else:
                    if board[y][x] == X:
                        style = discord.ButtonStyle.success
                    elif board[y][x] == O:
                        style = discord.ButtonStyle.danger
                    label = board[y][x]
                    disabled = True

                if ttt.terminal(self.board)[0]:
                    disabled = True
                    winner = ttt.winner(self.board)
                    if winner is None:
                        wintxt = "Гра закінчена. Нічия."
                    else:
                        if winner == player_select()[0]:
                            winner = "Ти"
                            ai_win = 0
                        else:
                            winner = "Я"
                            ai_win = 1
                        wintxt = f"Гра закінчена. {winner} переміг!"

                if processing:
                    disabled = True

                self.add_item(Button(x, y, label, style, disabled))

        print("board", board)
