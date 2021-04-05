# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Part 1
player_dutch_10 = 'Ruud Gullit'
player_dutch_12 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54

scorers = player_dutch_10 + ' ' + str(goal_0) + ', ' + player_dutch_12 + ' ' + str(goal_1)

report = f"{player_dutch_10} scored in the {goal_0}nd minute\n{player_dutch_12} scored in the {goal_1}th minute"

# Part 2
player = 'Ronald Koeman'

space_position = player.find(' ')
first_name = player[:space_position]

last_name = player[(space_position+1):]
last_name_len = len(last_name)

first_letter = first_name[0]
name_short = f"{first_letter}. {last_name}"

first_name_len = len(first_name)
first_name_shout = first_name + '! '
chant_with_last_space = first_name_shout * first_name_len
chant = chant_with_last_space[:-1]

good_chant = (chant[-1] != ' ')