from pytils.mapper import IterMapper


class TestMapper:

    value = {"a": 1, "nested": {"b": 2}, "list": [{"c": 3}, {"c": 4}]}

    def test_get_item(self):
        obj = IterMapper([self.value], "nested.b")
        assert obj.__getitem__(0) == 2
        obj.__setitem__(0, -1)

        assert obj.__getitem__(0) == -1
        assert not self.value["nested"]["b"] == -1
        obj[0] = 5
        assert obj[0] == 5
