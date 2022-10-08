from phonenumbers import geocoder
import phonenumbers
from phonenumbers import carrier

num = '+18085567495'
ch_num = phonenumbers.parse(num, 'CH')
se_num = phonenumbers.parse(num, 'RO')

print(carrier.name_for_number(se_num, 'en'))
print(geocoder.description_for_number(ch_num, 'en'))
# A website to tell you which service provider is your SIM
