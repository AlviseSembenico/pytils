from pytils.dictionary import get_nested_values


class TestDictionary:

    value = {"a": 1, "nested": {"b": 2}, "list": [{"c": 3}, {"c": 4}]}

    def test_single_key(self):
        assert get_nested_values(self.value, "a") == 1

    def test_nested_key(self):
        assert get_nested_values(self.value, "nested.b") == 2

    def test_nested_list(self):
        assert get_nested_values(self.value, "list[].c") == [3, 4]
