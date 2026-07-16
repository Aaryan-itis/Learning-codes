full_dot = '●'
empty_dot = '○'
def create_character(name, Str, Int, Cha) :
    if not isinstance(name, str) :
        return 'The character name should be a string'
    if name == '' :
        return 'The character should have a name'
    if len(name) > 10 :
        return 'The character name is too long'
    if ' ' in name :
        return 'The character name should not contain spaces'
    if not isinstance(Str, int) or not isinstance(Int, int) or not isinstance(Cha, int) :
        return 'All stats should be integers'
    if Str < 1 or Int < 1 or Cha < 1 :
        return 'All stats should be no less than 1'
    if Str > 4 or Int > 4 or Cha > 4 :
        return 'All stats should be no more than 4'
    points = Str + Int + Cha
    if not points == 7 :
        return 'The character should start with 7 points'
    else :
        Dot_s = 10 - Str
        Dot_i = 10 - Int
        Dot_c = 10 - Cha
        add_s = full_dot*Str+empty_dot*Dot_s
        add_i = full_dot*Int+empty_dot*Dot_i
        add_c = full_dot*Cha+empty_dot*Dot_c
        return f"""{name}
STR {add_s}
INT {add_i}
CHA {add_c}"""
name = input('Enter your character name: ')
print('You have 7 points to distribute between Strength, Intelligence, and Charisma. Each stat must be between 1 and 4.')
Str = int(input('Enter your character Strength (1-4): '))
Int = int(input('Enter your character Intelligence (1-4): '))
Cha = int(input('Enter your character Charisma (1-4): '))
result = create_character(name, Str, Int, Cha)
print(result)