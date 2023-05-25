from phonenumbers import geocoder
import phonenumbers
from phonenumbers import carrier

num = '+18085567495'
thi = "+2347048747638"
# ch_num = phonenumbers.parse(num, 'CH')
se_num = phonenumbers.parse(thi)

# print(carrier.name_for_number(ch_num, 'en'))
# print(geocoder.description_for_number(ch_num, 'en'))

location = geocoder.description_for_number(se_num, 'en')
print(carrier.name_for_number(se_num, 'en'))
print(geocoder.description_for_number(se_num, 'en'))
# A website to tell you which service provider is your SIM
print(location)
