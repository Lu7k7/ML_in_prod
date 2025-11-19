from app import clean_item_input


def test_clean_item_input_strips_whitespace():
    input_text = "   hello world   "
    expected_output = "Hello World"
    assert clean_item_input(input_text) == expected_output

def test_clean_item_input_handles_empty_string():
    input_text = ""
    expected_output = ""
    assert clean_item_input(input_text) == expected_output