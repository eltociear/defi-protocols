from decimal import Decimal

import pytest

from defi_protocols import Symmetric
from defi_protocols.constants import XDAI
from defi_protocols.functions import get_node


@pytest.mark.parametrize("decimals", [True, False])
def test_get_all_rewards(decimals):
    block = 27444181
    node = get_node(XDAI, block)
    wallet_v1 = "0x9b04a9eee500302980a117f514bc2de0fd1f683d"
    lptoken_address_v1 = "0x53ED0C2C6bB944D9421528E1ABD1e042B330696b"
    rewards_v1 = Symmetric.get_all_rewards(wallet_v1, lptoken_address_v1, block, XDAI, web3=node, decimals=decimals)
    assert rewards_v1 == {
        "protocol": "Symmetric",
        "blockchain": "xdai",
        "lptoken_address": "0x53ED0C2C6bB944D9421528E1ABD1e042B330696b",
        "block": 27444181,
        "rewards": [],
    }
    wallet_v2 = "0x2c640AC98E293Daa246F98D2828E328A06FA6936"
    lptoken_address_v2 = "0x650f5d96E83d3437bf5382558cB31F0ac5536684"
    rewards_v1 = Symmetric.get_all_rewards(wallet_v2, lptoken_address_v2, block, XDAI, web3=node, decimals=decimals)
    assert rewards_v1 == {
        "protocol": "Symmetric",
        "blockchain": "xdai",
        "lptoken_address": "0x650f5d96E83d3437bf5382558cB31F0ac5536684",
        "block": 27444181,
        "rewards": [
            {
                "token": "0xC45b3C1c24d5F54E7a2cF288ac668c74Dd507a84",
                "balance": Decimal("0.319599540070842681") if decimals else Decimal("319599540070842681"),
            },
            {
                "token": "0x9C58BAcC331c9aa871AFD802DB6379a98e80CEdb",
                "balance": Decimal("0.006197922467466093") if decimals else Decimal("6197922467466093"),
            },
        ],
    }


@pytest.mark.parametrize("decimals", [True, False])
def test_underlying(decimals):
    block = 27443088
    node = get_node(XDAI, block)
    wallet_v1 = "0x9b04a9eee500302980a117f514bc2de0fd1f683d"
    lptoken_address_v1 = "0x53ED0C2C6bB944D9421528E1ABD1e042B330696b"
    underlying_v1 = Symmetric.underlying(
        wallet_v1, lptoken_address_v1, block, XDAI, node, reward=False, decimals=decimals
    )
    assert underlying_v1 == {
        "protocol": "Symmetric",
        "blockchain": "xdai",
        "lptoken_address": "0x53ED0C2C6bB944D9421528E1ABD1e042B330696b",
        "block": 27443088,
        "unstaked": [
            {
                "token": "0x9C58BAcC331c9aa871AFD802DB6379a98e80CEdb",
                "balance": Decimal("0.09918343265529906587633112982")
                if decimals
                else Decimal("99183432655299065.87633112982"),
            },
            {
                "token": "0xe91D153E0b41518A2Ce8Dd3D7944Fa863463a97d",
                "balance": Decimal("8.122041293585052913340697534")
                if decimals
                else Decimal("8122041293585052913.340697534"),
            },
        ],
    }
    block = 27444181
    wallet_v2 = "0x2c640AC98E293Daa246F98D2828E328A06FA6936"
    lptoken_address_v2 = "0x650f5d96E83d3437bf5382558cB31F0ac5536684"
    underlying_v2 = Symmetric.underlying(
        wallet_v2, lptoken_address_v2, block, XDAI, node, reward=False, decimals=decimals
    )
    assert underlying_v2 == {
        "protocol": "Symmetric",
        "blockchain": "xdai",
        "lptoken_address": "0x650f5d96E83d3437bf5382558cB31F0ac5536684",
        "block": 27444181,
        "unstaked": [
            {
                "token": "0x9C58BAcC331c9aa871AFD802DB6379a98e80CEdb",
                "balance": Decimal("0E-18") if decimals else Decimal("0"),
            },
            {
                "token": "0xe91D153E0b41518A2Ce8Dd3D7944Fa863463a97d",
                "balance": Decimal("0E-18") if decimals else Decimal("0"),
            },
        ],
        "staked": [
            {
                "token": "0x9C58BAcC331c9aa871AFD802DB6379a98e80CEdb",
                "balance": Decimal("0.05341158140134450336962264979")
                if decimals
                else Decimal("53411581401344503.36962264979"),
            },
            {
                "token": "0xe91D153E0b41518A2Ce8Dd3D7944Fa863463a97d",
                "balance": Decimal("1.456160176840211550792382223")
                if decimals
                else Decimal("1456160176840211550.792382223"),
            },
        ],
    }
    underlying_v2_reward = Symmetric.underlying(
        wallet_v2, lptoken_address_v2, block, XDAI, node, reward=True, decimals=decimals
    )
    assert underlying_v2_reward == {
        "protocol": "Symmetric",
        "blockchain": "xdai",
        "lptoken_address": "0x650f5d96E83d3437bf5382558cB31F0ac5536684",
        "block": 27444181,
        "unstaked": [
            {
                "token": "0x9C58BAcC331c9aa871AFD802DB6379a98e80CEdb",
                "balance": Decimal("0E-18") if decimals else Decimal("0"),
            },
            {
                "token": "0xe91D153E0b41518A2Ce8Dd3D7944Fa863463a97d",
                "balance": Decimal("0E-18") if decimals else Decimal("0"),
            },
        ],
        "staked": [
            {
                "token": "0x9C58BAcC331c9aa871AFD802DB6379a98e80CEdb",
                "balance": Decimal("0.05341158140134450336962264979")
                if decimals
                else Decimal("53411581401344503.36962264979"),
            },
            {
                "token": "0xe91D153E0b41518A2Ce8Dd3D7944Fa863463a97d",
                "balance": Decimal("1.456160176840211550792382223")
                if decimals
                else Decimal("1456160176840211550.792382223"),
            },
        ],
        "rewards": [
            {
                "token": "0xC45b3C1c24d5F54E7a2cF288ac668c74Dd507a84",
                "balance": Decimal("0.319599540070842681") if decimals else Decimal("319599540070842681"),
            },
            {
                "token": "0x9C58BAcC331c9aa871AFD802DB6379a98e80CEdb",
                "balance": Decimal("0.006197922467466093") if decimals else Decimal("6197922467466093"),
            },
        ],
    }


@pytest.mark.parametrize("decimals", [True, False])
def test_pool_balances(decimals):
    block = 25502427
    node = get_node(XDAI, block)
    lptoken_address_v1 = "0x53ED0C2C6bB944D9421528E1ABD1e042B330696b"
    pool_balances_v1 = Symmetric.pool_balances(lptoken_address_v1, block, XDAI, web3=node, decimals=decimals)
    assert pool_balances_v1 == {
        "protocol": "Symmetric",
        "blockchain": "xdai",
        "lptoken_address": "0x53ED0C2C6bB944D9421528E1ABD1e042B330696b",
        "block": 25502427,
        "pool_balances": [
            {
                "token": "0x9C58BAcC331c9aa871AFD802DB6379a98e80CEdb",
                "balance": Decimal("12.584858151820221414") if decimals else Decimal("12584858151820221414"),
            },
            {
                "token": "0xe91D153E0b41518A2Ce8Dd3D7944Fa863463a97d",
                "balance": Decimal("711.653025596911491137") if decimals else Decimal("711653025596911491137"),
            },
        ],
    }
    lptoken_address_v2 = "0x870Bb2C024513B5c9A69894dCc65fB5c47e422f3"
    pool_balances_v2 = Symmetric.pool_balances(lptoken_address_v2, block, XDAI, web3=node, decimals=decimals)
    assert pool_balances_v2 == {
        "protocol": "Symmetric",
        "blockchain": "xdai",
        "lptoken_address": "0x870Bb2C024513B5c9A69894dCc65fB5c47e422f3",
        "block": 25502427,
        "pool_balances": [
            {
                "token": "0x3a97704a1b25F08aa230ae53B352e2e72ef52843",
                "balance": Decimal("237.906506136370454469") if decimals else Decimal("237906506136370454469"),
            },
            {
                "token": "0x9C58BAcC331c9aa871AFD802DB6379a98e80CEdb",
                "balance": Decimal("95.97151691604957935") if decimals else Decimal("95971516916049579350"),
            },
        ],
    }


@pytest.mark.parametrize("decimals", [True, False])
def test_get_rewards_per_second(decimals):
    block = 24502427
    node = get_node(XDAI, block)
    lptoken_address = "0x650f5d96E83d3437bf5382558cB31F0ac5536684"
    rewards = Symmetric.get_rewards_per_second(lptoken_address, block, XDAI, web3=node, decimals=decimals)
    assert rewards == {
        "protocol": "Symmetric",
        "blockchain": "xdai",
        "lptoken_address": "0x650f5d96E83d3437bf5382558cB31F0ac5536684",
        "block": 24502427,
        "reward_rates": [
            {
                "token": "0xC45b3C1c24d5F54E7a2cF288ac668c74Dd507a84",
                "rewards_per_second": Decimal("0.000234871031746032") if decimals else Decimal("234871031746032"),
            },
            {
                "token": "0x9C58BAcC331c9aa871AFD802DB6379a98e80CEdb",
                "rewards_per_second": Decimal("0.000005573390404850898876404494382")
                if decimals
                else Decimal("5573390404850.898876404494382"),
            },
        ],
    }
