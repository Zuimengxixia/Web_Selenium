from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = "python"
favorite_languages['sarah'] = 'C++'

for name,language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")