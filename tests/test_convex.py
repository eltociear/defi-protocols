from decimal import Decimal

import pytest

from defi_protocols import Convex
from defi_protocols.constants import CRV_ETH, CVX_ETH, DAI_ETH, ETHEREUM, LDO_ETH, USDC_ETH, USDT_ETH, X3CRV_ETH
from defi_protocols.functions import get_contract, get_node

web3 = get_node(ETHEREUM)

CRV3CRYPTO = "0xc4AD29ba4B3c580e6D59105FFf484999997675Ff"
cDAI_plus_cUSDC = "0x845838DF265Dcd2c412A1Dc9e959c7d08537f8a2"
steCRV = "0x06325440D014e39736583c165C2963BA99fAf14E"


def test_get_pool_rewarder():
    rewarders = Convex.get_pool_rewarders(X3CRV_ETH, 16993460)
    assert rewarders == ["0x689440f2Ff927E1f24c72F1087E1FAF471eCe1c8"]


def test_get_rewards():
    rewarders = Convex.get_pool_rewarders(CRV3CRYPTO, 16993460)
    rw_contract = get_contract(rewarders[0], ETHEREUM, web3=web3, abi=Convex.ABI_REWARDS, block=16993460)
    wallet = "0x58e6c7ab55Aa9012eAccA16d1ED4c15795669E1C"
    rewards = Convex.get_rewards(web3, rw_contract, wallet, 16993460, ETHEREUM, decimals=False)
    assert rewards == [CRV_ETH, Decimal("2628703131997023420479")]


# @pytest.mark.parametrize('lp_token', [CRV3CRYPTO, cDAI_plus_cUSDC, steCRV])
@pytest.mark.parametrize("lp_token", [steCRV])
# @pytest.mark.parametrize('wallet', [TEST_WALLET,
@pytest.mark.parametrize("wallet", ["0x849D52316331967b6fF1198e5E32A0eB168D039d"])
# '0x58e6c7ab55Aa9012eAccA16d1ED4c15795669E1C',
# '0x849D52316331967b6fF1198e5E32A0eB168D039d'])
def test_get_extra_rewards(lp_token, wallet):
    rewarders = Convex.get_pool_rewarders(lp_token, 16993460)
    rw_contract = get_contract(rewarders[0], ETHEREUM, web3=web3, abi=Convex.ABI_REWARDS, block=16993460)
    extra_rewards = Convex.get_extra_rewards(web3, rw_contract, wallet, 16993460, ETHEREUM, decimals=False)
    assert extra_rewards == [[LDO_ETH, Decimal("1680694318843318519229")]]


def test_get_cvx_mint_amount():
    cvx_mint_amount = Convex.get_cvx_mint_amount(
        web3, Decimal("6649.47123882958317496"), 17499865, ETHEREUM, decimals=False
    )
    assert cvx_mint_amount == [CVX_ETH, Decimal("106.9162438469377937584223851")]


def test_get_all_rewards():
    all_rewards = Convex.get_all_rewards(
        "0x704617048F435cB679252E24148638211fb4457D", X3CRV_ETH, 17499865, ETHEREUM, web3
    )
    assert all_rewards[CRV_ETH] == Decimal("6649.47123882958317496")
    assert all_rewards[CVX_ETH] == Decimal("106.9162438469377937584223851")


def test_get_locked():
    locked = Convex.get_locked(
        "0x99e703dA6A29f68a603724BAc8B68d26d235ebf6", 17499865, ETHEREUM, web3, reward=False, decimals=False
    )
    assert locked == [[CVX_ETH, Decimal("2269137508655082138108")]]


def test_get_staked():
    staked = Convex.get_staked(
        "0xFDB3E523fc6F0D93fce8e57e282c503c5384d08F", 17499865, ETHEREUM, web3, reward=False, decimals=False
    )
    assert staked == [[CVX_ETH, Decimal("656399329913009873936")]]


def test_underlying():
    underlying = Convex.underlying(
        "0x704617048F435cB679252E24148638211fb4457D",
        X3CRV_ETH,
        17499865,
        ETHEREUM,
        web3,
        reward=True,
        decimals=False,
        no_curve_underlying=False,
    )

    assert underlying["balances"][DAI_ETH] == Decimal("1977384398964183941684361.059")
    assert underlying["balances"][USDC_ETH] == Decimal("2063566980143.462508297458104")
    assert underlying["balances"][USDT_ETH] == Decimal("5558574151627.356090237218803")
    assert underlying["rewards"][CRV_ETH] == Decimal("6649471238829583174960")
    assert underlying["rewards"][CVX_ETH] == Decimal("106916243846937793758.4223851")


def test_pool_balances():
    balances = Convex.pool_balances(X3CRV_ETH, 16993460, ETHEREUM, web3, decimals=False)
    assert balances == [
        [DAI_ETH, Decimal("165857824629254122209119338")],
        [USDC_ETH, Decimal("175604425510732")],
        [USDT_ETH, Decimal("92743777795510")],
    ]


@pytest.mark.skip(reason="Takes too long")
def test_update_db():
    data = Convex.update_db(save_to="/dev/null")
    assert data
