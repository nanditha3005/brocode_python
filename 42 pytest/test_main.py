from main import get_weather

def test_get_weather():
    assert get_weather(18) == "cold"
    assert get_weather(32) =="hot"