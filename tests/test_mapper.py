from pytils.mapper import IterMapper


class TestMapper:

    value = {"a": 1, "nested": {"b": 2}, "list": [{"c": 3}, {"c": 4}]}
    value_list = [
        {"list": [{"c": 3}, {"c": 4}], "name": "a"},
        {"list": [{"c": 5}, {"c": 6}], "name": "b"},
    ]
    value_list_group = [
        {"list": [{"c": 3}, {"c": 4}], "name": "a"},
        {"list": [{"c": 5}, {"c": 6}], "name": "b"},
        {"list": [{"c": 5}, {"c": 6}], "name": "c"},
    ]

    def test_get_item(self):
        obj = IterMapper([self.value], "nested.b")
        assert obj.__getitem__(0) == 2
        obj.__setitem__(0, -1)

        assert obj.__getitem__(0) == -1
        assert not self.value["nested"]["b"] == -1
        obj[0] = 5
        assert obj[0] == 5

    def test_nested_list(self):
        obj = IterMapper(self.value_list, "list[].c")
        assert obj[0] == 3
        assert obj[1] == 4
        assert obj[2] == 5
        assert obj[3] == 6
        assert list(obj) == [3, 4, 5, 6]

    def test_group_by(self):
        obj = IterMapper(self.value_list_group, "list[].c")
        res = obj.group_by("list[].c", "name")
        assert 3 in res.keys()
        assert res[5] == ["b", "c"]
