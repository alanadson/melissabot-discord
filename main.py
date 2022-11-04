import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="$", case_insensitive = True ,intents=intents)
slash = SlashCommand(client, sync_commands=True)

guilds_id = ['DISCORD_ID']

@client.event
async def on_ready():
    # Setting `Playing ` status
    await client.change_presence(activity=discord.Game(name="FokiFoki"))
    print("🚀Bot is ready!")

    # react emoji
    Channel = client.get_channel('CHANNEL_ID')
    Text = "Clique nos emojis abaixo para pegar seus respectivos cargos (😁 = FokiMember)"
    Moji = await Channel.send(Text)
    await Moji.add_reaction('😁')

# welcome member
@client.event
async def on_member_join(member):
   await client.get_channel('CHANNEL_ID').send(f" Olá {member.mention}😁, bem-vindo ao fokifoki!")

# goodbye member
@client.event
async def on_member_remove(member):
   await client.get_channel('CHANNEL_ID').send(f"{member.mention} saiu do servidor😭")


# ping command
@slash.slash(name="ping", description="Pong!", guild_ids=guilds_id)
async def _ping(ctx: SlashContext):
    await ctx.send("Pong!")

# clean chat
@slash.slash(name="clean_chat", guild_ids=guilds_id)
@commands.has_permissions(manage_messages=True)
async def _clean_chat(ctx: SlashContext, num):
    await ctx.send(f'🤖Você apagou {num} com sucesso!!!', hidden=True)
    await ctx.channel.purge(limit=int(num))

# member count
@slash.slash(name='qntmembros', description="Quantidade de membros no grupo", guild_ids=guilds_id)
async def _qntmembros(ctx: SlashContext):
    await ctx.send(ctx.guild.member_count)

# ban member
@slash.slash(name='ban', description='Descricao', guild_ids=guilds_id)
@commands.has_permissions(ban_members=True)
async def _ban(ctx: SlashContext,
               membro: discord.Member,
               motivo = 'Sem motivo registrado'):
    await membro.ban(reason=motivo)
    await ctx.send(f"O membro `{membro}` foi banido! A razão foi {motivo}")

# kick member
@slash.slash(name='kick', description='Descricao', guild_ids=guilds_id)
@commands.has_permissions(kick_members=True)
async def _kick(ctx: SlashContext,
               membro: discord.Member,
               motivo = 'Sem motivo registrado'):
    await membro.kick(reason=motivo)
    await ctx.send(f"O membro `{membro}` foi kickado! A razão foi {motivo}")

@client.event
# emoji reaction
async def on_reaction_add(reaction, user):
    Channel = client.get_channel('CHANNEL_ID')
    if reaction.message.channel.id != Channel.id:
        return
    if reaction.emoji == "😁":
      Role = discord.utils.get(user.guild.roles, name="ROLE_ID")
      await user.add_roles(Role)

client.run("MTAzMzYyODMxODkyODQ5MDU2Ng.G7l_V4.tt9reAI0FuP6L-2XrruPTiTiFg3ylLY_0oB6S8")