# File: utils/constants.py

# Constants for the Discord moderation bot

# Command prefixes
PREFIX = '!'
WARNING_COMMAND = 'warn'
LOGGING_COMMAND = 'log'
MUTE_COMMAND = 'mute'
KICK_COMMAND = 'kick'
BAN_COMMAND = 'ban'

# Messages
WARNING_ISSUED = 'Warning issued to user {user} for {reason}.'
USER_MUTED = 'User {user} has been muted.'
USER_KICKED = 'User {user} has been kicked from the server.'
USER_BANNED = 'User {user} has been banned from the server.'

# Error messages
INVALID_USER = 'Invalid user specified.'
INVALID_REASON = 'Invalid reason specified.'
USER_ALREADY_MUTED = 'User is already muted.'
USER_NOT_MUTED = 'User is not muted.'
USER_NOT_FOUND = 'User not found.'
USER_ALREADY_BANNED = 'User is already banned.'
USER_NOT_BANNED = 'User is not banned.'