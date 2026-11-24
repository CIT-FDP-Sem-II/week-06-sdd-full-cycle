"""Tests for the 5-ambiguity prompt. No API calls.

The prompt is used unchanged all week and again in Week 7. These tests pin
down the three rules that stop it padding.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from find_ambiguities import PROMPT


def test_prompt_demands_a_quote():
    """A finding you cannot quote cannot be checked against the source."""
    assert "QUOTE:" in PROMPT
    assert "word for word" in PROMPT


def test_prompt_demands_a_concrete_rewrite():
    assert "REWRITE:" in PROMPT
    assert "not a rewrite" in PROMPT


def test_prompt_asks_for_ranking():
    """Five unranked problems is a list. Ranked, it is a judgement."""
    assert "Rank them" in PROMPT


def test_prompt_gives_permission_to_find_fewer_than_five():
    """Without this, the model pads to five on a clean spec - which is
    exactly the failure test case T7 is looking for."""
    assert "do not invent" in PROMPT.lower()
    assert "fewer than five" in PROMPT


def test_prompt_does_not_leak_a_key():
    assert "AIza" not in PROMPT
