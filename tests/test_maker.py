from decimal import Decimal

from defi_protocols import Maker
from defi_protocols.constants import DAI_ETH, ETHEREUM, ETHTokenAddr
from defi_protocols.functions import get_node

TEST_BLOCK = 17070386
WEB3 = get_node(blockchain=ETHEREUM, block=TEST_BLOCK)
# TEST_WALLET = '0xf929122994e177079c924631ba13fb280f5cd1f9'
# TEST_WALLET = '0x849D52316331967b6fF1198e5E32A0eB168D039d'
TEST_WALLET = "0x4971DD016127F390a3EF6b956Ff944d0E2e1e462"
VAULT_ID = 27353


def test_get_vault_data():
    x = Maker.get_vault_data(VAULT_ID, TEST_BLOCK, WEB3)
    assert x == {
        "mat": Decimal("1.6"),
        "gem": ETHTokenAddr.wstETH,
        "dai": DAI_ETH,
        "ink": Decimal("57328.918780519001386926"),
        "art": Decimal("21811755.174275192209603126"),
        "Art": Decimal("131281671.560444627089962248"),
        "rate": Decimal("1.033782392295892171018325313"),
        "spot": Decimal("1456.9286150664385"),
        "line": Decimal("154522941.8359970071858062359"),
        "dust": Decimal("7500"),
    }


def test_underlying():
    x = Maker.underlying(VAULT_ID, TEST_BLOCK, WEB3)
    assert x == [
        [ETHTokenAddr.wstETH, Decimal("57328.918780519001386926")],
        [DAI_ETH, Decimal("-22548608.44423451266093976218")],
    ]


def test_get_delegated_MKR():
    x = Maker.get_delegated_MKR(TEST_WALLET, TEST_BLOCK, WEB3, decimals=False)
    assert x == [[ETHTokenAddr.MKR, Decimal("583805204609736124092")]]
