from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """Return two digit country code of the pygal"""
    for code,name in COUNTRIES.items():
        if name == country_name:
            return code
        elif country_name == 'Yemen, Rep.':
            return 'ye'
        elif country_name == 'Bahamas, The':
            return 'bs'
        elif country_name == 'Barbados':
            return 'bb'
        elif country_name == 'Bolivia':
            return 'bo'
        elif country_name == 'Congo, Dem. Rep.':
            return 'cd'
        elif country_name == 'Congo, Rep.':
            return 'cg'
        elif country_name == 'Egypt, Arab Rep.':
            return 'eg'
        elif country_name == 'Gambia, The':
            return 'gm'
        elif country_name == 'Hong Kong SAR, China':
            return 'hk'
        elif country_name == 'Iran, Islamic Rep.':
            return 'ir'
        elif country_name == 'Korea, Dem. Rep.':
            return 'kp'
        elif country_name == 'Korea, Rep.':
            return 'kr'
        elif country_name == 'Libya':
            return 'ly'
        elif country_name == 'Qatar':
            return 'qa'
        elif country_name == 'Tanzania':
            return 'tz'
        elif country_name == 'Venezuela, RB':
            return 've'
        elif country_name == 'Vietnam':
            return 'vn'
        elif country_name == 'Virgin Islands (U.S.)':
            return 'vi'
        elif country_name == 'Vanuatu':
            return 'vu'
        elif country_name == 'Trinidad and Tobago':
            return 'tt'
        elif country_name == 'St. Vincent and the Grenadines':
            return 'vc'
        elif country_name == 'Slovak Republic':
            return 'sk'
        elif country_name == 'Moldova':
            return 'md'
        elif country_name == 'Kosovo':
            return 'xk'
        elif country_name == 'Kyrgyz Republic':
            return 'kg'
        elif country_name == 'Grenada':
            return 'gd'
        elif country_name == 'St. Vincent and the Grenadines':
            return 'vc'
        elif country_name == 'Slovak Republic':
            return 'sk'
        elif country_name == 'Japan':
            return 'jp'


    # returns None if country is not found
    return None


