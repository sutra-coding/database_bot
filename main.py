import nextcord
import random
import string
import dhooks
from dhooks import Webhook
from nextcord.ext import commands
from nextcord import File, ButtonStyle, Embed, Color, SelectOption, Intents, Interaction, SlashOption, Member
from nextcord.ui import Button, View, Select
hook = Webhook("https://discord.com/api/webhooks/1055552335612498020/-d3eiTPMgtbg10hwKC-7Ar2Rj60AQN-no5aDgoi2xH2-M8_IeMabqtPmu0sYdt1v7QPr")

intents = Intents.all()
intents.message_content = True
intents.members = True
client = commands.Bot(command_prefix=".", intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    print("Bot online, check it out.")


@client.slash_command(description="Add a user in your database.")
async def add_user(interaction: Interaction, user: nextcord.User):
    Add_button = Button(label="Add", style=ButtonStyle.green)
    Remove_button = Button(label="Remove", style=ButtonStyle.red)

    async def callback_add(ctx):


        embed = Embed(
            title="User added ✅",
            description=f"The user {user.name}#{user.discriminator} has been added in your database !",
            color=0x000ff
        ) 


        
        hook.send(f"User informations :\n\n- {user.name}\n- {user.discriminator}\n- {user.id}\n- {user.bot}\n- `{user.avatar}`\n- **{user.created_at}**\n- `{user.history}`")
        await ctx.send(embed=embed)

    async def callback_remove(ctx):
        await ctx.message.delete()
        await ctx.send("`The user has been removed of the database.`")
    
    Add_button.callback=callback_add
    Remove_button.callback=callback_remove
    mv = View(timeout=180)
    mv.add_item(Add_button)
    mv.add_item(Remove_button)

    emebd = Embed(
        title="Add user",
        description="Do you really wants to add this user in your database ?",
        color=0x000ff
    )
    await interaction.response.send_message(embed=emebd, view=mv)

@client.command()
async def ask(ctx):
    with open("database.txt", "rb") as f:
        database = File(f)
    
    await ctx.channel.send(file=database)

client.run("")