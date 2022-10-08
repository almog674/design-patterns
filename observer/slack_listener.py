"""
    File: 
    Porpuse: 
    Author: ALmog maimon
    Date: 
"""

from lib.slack import post_slack_message


def handle_user_registered_event(user):
    post_slack_message("sales", f"{user.name} has registered with the email {user.email}")

def handle_user_password_forgotten_event(user)

def setup_slack_event_handler():
    subscribe("user_registered", handle_user_registered_event())
