
def num_BTC(blockNum):
    
    numBTC = 0
    reward = 50

    while blockNum > 0:
        if blockNum >= 210000:
            numBTC = numBTC + (210000 * reward)
        else: 
            numBTC = blockNum * reward
        reward = reward/2
        blockNum = blockNum - 210000
    
    return float(numBTC)


print(num_BTC(813574))
# 19522337.5