def test_login_input_validation():
    with open("login.txt", encoding="utf-8-sig") as f:
        content = f.read()
    assert "Input validation" in content