import abc
from typing import Type

import jsonpath_rw
from hamcrest import assert_that, equal_to


class Condition(object):

    def __init__(self):
        pass

    @abc.abstractmethod
    def match(self, response):
        return


class StatusCodeCondition(Condition):

    def match(self, response):
        assert response.status_code == self._status_code, "Wrong Status Code"

    def __init__(self, code):
        super().__init__()
        self._status_code = code.value

    def __repr__(self):
        return "Status code is {}".format(self._status_code)


status_code: Type[StatusCodeCondition] = StatusCodeCondition


class BodyFieldCondition(Condition):

    def __init__(self, json_path, matcher=None):
        super().__init__()
        self._json_path = json_path
        self._matcher = matcher

    def __repr__(self):
        return "Body field {} is {}".format(self._json_path, self._matcher)

    def match(self, response):
        json = response.json()
        jsonpath_expression = jsonpath_rw.parse(self._json_path)
        match = jsonpath_expression.find(json)
        assert_that(match[0].value, self._matcher)

    def contains(self, response):
        json = response.json()
        jsonpath_expression = jsonpath_rw.parse(self._json_path)
        matched_values = [match.value for match in jsonpath_expression.find(json)]
        assert_that(matched_values, self._matcher)

    def match_json(self, json_object):
        jsonpath_expression = jsonpath_rw.parse(self._json_path)
        match = jsonpath_expression.find(json_object)
        assert_that(match[0].value, self._matcher)

    def contains_json(self, json_object):
        jsonpath_expression = jsonpath_rw.parse(self._json_path)
        matched_values = [match.value for match in jsonpath_expression.find(json_object)]
        assert_that(matched_values, self._matcher)

    def not_presented(self, response):
        json = response.json()
        jsonpath_expression = jsonpath_rw.parse(self._json_path)
        matched_values = [match for match in jsonpath_expression.find(json)]
        assert_that(matched_values, equal_to([]))


body: Type[BodyFieldCondition] = BodyFieldCondition


class ConcreteValueCondition(Condition):

    def __init__(self, object_to_assert, matcher):
        super().__init__()
        self._object_to_assert = object_to_assert
        self._matcher = matcher

    def __repr__(self):
        return "Field {} is {}".format(self._object_to_assert, self._matcher)

    def match(self, response):
        assert_that(self._object_to_assert, self._matcher)


field: Type[ConcreteValueCondition] = ConcreteValueCondition
