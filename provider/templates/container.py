import discord

class ExampleContainer:
    def embed(self, interaction):
        embed = discord.Embed(title=interaction.guild.name, description="")
        return embed
    
    def embedSuccess(self, interaction):
        embed = discord.Embed(title=interaction.guild.name, description="Success")
        return embed