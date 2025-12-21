import discord

class ExampleButtons(discord.ui.View):
    def __init__(self, container):
        super().__init__(timeout=None)
        self.container = container

    @discord.ui.button(label="Button", style=discord.ButtonStyle.green, custom_id='example-button')
    async def button(self, interaction, button):
        # Code here
        ...

class ExampleModal(discord.ui.Modal, title="Example Modal"):
    def __init__(self, container):
        super().__init__(timeout=None)
        self.container = container

    input = discord.ui.TextInput(
        label="Your Input",
        placeholder="Type something...",
        required=True
    )

    async def on_submit(self, interaction: discord.Interaction):
        # Code here
        ...

class ExampleSeletor(discord.ui.View):
    def __init__(self, container):
        super().__init__(timeout=None)
        self.add_item(self.seletor())
        self.container = container

    def seletor(self):
        select = discord.ui.Select(
            custom_id='example-seletor',
            placeholder="placeholder",
            options = [
                discord.SelectOption(
                    label="Option 1"),
            ]
        )

        select.callback = self.select_callback
        return select

    async def select_callback(self, interaction:discord.Interaction):
        # Code here
        ...