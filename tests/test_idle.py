from decimal import Decimal

from defi_protocols import Idle
from defi_protocols.constants import ETHEREUM, ETHTokenAddr

TEST_WALLET = "0x849D52316331967b6fF1198e5E32A0eB168D039d"
TEST_BLOCK = 16836190
LIDO_STAKED_TOKEN_ETH = "0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84"


def test_get_all_rewards():
    gauge = "0x675eC042325535F6e176638Dd2d4994F645502B9"
    rewards = Idle.get_all_rewards(TEST_WALLET, gauge, TEST_BLOCK, ETHEREUM)
    assert rewards == [[ETHTokenAddr.IDLE, Decimal("0")], [ETHTokenAddr.LDO, Decimal("31065.052700304643473107")]]


def test_get_amounts():
    amounts = Idle.get_amounts(
        underlying_address="0x956F47F50A910163D8BF957Cf5846D573E7f87CA",
        cdo_address="0x34dcd573c5de4672c8248cd12a99f875ca112ad8",
        aa_address="0x2688FC68c4eac90d9E5e1B94776cF14eADe8D877",
        bb_address="0x3a52fa30c33cAF05fAeE0f9c5Dfe5fd5fe8B3978",
        gauge_address=None,
        wallet=TEST_WALLET,
        block=TEST_BLOCK,
        blockchain=ETHEREUM,
    )
    assert amounts == [[ETHTokenAddr.FEI, Decimal("924.3773587200106717312902131")]]


def test_underlying():
    underlying = Idle.underlying(
        token_address=LIDO_STAKED_TOKEN_ETH, wallet=TEST_WALLET, block=TEST_BLOCK, blockchain=ETHEREUM, rewards=True
    )

    assert underlying == [
        [LIDO_STAKED_TOKEN_ETH, Decimal("924.3773587200106717312902131")],
        [[ETHTokenAddr.IDLE, Decimal("0")], [ETHTokenAddr.LDO, Decimal("31065.052700304643473107")]],
    ]


def test_underlying_all():
    wallet = "0x849D52316331967b6fF1198e5E32A0eB168D039d"
    underlying = Idle.underlying_all(wallet, 17295010, ETHEREUM, rewards=True)
    assert underlying == [
        [
            [ETHTokenAddr.STETH, Decimal("931.756327134769968317289982")],
            [[ETHTokenAddr.IDLE, Decimal("0")], [ETHTokenAddr.LDO, Decimal("31065.052700304643473107")]],
        ]
    ]


def test_get_addresses():
    addresses = Idle.get_addresses(TEST_BLOCK, ETHEREUM)
    assert addresses == {
        "tranches": [
            {
                "underlying_token": "0x956F47F50A910163D8BF957Cf5846D573E7f87CA",
                "CDO address": "0x77648a2661687ef3b05214d824503f6717311596",
                "AA tranche": {"aa_token": "0x9cE3a740Df498646939BcBb213A66BBFa1440af6", "aa_gauge": None},
                "bb token": "0x2490D810BF6429264397Ba721A488b0C439aA745",
            },
            {
                "underlying_token": "0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84",
                "CDO address": "0x34dcd573c5de4672c8248cd12a99f875ca112ad8",
                "AA tranche": {
                    "aa_token": "0x2688FC68c4eac90d9E5e1B94776cF14eADe8D877",
                    "aa_gauge": "0x675eC042325535F6e176638Dd2d4994F645502B9",
                },
                "bb token": "0x3a52fa30c33cAF05fAeE0f9c5Dfe5fd5fe8B3978",
            },
            {
                "underlying_token": "0xd632f22692FaC7611d2AA1C0D552930D43CAEd3B",
                "CDO address": "0x4ccaf1392a17203edab55a1f2af3079a8ac513e7",
                "AA tranche": {
                    "aa_token": "0x15794DA4DCF34E674C18BbFAF4a67FF6189690F5",
                    "aa_gauge": "0x7ca919Cf060D95B3A51178d9B1BCb1F324c8b693",
                },
                "bb token": "0x18cf59480d8c16856701F66028444546B7041307",
            },
            {
                "underlying_token": "0x5a6A4D54456819380173272A5E8E9B9904BdF41B",
                "CDO address": "0x151e89e117728ac6c93aae94c621358b0ebd1866",
                "AA tranche": {
                    "aa_token": "0xFC96989b3Df087C96C806318436B16e44c697102",
                    "aa_gauge": "0x8cC001dd6C9f8370dB99c1e098e13215377Ecb95",
                },
                "bb token": "0x5346217536852CD30A5266647ccBB6f73449Cbd1",
            },
            {
                "underlying_token": "0x43b4FdFD4Ff969587185cDB6f0BD875c5Fc83f8c",
                "CDO address": "0x008c589c471fd0a13ac2b9338b69f5f7a1a843e1",
                "AA tranche": {
                    "aa_token": "0x790E38D85a364DD03F682f5EcdC88f8FF7299908",
                    "aa_gauge": "0x21dDA17dFF89eF635964cd3910d167d562112f57",
                },
                "bb token": "0xa0E8C9088afb3Fa0F40eCDf8B551071C34AA1aa4",
            },
            {
                "underlying_token": "0x1AEf73d49Dedc4b1778d0706583995958Dc862e6",
                "CDO address": "0x16d88c635e1b439d8678e7bac689ac60376fbfa6",
                "AA tranche": {
                    "aa_token": "0x4585F56B06D098D4EDBFc5e438b8897105991c6A",
                    "aa_gauge": "0xAbd5e3888ffB552946Fc61cF4C816A73feAee42E",
                },
                "bb token": "0xFb08404617B6afab0b19f6cEb2Ef9E07058D043C",
            },
            {
                "underlying_token": "0xb9446c4Ef5EBE66268dA6700D26f96273DE3d571",
                "CDO address": "0x858f5a3a5c767f8965cf7b77c51fd178c4a92f05",
                "AA tranche": {
                    "aa_token": "0x158e04225777BBEa34D2762b5Df9eBD695C158D2",
                    "aa_gauge": "0xDfB27F2fd160166dbeb57AEB022B9EB85EA4611C",
                },
                "bb token": "0x3061C652b49Ae901BBeCF622624cc9f633d01bbd",
            },
            {
                "underlying_token": "0x06325440D014e39736583c165C2963BA99fAf14E",
                "CDO address": "0x7ecfc031758190eb1cb303d8238d553b1d4bc8ef",
                "AA tranche": {
                    "aa_token": "0x060a53BCfdc0452F35eBd2196c6914e0152379A6",
                    "aa_gauge": "0x30a047d720f735Ad27ad384Ec77C36A4084dF63E",
                },
                "bb token": "0xd83246d2bCBC00e85E248A6e9AA35D0A1548968E",
            },
            {
                "underlying_token": "0xe2f2a5C287993345a840Db3B0845fbC70f5935a5",
                "CDO address": "0x70320a388c6755fc826be0ef9f98bcb6bccc6fea",
                "AA tranche": {
                    "aa_token": "0xfC558914b53BE1DfAd084fA5Da7f281F798227E7",
                    "aa_gauge": "0x41653c7AF834F895Db778B1A31EF4F68Be48c37c",
                },
                "bb token": "0x91fb938FEa02DFd5303ACeF5a8A2c0CaB62b94C7",
            },
            {
                "underlying_token": "0xC9467E453620f16b57a34a770C6bceBECe002587",
                "CDO address": "0xf324dca1dc621fcf118690a9c6bae40fbd8f09b7",
                "AA tranche": {
                    "aa_token": "0x4657B96D587c4d46666C244B40216BEeEA437D0d",
                    "aa_gauge": "0x2bEa05307b42707Be6cCE7a16d700a06fF93a29d",
                },
                "bb token": "0x3872418402d1e967889aC609731fc9E11f438De5",
            },
            {
                "underlying_token": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
                "CDO address": "0xf5a3d259bfe7288284bd41823ec5c8327a314054",
                "AA tranche": {
                    "aa_token": "0x1e095cbF663491f15cC1bDb5919E701b27dDE90C",
                    "aa_gauge": "0x1CD24F833Af78ae877f90569eaec3174d6769995",
                },
                "bb token": "0xe11679CDb4587FeE907d69e9eC4a7d3F0c2bcf3B",
            },
            {
                "underlying_token": "0x6B175474E89094C44Da98b954EedeAC495271d0F",
                "CDO address": "0x46c1f702a6aad1fd810216a5ff15aab1c62ca826",
                "AA tranche": {
                    "aa_token": "0x852c4d2823E98930388b5cE1ed106310b942bD5a",
                    "aa_gauge": "0x57d59d4bBb0E2432f1698F33D4A47B3C7a9754f3",
                },
                "bb token": "0x6629baA8C7c6a84290Bf9a885825E3540875219D",
            },
            {
                "underlying_token": "0xdAC17F958D2ee523a2206206994597C13D831ec7",
                "CDO address": "0xd5469df8ca36e7eaedb35d428f28e13380ec8ede",
                "AA tranche": {
                    "aa_token": "0xE0f126236d2a5b13f26e72cBb1D1ff5f297dDa07",
                    "aa_gauge": "0x0C3310B0B57b86d376040B755f94a925F39c4320",
                },
                "bb token": "0xb1EC065abF6783BCCe003B8d6B9f947129504854",
            },
            {
                "underlying_token": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
                "CDO address": "0xe4cecd8e7cc1f8a45f0e7def15466be3d8031841",
                "AA tranche": {"aa_token": "0xB8110bCAC56472E687885aD4f39035fa026E171E", "aa_gauge": None},
                "bb token": "0x668a006E8A1043Eaec5117996644f0c393D188e6",
            },
            {
                "underlying_token": "0x1a7e4e63778B4f12a199C062f3eFdD288afCBce8",
                "CDO address": "0x2398bc075fa62ee88d7fab6a18cd30bff869bda4",
                "AA tranche": {
                    "aa_token": "0x624DfE05202b66d871B8b7C0e14AB29fc3a5120c",
                    "aa_gauge": "0x8f195979F7aF6C500b4688E492d07036c730c1B2",
                },
                "bb token": "0xcf5FD05F72cA777d71FB3e38F296AAD7cE735cB7",
            },
            {
                "underlying_token": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
                "CDO address": "0xdbcee5ae2e9daf0f5d93473e08780c9f45dfeb93",
                "AA tranche": {"aa_token": "0xb86264c21418aA75F7c337B1821CcB4Ff4d57673", "aa_gauge": None},
                "bb token": "0x4D9d9AA17c3fcEA05F20a87fc1991A045561167d",
            },
            {
                "underlying_token": "0x6B175474E89094C44Da98b954EedeAC495271d0F",
                "CDO address": "0xc8c64cc8c15d9aa1f4dd40933f3ef742a7c62478",
                "AA tranche": {"aa_token": "0xd54E5C263298E60A5030Ce2C8ACa7981EaAaED4A", "aa_gauge": None},
                "bb token": "0xD3E4C5C37Ba3185410550B836557B8FA51d5EA3b",
            },
            {
                "underlying_token": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
                "CDO address": "0x4bc5e595d2e0536ea989a7a9741e9eb5c3caea33",
                "AA tranche": {"aa_token": "0x5f45A578491A23AC5AEE218e2D405347a0FaFa8E", "aa_gauge": None},
                "bb token": "0x982E46e81E99fbBa3Fb8Af031A7ee8dF9041bb0C",
            },
            {
                "underlying_token": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
                "CDO address": "0xdbd47989647aa73f4a88b51f2b5ff4054de1276a",
                "AA tranche": {"aa_token": "0xa0154A44C1C45bD007743FA622fd0Da4f6d67D57", "aa_gauge": None},
                "bb token": "0x7a625a2882C9Fc8DF1463d5E538a3F39B5DBD073",
            },
            {
                "underlying_token": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
                "CDO address": "0xf6b692cc9a5421e4c66d32511d65f94c64fbd043",
                "AA tranche": {"aa_token": "0x3e041C9980Bc03011cc30491d0c4ccD53602F89B", "aa_gauge": None},
                "bb token": "0x65237B6Fc6E62B05B62f1EbE53eDAadcCd1684Ad",
            },
            {
                "underlying_token": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
                "CDO address": "0xf615a552c000b114ddaa09636bbf4205de49333c",
                "AA tranche": {"aa_token": "0x1AF0294524093BFdF5DA5135853dC2fC678C12f7", "aa_gauge": None},
                "bb token": "0x271db794317B44827EfE81DeC6193fFc277050F6",
            },
            {
                "underlying_token": "0xdAC17F958D2ee523a2206206994597C13D831ec7",
                "CDO address": "0x860b1d25903dbdffec579d30012da268aeb0d621",
                "AA tranche": {"aa_token": "0x6796FCd41e4fb26855Bb9BDD7Cad41128Da1Fd59", "aa_gauge": None},
                "bb token": "0x00B80FCCA0fE4fDc3940295AA213738435B0f94e",
            },
            {
                "underlying_token": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
                "CDO address": "0xec964d06cd71a68531fc9d083a142c48441f391c",
                "AA tranche": {"aa_token": "0x2B7Da260F101Fb259710c0a4f2EfEf59f41C0810", "aa_gauge": None},
                "bb token": "0x2e80225f383F858E8737199D3496c5Cf827670a5",
            },
            {
                "underlying_token": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
                "CDO address": "0x9c13ff045c0a994af765585970a5818e1db580f8",
                "AA tranche": {"aa_token": "0x376B2dCF9eBd3067BB89eb6D1020FbE604092212", "aa_gauge": None},
                "bb token": "0x86a40De6d77331788Ba24a85221fb8DBFcBC9bF0",
            },
            {
                "underlying_token": "0x6B175474E89094C44Da98b954EedeAC495271d0F",
                "CDO address": "0xdb82ddcb7e2e4ac3d13ebd1516cbfdb7b7ce0ffc",
                "AA tranche": {"aa_token": "0x69d87d0056256e3df7Be9b4c8D6429B4b8207C5E", "aa_gauge": None},
                "bb token": "0xB098AF638aF0c4Fa3edb1A24f807E9c22dA0fE73",
            },
            {
                "underlying_token": "0xdAC17F958D2ee523a2206206994597C13D831ec7",
                "CDO address": "0x440cead9c0a0f4dda1c81b892bedc9284fc190dd",
                "AA tranche": {"aa_token": "0x745e005a5dF03bDE0e55be811350acD6316894E1", "aa_gauge": None},
                "bb token": "0xF0C177229Ae1cd41BF48dF6241fae3e6A14A6967",
            },
            {
                "underlying_token": "0x6B175474E89094C44Da98b954EedeAC495271d0F",
                "CDO address": "0x264e1552ee99f57a7d9e1bd1130a478266870c39",
                "AA tranche": {"aa_token": "0x62Eb6a8c7A555eae3e0B17D42CA9A3299af2787E", "aa_gauge": None},
                "bb token": "0x56263BDE26b72b3e3D26d8e03399a275Aa8Bbfb2",
            },
            {
                "underlying_token": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
                "CDO address": "0xb3f717a5064d2cbe1b8999fdfd3f8f3da98339a6",
                "AA tranche": {"aa_token": "0x6c0c8708e2FD507B7057762739cb04cF01b98d7b", "aa_gauge": None},
                "bb token": "0xd69c52E6AF3aE708EE4b3d3e7C0C5b4CF4d6244B",
            },
            {
                "underlying_token": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
                "CDO address": "0x1329e8db9ed7a44726572d44729427f132fa290d",
                "AA tranche": {"aa_token": "0x9CAcd44cfDf22731bc99FaCf3531C809d56BD4A2", "aa_gauge": None},
                "bb token": "0xf85Fd280B301c0A6232d515001dA8B6c8503D714",
            },
            {
                "underlying_token": "0x6B175474E89094C44Da98b954EedeAC495271d0F",
                "CDO address": "0x5dca0b3ed7594a6613c1a2acd367d56e1f74f92d",
                "AA tranche": {"aa_token": "0x43eD68703006add5F99ce36b5182392362369C1c", "aa_gauge": None},
                "bb token": "0x38D36353D07CfB92650822D9c31fB4AdA1c73D6E",
            },
        ]
    }


def test_get_gauges():
    gauges = Idle.get_gauges(TEST_BLOCK, ETHEREUM)
    assert gauges == [
        ["0x21dDA17dFF89eF635964cd3910d167d562112f57", "0x790E38D85a364DD03F682f5EcdC88f8FF7299908"],
        ["0x675eC042325535F6e176638Dd2d4994F645502B9", "0x2688FC68c4eac90d9E5e1B94776cF14eADe8D877"],
        ["0x7ca919Cf060D95B3A51178d9B1BCb1F324c8b693", "0x15794DA4DCF34E674C18BbFAF4a67FF6189690F5"],
        ["0x8cC001dd6C9f8370dB99c1e098e13215377Ecb95", "0xFC96989b3Df087C96C806318436B16e44c697102"],
        ["0xDfB27F2fd160166dbeb57AEB022B9EB85EA4611C", "0x158e04225777BBEa34D2762b5Df9eBD695C158D2"],
        ["0x30a047d720f735Ad27ad384Ec77C36A4084dF63E", "0x060a53BCfdc0452F35eBd2196c6914e0152379A6"],
        ["0xAbd5e3888ffB552946Fc61cF4C816A73feAee42E", "0x4585F56B06D098D4EDBFc5e438b8897105991c6A"],
        ["0x41653c7AF834F895Db778B1A31EF4F68Be48c37c", "0xfC558914b53BE1DfAd084fA5Da7f281F798227E7"],
        ["0x2bEa05307b42707Be6cCE7a16d700a06fF93a29d", "0x4657B96D587c4d46666C244B40216BEeEA437D0d"],
        ["0x8f195979F7aF6C500b4688E492d07036c730c1B2", "0x624DfE05202b66d871B8b7C0e14AB29fc3a5120c"],
        ["0x1CD24F833Af78ae877f90569eaec3174d6769995", "0x1e095cbF663491f15cC1bDb5919E701b27dDE90C"],
        ["0x57d59d4bBb0E2432f1698F33D4A47B3C7a9754f3", "0x852c4d2823E98930388b5cE1ed106310b942bD5a"],
        ["0x0C3310B0B57b86d376040B755f94a925F39c4320", "0xE0f126236d2a5b13f26e72cBb1D1ff5f297dDa07"],
    ]
