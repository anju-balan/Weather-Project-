# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 10:03:53 2022

@author: Karthik Mohan
"""
import os
import webapp

import pytest

@pytest.fixture
def client():
    webapp.config.update({'TESTING': True})

    with webapp.test_client() as client:
        yield client