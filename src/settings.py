"""
Global settings for forseti
"""

# LCM
LCM_URI='udpm://239.255.76.67:7667?ttl=1'


# enumeration of physical goals
BLUE_GOLD = 0
BLUE_PIRATE = 1
GOLD_GOLD = 2
GOLD_PIRATE = 3

# # Servo angular values for the two states
# SERVO_HELD = 10
# SERVO_RELEASED = 90

# # Dispensers numbers within the forest
# DISPENSER_LEFT = 0
# DISPENSER_RIGHT = 3
# DISPENSER_TELEOP_0 = 1
# DISPENSER_TELEOP_1 = 2

# # Game-derived values: everything that comes from the rulebook
# INITIAL_ALLIANCE_SCORE = 2 # each alliance starts with 2 balls on the field,
#                            # for a 2-2 initial score
# BONUS_INITIAL = 5
# BONUS_INCREMENT = 1
# BONUS_TIMER_SECONDS = 30.0
# GAME_PIECE_VALUE = 1
# PERMANENT_GOAL_VALUE = 3
# PERMANENT_GOAL_MAXIMUM = PERMANENT_GOAL_VALUE * 7
# BALL_VALUE_PER_DISPENSER = 5 # value of balls in the dispenser
# PENALTY_REGULAR = 5
# PENALTY_BONUS_TIMER = 5
# BAD_RFID_DISABLE_SECONDS = 3
# DISPENSER_RELEASE_POINTS = 4

AUTONOMOUS_LENGTH_SECONDS = 20
TELEOP_LENGTH_SECONDS = 120
