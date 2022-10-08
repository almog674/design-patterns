"""
    File: 
    Porpuse: 
    Author: ALmog maimon
    Date: 
"""
from typing import Callable

subscribers = dict()


def subscribe(event_type: str, function: Callable):
    if not event_type in subscribers:
        subscribers[event_type] = []

    subscribers[event_type].append(function)


def post_event(event_type: str, data):
    if not event_type in subscribers:
        return

    for function in subscribers[event_type]:
        function(data)
