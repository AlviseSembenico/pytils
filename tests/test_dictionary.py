from pytils.dictionary import get_nested_value, get_nested_values, set_nested_value


class TestDictionary:

    value = {"a": 1, "nested": {"b": 2}, "list": [{"c": 3}, {"c": 4}]}

    def test_single_key(self):
        assert get_nested_value(self.value, "a") == 1

    def test_nested_key(self):
        assert get_nested_value(self.value, "nested.b") == 2

    def test_nested_list(self):
        assert list(get_nested_values(self.value, "list[].c")) == [3, 4]

    def test_set_nested_value(self):
        res = set_nested_value(self.value, "nested.b", -1)
        assert res["nested"]["b"] == -1
