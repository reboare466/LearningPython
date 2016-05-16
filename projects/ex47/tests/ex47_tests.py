from nose.tools import *
from ex47.game import Room

def test_room():
    gold = Room("GoldRoom",
						"""This room has gold in it you can grab. There's a
						door to the north."""
	assert gold.name == "GoldRoom"
	assert_equal(gold.paths, {})

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("I RAN!")