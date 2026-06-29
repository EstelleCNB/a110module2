from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Regression test for the str/int comparison bug (commit bb46841) ---
#
# The old code coerced the secret to a string on even attempts and then fell
# back to a lexicographic comparison inside check_guess. Lexicographically
# "9" > "50" is True and "100" < "20" is True, which is the opposite of the
# numeric ordering. These cases are chosen so a string comparison would return
# the WRONG outcome, locking in the clean numeric-comparison fix.
def test_check_guess_uses_numeric_not_lexicographic_comparison():
    # 9 < 50 numerically -> "Too Low"  (lexicographic "9" > "50" would say "Too High")
    outcome, _ = check_guess(9, 50)
    assert outcome == "Too Low"

    # 100 > 20 numerically -> "Too High"  (lexicographic "100" < "20" would say "Too Low")
    outcome, _ = check_guess(100, 20)
    assert outcome == "Too High"

    # The hint message must agree with the outcome. The buggy fallback paired
    # the "Too High" outcome with a "Go HIGHER" message.
    outcome, message = check_guess(100, 20)
    assert outcome == "Too High"
    assert "LOWER" in message
