import json
import discord
from discord_slash import SlashCommand

with open('config.json') as config_file:
    config = json.load(config_file)

guild_id = config['guild_id']
target_user_id = config['target_user_id']
role_name = config['role_name']
owner_id = config['owner_id']

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
slash = SlashCommand(client, sync_commands=True)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

async def create_funny_role(user):
    newRole = await user.guild.create_role(name=role_name, colour=discord.Colour(0xDA01E6))
    await user.add_roles(newRole)

@client.event
async def on_member_update(before, after):
    if after.id == target_user_id and len(before.roles) > len(after.roles):
        oldRole = next(role for role in before.roles if role not in after.roles)
        print("The role count has changed for", after)

        if oldRole.name == role_name:
            print("He lost the funny role, let's put it back rn!!!")
            try:
                await after.add_roles(oldRole)
            except:
                await create_funny_role(after)

guild_ids = [guild_id]

@slash.slash(name="dothefunny", description="do not attempt at home", guild_ids=guild_ids)
async def _dothefunny(ctx):
    await create_funny_role(client.get_guild(guild_id).get_member(target_user_id))
    await ctx.send(content="Let's fucking go!!!!!!!!!!!!", hidden=True)

@slash.slash(name="ping", description="go for the pong", guild_ids=guild_ids)
async def _ping(ctx):
    await ctx.send(content=f"Pong! ({client.latency*1000:.4f}ms)", hidden=True)

@slash.slash(name="shutdown", description="bye bye", guild_ids=guild_ids)
async def _exit(ctx):
    if ctx.author_id == owner_id:
        await ctx.send(content="ok I go poof", hidden=True)
        await client.close()
    else:
        await ctx.send(content="no u", hidden=True)


client.run(config['token'])
