from decimal import Decimal

import pytest

from defi_protocols import UniswapV3
from defi_protocols.constants import ETHEREUM, ETHTokenAddr
from defi_protocols.functions import get_node

WALLET_N1 = "0x849D52316331967b6fF1198e5E32A0eB168D039d"
WALLET_N2 = "0x0EFcCBb9E2C09Ea29551879bd9Da32362b32fc89"
NFT_ID = 358770


@pytest.mark.parametrize("decimals", [False, True])
def test_underlying(decimals):
    block = 17094489
    node = get_node(ETHEREUM, block)

    x = UniswapV3.underlying(WALLET_N1, NFT_ID, block, ETHEREUM, web3=node, decimals=decimals, fee=True)
    y = Decimal(10**18 if decimals else 1)
    assert x == [
        [ETHTokenAddr.GNO, Decimal("98419156383881089964338.69948") / y],
        [ETHTokenAddr.WETH, Decimal("2210998677615110963219.938648") / y],
    ]


def test_allnfts():
    block = 17094489
    node = get_node(ETHEREUM, block)

    nfts = UniswapV3.allnfts(WALLET_N1, block, ETHEREUM, node)
    assert nfts == [
        185085,
        186529,
        189493,
        214704,
        214707,
        214716,
        218573,
        220361,
        217714,
        286920,
        339884,
        346143,
        358770,
        415282,
    ]


def test_underlying_all():
    block = 17119477

    balances = UniswapV3.underlying_all(WALLET_N2, block, ETHEREUM, fee=True)
    assert balances == [
        [
            [ETHTokenAddr.WBTC, Decimal("0.000007761923265277525510526250729")],
            [ETHTokenAddr.WETH, Decimal("0.001896950944013546473011431266")],
        ],
        [
            [ETHTokenAddr.WETH, Decimal("0.0005397922732214861340191702537")],
            [ETHTokenAddr.sETH2, Decimal("0.001391854480130107973608729216")],
        ],
        [
            [ETHTokenAddr.WBTC, Decimal("8.020662601714621409987468151")],
            [ETHTokenAddr.WETH, Decimal("194.4352083634992021665618551")],
        ],
    ]


def test_get_rate():
    block = 17094489
    node = get_node(ETHEREUM, block)

    position_nft = UniswapV3.NFTPosition(NFT_ID, ETHEREUM, block, node, decimals=True)
    assert UniswapV3.get_rate_uniswap_v3(
        position_nft.token0, position_nft.token1, block, ETHEREUM, node, UniswapV3.FeeAmount.MEDIUM
    ) == Decimal("0.05737047195982491454567443143")


@pytest.mark.parametrize("decimals", [False, True])
def test_get_fee(decimals):
    block = 17094489
    node = get_node(ETHEREUM, block)

    x = UniswapV3.get_fee(NFT_ID, block, web3=node, blockchain=ETHEREUM, decimals=decimals)
    y = Decimal(10**18 if decimals else 1)
    assert x == [
        ["0x6810e776880C02933D47DB1b9fc05908e5386b96", Decimal("474998434375840983379.1298473") / y],
        ["0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2", Decimal("25927112063507954904.89758316") / y],
    ]
