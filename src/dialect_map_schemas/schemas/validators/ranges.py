# -*- coding: utf-8 -*-

from marshmallow.validate import Range


arxiv_rev_range = Range(min=1, max=None)
jargon_abs_freq = Range(min=0, max=None)
jargon_rel_freq = Range(min=0, max=1)
paper_ref_count = Range(min=0, max=None)
