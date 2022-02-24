
# Set up
from messari.blockexplorers import Etherscan
import time
API_KEY='your_api_key'
es = Etherscan(api_key=API_KEY)

# Sushiswap Router, Ygov Contract
contracts = ['0xd9e1cE17f2641f24aE83637ab66a2cca9C378B9F', '0x0001FB050Fe7312791bF6475b96569D83F695C9f']

# Get contracts

contracts0 = ['0xA2B47E3D5c44877cca798226B7B8118F9BFb7A56','0x52EA46506B9CC5Ef470C5bf89f17Dc28bB35D85C','0x45F783CCE6B7FF23B2ab2D70e416cdb7D6055f51','0x79a8C46DeA5aDa233ABaFFD40F3A0A2B1e5A4F27']
contracts1 = ['0xA5407eAE9Ba41422680e2e00537571bcC53efBfD','0x06364f10B501e868329afBc005b3492902d6C763','0x93054188d876f558f4a66B2EF1d97d16eDf0895B','0x7fC77b5c7614E1533320Ea6DDc2Eb61fa00A9714']
contracts2 = ['0x4CA9b3063Ec5866A4B82E437059D2C43d1be596F','0xbebc44782c7db0a1a60cb6fe97d0b483032ff1c7','0x4f062658EaAF2C1ccf8C8e36D6824CDf41167956','0x3eF6A01A0f81D6046290f3e2A8c5b843e738E604']
contracts3 = ['0x3E01dD8a5E1fb3481F0F589056b428Fc308AF0Fb','0x0f9cb53Ebe405d49A0bbdBD291A65Ff571bC83e1','0x8474DdbE98F5aA3179B3B3F5942D724aFcdec9f6','0xC25099792E9349C7DD09759744ea681C7de2cb66']
contracts4 = ['0xC18cC39da8b11dA8c3541C598eE022258F9744da','0x8038C01A0390a8c547446a0b2c18fc9aEFEcc10c','0x7F55DDe206dbAD629C080068923b36fe9D6bDBeF','0x071c661B4DeefB59E2a3DdB20Db036821eeE8F4b']
contracts5 = ['0xd81dA8D904b52208541Bade1bD6595D8a251F8dd','0x890f4e345B1dAED0367A877a1612f86A1f86985f','0x0Ce6a5fF5217e38315f87032CF90686C96627CAA','0xc5424b857f758e906013f3555dad202e4bdb4567']
contracts6 = ['0xDeBF20617708857ebe4F679508E7b7863a8A8EeE','0xDC24316b9AE028F1497c275EB9192a3Ea0f67022','0xEB16Ae0052ed37f479f7fe63849198Df1765a733','0xA96A65c051bF88B4095Ee1f2451C2A9d43F53Ae2']
contracts7 = ['0x2dded6Da1BF5DBdF597C45fcFaa3194e53EcfeAF','0xF178C0b5Bb7e7aBF4e12A4838C7b7c5bA2C623c0','0x42d7025938bEc20B69cBae5A77421082407f053A','0xecd5e75afb02efa118af914515d6521aabd189f1']
contracts8 = ['0x4807862AA8b2bF68830e4C8dc86D0e9A998e085a','0xd632f22692FaC7611d2AA1C0D552930D43CAEd3B','0xEd279fDD11cA84bEef15AF5D39BB4d4bEE23F0cA','0xF9440930043eb3997fc70e1339dBb11F341de7A8']
contracts9 = ['0x43b4FdFD4Ff969587185cDB6f0BD875c5Fc83f8c','0x80466c64868E1ab14a1Ddf27A676C3fcBE638Fe5','0xD51a44d3FaE010294C616388b506AcdA1bfAAE46','0xfd5db7463a3ab53fd211b4af195c5bccc1a03890']
contracts10 = ['0x5a6A4D54456819380173272A5E8E9B9904BdF41B','0x98a7F18d4E56Cfe84E3D081B40001B3d5bD3eB8B','0x9838eCcC42659FA8AA7daF2aD134b53984c9427b','0x8301AE4fc9c624d1D396cbDAa1ed877821D7C511']
contracts11 = ['0x618788357D0EBd8A37e763ADab3bc575D54c2C7d','0xB576491F1E6e5E62f1d8F26062Ee822B40B0E0d4','0xAdCFcf9894335dC340f6Cd182aFA45999F45Fc44','0x98638FAcf9a3865cd033F36548713183f6996122']
contracts12 = ['0x752eBeb79963cf0732E9c0fec72a49FD1DEfAEAC','0xE7a24EF0C5e95Ffb0f6684b813A78F2a3AD7D171']

contract_groups = [contracts0,contracts1,contracts2,contracts3,contracts4,contracts5,contracts6,contracts7,contracts8,contracts9,contracts10,contracts11,contracts12]


abis = {}

count = 0
total = len(contract_groups)
for contract_group in contract_groups:
    print(f'run {count}/{total}') # Status-Bar
    count+=1

    tmp_dict = es.get_contract_abi(contract_group)
    time.sleep(1.5)
    abis.update(tmp_dict)

abi_values = abis.values()
abi_set = set(abi_values)

contract_count = len(abi_values)
set_count = len(abi_set)


grouping_dict = {}
for contract in abis:
    count = 0
    for abi in abi_set:
        if abis[contract] == abi:
            grouping_dict[contract] = count
        else:
            count+=1

print(grouping_dict)


print(f'{contract_count} contracts')

print(f'{set_count} unique ABIs')



