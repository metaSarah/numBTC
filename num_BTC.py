
def num_BTC(blockNum):
    
    numBTC = 0
    reward = 50

    while blockNum > 0:
        if blockNum >= 210000:
            numBTC = numBTC + (210000 * 50)
        else: 
            numBTC = blockNum * reward
        reward = reward/2
        blockNum = blockNum - 210000
    
    return float(numBTC)


