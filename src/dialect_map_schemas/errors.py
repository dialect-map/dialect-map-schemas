# -*- coding: utf-8 -*-

from marshmallow.exceptions import MarshmallowError


### NOTE:
### This custom tuple of errors contains all the possible exceptions
### that can be raised during the schemas serialization / deserialization
SchemaError = (AssertionError, MarshmallowError)
