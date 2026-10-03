import discord
from discord import app_commands
from discord.ext import commands

TOKEN = "PON_AQUI_EL_TOKEN_DE_TU_BOT"

intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} comandos sincronizados")
    except Exception as e:
        print(f"Error sincronizando comandos: {e}")


@bot.tree.command(name="presidente", description="Información del presidente")
async def presidente(interaction: discord.Interaction):
    await interaction.response.send_message(
        "🇮🇹 **Presidencia de la República**\n\n"
        "👤 Presidente: Pendiente de configurar\n"
        "🏛️ Gobierno: Pendiente de configurar"
    )


@bot.tree.command(name="gobierno", description="Información del Gobierno")
async def gobierno(interaction: discord.Interaction):
    await interaction.response.send_message(
        "🏛️ **Gobierno**\n\n"
        "Información del Gobierno pendiente de configurar."
    )


@bot.tree.command(name="comunicado", description="Publicar un comunicado oficial")
@app_commands.describe(texto="Texto del comunicado")
async def comunicado(interaction: discord.Interaction, texto: str):
    await interaction.response.send_message(
        f"📢 **COMUNICADO OFICIAL**\n\n{texto}"
    )


@bot.tree.command(name="decreto", description="Publicar un decreto")
@app_commands.describe(texto="Texto del decreto")
async def decreto(interaction: discord.Interaction, texto: str):
    await interaction.response.send_message(
        f"📜 **DECRETO PRESIDENCIAL**\n\n{texto}"
    )


@bot.tree.command(name="anuncio", description="Publicar un anuncio oficial")
@app_commands.describe(texto="Texto del anuncio")
async def anuncio(interaction: discord.Interaction, texto: str):
    await interaction.response.send_message(
        f"📣 **ANUNCIO OFICIAL**\n\n{texto}"
    )


bot.run(TOKEN)
