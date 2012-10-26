import unittest
from nose.tools import ok_, eq_, make_decorator, raises, set_trace, timed, with_setup, istest, nottest
from slimish_jinja.tokens import *


class TestTokens:

    def test_parse_text_contents(self):
        contents=[
            ('=foo','{{ foo }}'),
            ('=foo|filter','{{ foo|filter }}'),
            ('=foo | str','{{ foo }} | str'),
            ('=foo| filter','{{ foo| filter }}'),
            ('=foo|filter()','{{ foo|filter() }}'),
            ('=foo|filter(arg, kwarg="kw")','{{ foo|filter(arg, kwarg="kw") }}'),
            ('=foo.bar','{{ foo.bar }}'),
            ('=foo()','{{ foo() }}'),
            ('=foo().hoge()','{{ foo().hoge() }}'),
            ('=foo[]','{{ foo[] }}'),
            ('=foo[1][2]','{{ foo[1][2] }}'),
            ('foo =bar','foo {{ bar }}'),
            ('=foo bar','{{ foo }} bar'),
            ('=foo.method(arg, kwarg="kw")','{{ foo.method(arg, kwarg="kw") }}'),
            ('{{foo(kw=1)}} =bar','{{foo(kw=1)}} {{ bar }}'),
            ('=foo if bar', '{{ foo if bar }}'),
            ('=foo or bar', '{{ foo or bar }}'),
            ('{{ =foo }}','{{ =foo }}'),
            ('=foo[1][2]bar','{{ foo[1][2] }}bar'),
            ("=foo if page.title is defined else bar",'{{ foo if page.title is defined else bar }}'),
            ("='\%s' % var","{{ '\%s' % var }}"),
            ("=foo ~ var","{{ foo ~ var }}"),
            ("={'class': 'my_list', 'missing': none, 'id': 'list-\%d'|format(variable)}|xmlattr",
                "{{ {'class': 'my_list', 'missing': none, 'id': 'list-\%d'|format(variable)}|xmlattr }}"),
            ("={'foo':{bar:'2'}}", "{{ {'foo':{bar:'2'}} }}"),
            ("='active' if controller.action == 'index'", "{{ 'active' if controller.action == 'index' }}"),
        ]
        for content, ret in contents:
            parsed = parse_text_contents(content)
            eq_(parsed, ret, 'test "%s" error: parsed "%s" not equals "%s"' % (content, parsed, ret))
        

