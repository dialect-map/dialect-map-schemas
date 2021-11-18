# -*- coding: utf-8 -*-

from marshmallow.validate import Regexp


group_id_regex = Regexp("^group-\\d+$")
jargon_id_regex = Regexp("^group-\\d+-jargon-\\d+$")
jargon_term_regex = Regexp("^[a-z]+([ \\-][a-z]+)*$")
