# #!/usr/bin/env python
# -*- coding: utf-8 -*-
# <sure - assertion toolbox>
# Copyright (C) <2010>  Gabriel Falcão <gabriel@nacaolivre.org>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

import sure
from sure import that
from threading import local
from nose.tools import assert_equals, assert_raises

def test_setup_with_context():
    "sure.with_context() runs setup before the function itself"

    def setup(context):
        context.name = "John Resig"

    @sure.that_with_context(setup)
    def john_is_within_context(context):
        assert isinstance(context, local)
        assert hasattr(context, "name")

    john_is_within_context()
    assert_equals(
        john_is_within_context.__name__,
        'test_john_is_within_context'
    )

def test_setup_with_context_optional_context():
    "sure.that_with_context() handle optional context"

    def setup(context):
        context.name = "John Resig"

    @sure.that_with_context(setup)
    def it_passes():
        assert True

    it_passes() #?
    assert_equals(
        it_passes.__name__,
        'test_it_passes'
    )

def test_teardown_with_context():
    "sure.with_context() runs teardown before the function itself"

    class something:
        pass

    def setup(context):
        something.modified = True

    def teardown(context):
        del something.modified

    @sure.that_with_context(setup, teardown)
    def something_was_modified(context):
        assert hasattr(something, "modified")
        assert something.modified

    something_was_modified()
    assert not hasattr(something, "modified")

def test_that_is_a():
    "sure.that() is_a(object)"

    something = "something"

    assert that(something).is_a(str)
    assert isinstance(something, str)

def test_that_equals():
    "sure.that() equals(object)"

    something = "something"

    assert that(something).equals(something)
    assert something == something

def test_that_differs():
    "sure.that() differs(object)"

    something = "something"

    assert that(something).differs("23123%FYTUGIHOfdf")
    assert something != "23123%FYTUGIHOfdf"

def test_that_has():
    "sure.that() has(object)"

    class Class:
        name = "some class"
    Object = Class()
    dictionary = {
        'name': 'John'
    }
    name = "john"

    assert hasattr(Class, 'name')
    assert that(Class).has("name")
    assert that(Class).like("name")
    assert "name" in sure.that(Class)

    assert hasattr(Object, 'name')
    assert that(Object).has("name")
    assert that(Object).like("name")
    assert "name" in sure.that(Object)

    assert dictionary.has_key('name')
    assert that(dictionary).has("name")
    assert that(dictionary).like("name")
    assert "name" in sure.that(dictionary)

    assert that(name).has("john")
    assert that(name).like("john")
    assert "john" in sure.that(name)
    assert that(name).has("hn")
    assert that(name).like("hn")
    assert "hn" in sure.that(name)
    assert that(name).has("jo")
    assert that(name).like("jo")
    assert "jo" in sure.that(name)

def test_that_len_is():
    "sure.that() len_is(number)"

    lst = range(1000)

    assert that(lst).len_is(1000)
    assert len(lst) == 1000
    assert that(lst).len_is(lst)

def test_that_len_greater_than():
    "sure.that() len_greater_than(number)"

    lst = range(1000)
    lst2 = range(100)

    assert that(lst).len_greater_than(100)
    assert len(lst) == 1000
    assert that(lst).len_greater_than(lst2)

def test_that_len_greater_than_should_raise_assertion_error():
    "sure.that() len_greater_than(number) raise AssertionError"

    lst = range(1000)
    try:
        that(lst).len_greater_than(1000)
    except AssertionError, e:
        assert_equals(str(e), 'the length of the list should be greater then %d, but is %d' % (1000, 1000))

def test_that_len_greater_than_or_equals():
    "sure.that() len_greater_than_or_equals(number)"

    lst = range(1000)
    lst2 = range(100)

    assert that(lst).len_greater_than_or_equals(100)
    assert that(lst).len_greater_than_or_equals(1000)
    assert len(lst) == 1000
    assert that(lst).len_greater_than_or_equals(lst2)
    assert that(lst).len_greater_than_or_equals(lst)

def test_that_len_greater_than_or_equals_should_raise_assertion_error():
    "sure.that() len_greater_than_or_equals(number) raise AssertionError"

    lst = range(1000)
    try:
        that(lst).len_greater_than_or_equals(1001)
    except AssertionError, e:
        assert_equals(str(e), 'the length of %r should be greater then or equals %d, but is %d' % (lst, 1001, 1000))

def test_that_len_lower_than():
    "sure.that() len_lower_than(number)"

    lst = range(100)
    lst2 = range(1000)

    assert that(lst).len_lower_than(101)
    assert len(lst) == 100
    assert that(lst).len_lower_than(lst2)

def test_that_len_lower_than_should_raise_assertion_error():
    "sure.that() len_lower_than(number) raise AssertionError"

    lst = range(1000)
    try:
        that(lst).len_lower_than(1000)
    except AssertionError, e:
        assert_equals(str(e), 'the length of %r should be lower then %d, but is %d' % (lst, 1000, 1000))

def test_that_len_lower_than_or_equals():
    "sure.that() len_lower_than_or_equals(number)"

    lst = range(1000)
    lst2 = range(1001)

    assert that(lst).len_lower_than_or_equals(1001)
    assert that(lst).len_lower_than_or_equals(1000)
    assert len(lst) == 1000
    assert that(lst).len_lower_than_or_equals(lst2)
    assert that(lst).len_lower_than_or_equals(lst)

def test_that_len_lower_than_or_equals_should_raise_assertion_error():
    "sure.that() len_lower_than_or_equals(number) raise AssertionError"

    lst = range(1000)
    try:
        that(lst).len_lower_than_or_equals(100)
    except AssertionError, e:
        assert_equals(str(e), 'the length of %r should be lower then or equals %d, but is %d' % (lst, 100, 1000))

def test_that_checking_all_atributes():
    "sure.that(iterable).the_attribute('name').equals('value')"
    class shape(object):
        def __init__(self, name):
            self.kind = 'geometrical form'
            self.name = name

    shapes = [
        shape('circle'),
        shape('square'),
        shape('rectangle'),
        shape('triangle')
    ]

    assert that(shapes).the_attribute("kind").equals('geometrical form')

def test_that_checking_all_atributes_of_range():
    "sure.that(iterable, within_range=(1, 2)).the_attribute('name').equals('value')"
    class shape(object):
        def __init__(self, name):
            self.kind = 'geometrical form'
            self.name = name
        def __repr__(self):
            return '<%s:%s>' % (self.kind, self.name)

    shapes = [
        shape('circle'),
        shape('square'),
        shape('square'),
        shape('triangle')
    ]

    assert shapes[0].name != 'square'
    assert shapes[3].name != 'square'

    assert shapes[1].name == 'square'
    assert shapes[2].name == 'square'

    assert that(shapes, within_range=(1, 2)).the_attribute("name").equals('square')

def test_that_checking_all_elements():
    "sure.that(iterable).every_one_is('value')"
    shapes = [
        'cube',
        'ball',
        'ball',
        'piramid'
    ]

    assert shapes[0] != 'ball'
    assert shapes[3] != 'ball'

    assert shapes[1] == 'ball'
    assert shapes[2] == 'ball'

    assert that(shapes, within_range=(1, 2)).every_one_is('ball')

def test_that_checking_each_matches():
    "sure.that(iterable).in_each('').equals('value')"
    class animal(object):
        def __init__(self, kind):
            self.attributes = {
                'class': 'mammal',
                'kind': kind,
            }

    animals = [
        animal('dog'),
        animal('cat'),
        animal('cow'),
        animal('cow'),
        animal('cow'),
    ]

    assert animals[0].attributes['kind'] != 'cow'
    assert animals[1].attributes['kind'] != 'cow'

    assert animals[2].attributes['kind'] == 'cow'
    assert animals[3].attributes['kind'] == 'cow'
    assert animals[4].attributes['kind'] == 'cow'

    assert animals[0].attributes['class'] == 'mammal'
    assert animals[1].attributes['class'] == 'mammal'
    assert animals[2].attributes['class'] == 'mammal'
    assert animals[3].attributes['class'] == 'mammal'
    assert animals[4].attributes['class'] == 'mammal'

    assert that(animals).in_each("attributes['class']").matches('mammal')
    assert that(animals).in_each("attributes['class']").matches(['mammal','mammal','mammal','mammal','mammal'])

    assert that(animals).in_each("attributes['kind']").matches(['dog','cat','cow','cow','cow'])

    try:
        assert that(animals).in_each("attributes['kind']").matches(['dog'])
        assert False, 'should not reach here'
    except AssertionError, e:
        assert that(unicode(e)).equals(
            '%r has 5 items, but the matching list has 1: %r' % (
                ['dog','cat','cow','cow','cow'], ['dog']
            )
        )

def test_that_raises():
    "sure.that(callable, with_args=[arg1], and_kwargs={'arg2': 'value'}).raises(SomeException)"

    called = False
    global called
    def function(arg1=None, arg2=None):
        global called
        called = True
        if arg1 == 1 and arg2 == 2:
            raise RuntimeError('yeah, it failed')

        return "OK"

    try:
        function(1, 2)
        assert False, 'should not reach here'

    except RuntimeError, e:
        assert unicode(e) == 'yeah, it failed'

    except Exception:
        assert False, 'should not reach here'

    finally:
        assert called
        called = False

    assert_raises(RuntimeError, function, 1, 2)

    called = False
    assert_equals(function(3, 5), 'OK')
    assert called

    called = False
    assert that(function, with_args=[1], and_kwargs={'arg2': 2}).raises(RuntimeError)
    assert called

    called = False
    assert that(function, with_args=[1], and_kwargs={'arg2': 2}).raises(RuntimeError, 'yeah, it failed')
    assert called

    called = False
    assert that(function, with_args=[1], and_kwargs={'arg2': 2}).raises('yeah, it failed')
    assert called

    called = False
    assert that(function, with_kwargs={'arg1': 1, 'arg2': 2}).raises(RuntimeError)
    assert called

    called = False
    assert that(function, with_kwargs={'arg1': 1, 'arg2': 2}).raises(RuntimeError, 'yeah, it failed')
    assert called

    called = False
    assert that(function, with_kwargs={'arg1': 1, 'arg2': 2}).raises('yeah, it failed')
    assert called

    called = False
    assert that(function, with_kwargs={'arg1': 1, 'arg2': 2}).raises(r'it fail')
    assert called

    called = False
    assert that(function, with_kwargs={'arg1': 1, 'arg2': 2}).raises(RuntimeError, r'it fail')
    assert called

def test_that_looks_like():
    "sure.that('String\\n with BREAKLINE').looks_like('string with breakline')"
    assert that('String\n with BREAKLINE').looks_like('string with breakline')

def test_that_raises_with_args():
    "sure.that(callable, with_args=['foo']).raises(FooError)"

    class FooError(Exception):
        pass

    def my_function(string):
        if string == 'foo':
            raise FooError('OOps')

    assert that(my_function, with_args=['foo']).raises(FooError, 'OOps')

def test_that_contains_string():
    "sure.that('foobar').contains('foo')"

    assert 'foo' in 'foobar'
    assert that('foobar').contains('foo')

def test_that_contains_none():
    "sure.that('foobar').contains(None)"

    try:
        assert that('foobar').contains(None)
        assert False, 'should not reach here'
    except Exception, e:
        assert_equals(unicode(e), u'None should be a string')

def test_that_none_contains_string():
    "sure.that(None).contains('bungalow')"

    try:
        assert that(None).contains('bungalow')
        assert False, 'should not reach here'
    except Exception, e:
        assert_equals(unicode(e), u'None is not a string, so is is impossible to check if "bungalow" is there')

def test_that_some_iterable_is_empty():
    "sure.that(some_iterable).is_empty and sure.that(something).are_empty"

    assert that([]).is_empty
    assert that([]).are_empty

    assert that(tuple()).is_empty
    assert that({}).are_empty

    def fail_single():
        assert that((1,)).is_empty

    assert that(fail_single).raises('(1,) is not empty, it has 1 item')

    def fail_plural():
        assert that((1, 2)).is_empty

    assert that(fail_plural).raises('(1, 2) is not empty, it has 2 items')

def test_that_something_is_empty_raises():
    "sure.that(something_not_iterable).is_empty and sure.that(something_not_iterable).are_empty raises"


    obj = object()
    def fail():
        assert that(obj).is_empty
        assert False, 'should not reach here'

    assert that(fail).raises('%r is not iterable' % obj)

def test_that_something_iterable_matches_another():
    "sure.that(something_iterable).matches(another_iterable)"

    KlassOne = type('KlassOne', (object,), {})
    KlassTwo = type('KlassTwo', (object,), {})
    one = [
        ("/1", KlassOne),
        ("/2", KlassTwo),
    ]

    two = [
        ("/1", KlassOne),
        ("/2", KlassTwo),
    ]

    assert that(one).matches(two)
    assert that(one).equals(two)

    def fail_1():
        assert that(range(1)).matches(xrange(2))

    def fail_2():
        assert that(xrange(1)).equals(range(2))

    assert that(fail_1).raises('[0] has 1 item, but xrange(2) has 2 items')
    assert that(fail_2).raises('xrange(1) has 1 item, but [0, 1] has 2 items')

def test_within_pass():
    "within(five=miliseconds) will pass"
    from sure import within, miliseconds

    within(five=miliseconds)(lambda *a: None)()

def test_within_fail():
    "within(five=miliseconds) will fail"
    import time
    from sure import within, miliseconds

    def sleepy():
        time.sleep(0.7)

    failed = False
    try:
        within(five=miliseconds)(sleepy)()
    except AssertionError, e:
        failed = True
        assert_equals('sleepy did not run within five miliseconds', str(e))

    assert failed, 'within(five=miliseconds)(sleepy) did not fail'


def test_word_to_number():
    assert_equals(sure.word_to_number('one'),      1)
    assert_equals(sure.word_to_number('two'),      2)
    assert_equals(sure.word_to_number('three'),    3)
    assert_equals(sure.word_to_number('four'),     4)
    assert_equals(sure.word_to_number('five'),     5)
    assert_equals(sure.word_to_number('six'),      6)
    assert_equals(sure.word_to_number('seven'),    7)
    assert_equals(sure.word_to_number('eight'),    8)
    assert_equals(sure.word_to_number('nine'),     9)
    assert_equals(sure.word_to_number('ten'),     10)
    assert_equals(sure.word_to_number('eleven'),  11)
    assert_equals(sure.word_to_number('twelve'),  12)


def test_word_to_number_fail():
    failed = False
    try:
        sure.word_to_number('twenty')
    except AssertionError, e:
        failed = True
        assert_equals(unicode(e), 'sure supports only literal numbers from one ' \
                      'to twelve, you tried the word "twenty"')

    assert failed, 'should raise assertion error'

def test_microsecond_unit():
    "testing microseconds convertion"
    cfrom, cto = sure.UNITS[sure.microsecond]

    assert_equals(cfrom(1), 100000)
    assert_equals(cto(1), 1)

    cfrom, cto = sure.UNITS[sure.microseconds]

    assert_equals(cfrom(1), 100000)
    assert_equals(cto(1), 1)

def test_milisecond_unit():
    "testing miliseconds convertion"
    cfrom, cto = sure.UNITS[sure.milisecond]

    assert_equals(cfrom(1), 1000)
    assert_equals(cto(100), 1)

    cfrom, cto = sure.UNITS[sure.miliseconds]

    assert_equals(cfrom(1), 1000)
    assert_equals(cto(100), 1)

def test_second_unit():
    "testing seconds convertion"
    cfrom, cto = sure.UNITS[sure.second]

    assert_equals(cfrom(1), 1)
    assert_equals(cto(100000), 1)

    cfrom, cto = sure.UNITS[sure.seconds]

    assert_equals(cfrom(1), 1)
    assert_equals(cto(100000), 1)

def test_minute_unit():
    "testing minutes convertion"
    cfrom, cto = sure.UNITS[sure.minute]

    assert_equals(cfrom(60), 1)
    assert_equals(cto(1), 6000000)

    cfrom, cto = sure.UNITS[sure.minutes]

    assert_equals(cfrom(60), 1)
    assert_equals(cto(1), 6000000)

def test_within_pass_utc():
    "within(five=miliseconds) gives utc parameter"
    from sure import within, miliseconds
    from datetime import datetime
    def assert_utc(utc):
        assert isinstance(utc, datetime)

    within(five=miliseconds)(assert_utc)()

def test_that_is_a_matcher_should_absorb_callables_to_be_used_as_matcher():
    u"that.is_a_matcher should absorb callables to be used as matcher"
    @that.is_a_matcher
    def is_truthful(what):
        assert bool(what), '{0} is so untrue'.format(what)
        return 'foobar'

    assert that('friend').is_truthful()
    assert_equals(that('friend').is_truthful(), 'foobar')

