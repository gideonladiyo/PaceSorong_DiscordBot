import pytest
import asyncio
from unittest.mock import AsyncMock, patch, MagicMock
from discord.ext import commands
from discord import Message

pytestmark = pytest.mark.asyncio

@pytest.fixture
def test_bot():
    from bot import bot

    return bot


@patch("utils.read_save_data.read_data", return_value=[])
@patch("utils.read_save_data.save_data")
async def test_setrenunganchannel(mock_save_data, mock_read_data, test_bot):
    ctx = MagicMock()
    ctx.channel.id = 1371476522036105387
    ctx.send = AsyncMock()

    await test_bot.get_command("setrenunganchannel").callback(test_bot, ctx)

    mock_save_data.assert_called_once()
    ctx.send.assert_called_once()


@patch("utils.read_save_data.read_data", return_value=["1371476522036105387"])
@patch("utils.read_save_data.save_data")
async def test_cancelrenunganchannel(mock_save_data, mock_read_data, test_bot):
    ctx = MagicMock()
    ctx.channel.id = 1371476522036105387
    ctx.send = AsyncMock()

    await test_bot.get_command("cancelrenunganchannel").callback(test_bot, ctx)

    mock_save_data.assert_called_once()
    ctx.send.assert_called_once()


@patch("utils.generate_prompt.generate_prompt", return_value="dummy prompt")
@patch("google.generativeai.GenerativeModel.generate_content")
async def test_renunganmanual_pagi(
    mock_generate_content, mock_generate_prompt, test_bot
):
    ctx = MagicMock()
    ctx.send = AsyncMock()
    mock_response = MagicMock()
    mock_response.text = "Ini renungan pagi"
    mock_generate_content.return_value = mock_response

    await test_bot.get_command("renunganmanual").callback(test_bot, ctx, waktu="pagi")

    ctx.send.assert_any_call(
        "We kam pace @everyone, baca tong pu renungan pagi dulu ini."
    )
    ctx.send.assert_any_call("Ini renungan pagi")


async def test_renunganmanual_invalid_time(test_bot):
    ctx = MagicMock()
    ctx.send = AsyncMock()

    await test_bot.get_command("renunganmanual").callback(test_bot, ctx, waktu="siang")

    ctx.send.assert_called_once_with("⚠️ Waktu harus 'pagi' atau 'malam'.")


@patch(
    "utils.read_save_data.read_data", return_value={"1371413629567762525": ["bot"]}
)
@patch("utils.read_save_data.save_data")
@patch("utils.generate_prompt.generate_prompt", return_value="dummy prompt")
@patch("google.generativeai.GenerativeModel.generate_content")
async def test_pace_command(
    mock_generate_content,
    mock_generate_prompt,
    mock_save_data,
    mock_read_data,
    test_bot,
):
    ctx = MagicMock()
    ctx.channel.id = 1371413629567762525
    ctx.send = AsyncMock()
    mock_response = MagicMock()
    mock_response.text = "Pace: Oke kaka, ini jawaban dari sa"
    mock_generate_content.return_value = mock_response

    await test_bot.get_command("pace").callback(test_bot, ctx, pertanyaan="Apa kabar?")

    ctx.send.assert_any_call(" Oke kaka, ini jawaban dari sa")


@patch(
    "utils.read_save_data.read_data", return_value={"1371413629567762525": ["bot"]}
)
@patch("utils.read_save_data.save_data")
async def test_reset_command(mock_save_data, mock_read_data, test_bot):
    ctx = MagicMock()
    ctx.channel.id = 1371413629567762525
    ctx.send = AsyncMock()

    await test_bot.get_command("reset").callback(test_bot, ctx)

    ctx.send.assert_called_once_with(
        "🔄 Konteks percakapan su direset. Pace mulai baru lagi e!"
    )
