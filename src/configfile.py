import os
import sys
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.

my_address = os.getenv('PANCAKE_BOT_ADDRESS')
my_pk = os.getenv('PANCAKE_BOT_PK')

max_slippage ='0.03'
incaseofbuyinghowmuch='1'


ethtokeep='5'

speed='schnell'
maincoinoption='BNB'
mcotoseeassell='10'

diffdepositaddress=''
maxgweinumber='5'
diffdeposit='0'
maxgwei='1'
secondswaitaftertrade='80'
secondscheckingprice_2='80'
secondscheckingprice='4'
infuraurl='https://bsc-dataseed1.binance.org:443'
tokentokennumerator='3.3''

# CAKE
######
activatetoken1='1' 
checkpricetoken1='0'
tradewithETHtoken1='0'
tradewithERCtoken1='0'
token1ethaddress='0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82'
token1low='0.04919788'
token1high='0.05183798'
#
activatetoken2='0'
checkpricetoken2='1'
tradewithETHtoken2='0'
tradewithERCtoken2='0'
token2ethaddress='0'
token2low='0.00001'
token2high='99999'
activatetoken3='0'
checkpricetoken3='1'
tradewithETHtoken3='0'
tradewithERCtoken3='0'
token3ethaddress='0'
token3low='0.00001'
token3high='99999'
activatetoken4='0'
checkpricetoken4='1'
tradewithETHtoken4='0'
tradewithERCtoken4='0'
token4ethaddress='0'
token4low='0.00001'
token4high='99999'
activatetoken5='0'
checkpricetoken5='1'
tradewithETHtoken5='0'
tradewithERCtoken5='0'
token5ethaddress='0'
token5low='0.00001'
token5high='99999'
activatetoken6='0'
checkpricetoken6='1'
tradewithETHtoken6='0'
tradewithERCtoken6='0'
token6ethaddress='0'
token6low='0.00001'
token6high='99999'

activatetoken7='0'
checkpricetoken7='0'
tradewithETHtoken7='0'
tradewithERCtoken7='0'
token7ethaddress='0'
token7low='0.00001'
token7high='99999'

activatetoken8='0'
checkpricetoken8='0'
tradewithETHtoken8='0'
tradewithERCtoken8='0'
token8ethaddress='0'
token8low='0.00001'
token8high='99999'

activatetoken9='0'
checkpricetoken9='0'
tradewithETHtoken9='0'
tradewithERCtoken9='0'
token9ethaddress='0'
token9low='0.00001'
token9high='99999'

activatetoken10='0'
checkpricetoken10='0'
tradewithETHtoken10='0'
tradewithERCtoken10='0'
token10ethaddress='0'
token10low='0.00001'
token10high='99999'


token1name='CAKE'
token2name='0'
token3name='0'
token4name='0'
token5name='0'
token6name='0'
token7name='0'
token8name='0'
token9name='0'
token10name='0'

token1decimals='18'
token2decimals='18'
token3decimals='18'
token4decimals='18'
token5decimals='18'
token6decimals='18'
token7decimals='18'
token8decimals='18'
token9decimals='18'
token10decimals='18'


token1stoploss='0'
token2stoploss='0'
token3stoploss='0'
token4stoploss='0'
token5stoploss='0'
token6stoploss='0'
token7stoploss='0'
token8stoploss='0'
token9stoploss='0'
token10stoploss='0'

stoplosstoken1='0'
stoplosstoken2='0'
stoplosstoken3='0'
stoplosstoken4='0'
stoplosstoken5='0'
stoplosstoken6='0'
stoplosstoken7='0'
stoplosstoken8='0'
stoplosstoken9='0'
stoplosstoken10='0'

debugmode='0'

my_address = '0'
my_pk = '0'

sys.path.append(".")