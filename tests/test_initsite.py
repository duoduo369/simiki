#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path
import unittest
import shutil

from simiki.initsite import InitSite
from simiki.utils import check_path_exists


class TestInitSite(unittest.TestCase):

    def setUp(self):
        BASE_DIR = os.path.join(os.path.dirname(__file__), '..')
        self.config_file = os.path.join(BASE_DIR, "simiki", "conf_templates",
                                        "_config.yml.in")
        self.target_path = os.path.join(BASE_DIR, "tests", "_build")
        if os.path.exists(self.target_path):
            shutil.rmtree(self.target_path)
        os.mkdir(self.target_path)
        self.files = [
            "_config.yml",
            "fabfile.py",
            "content/intro/gettingstarted.md",
        ]
        self.dirs = [
            "content",
            "output",
            "themes",
            "themes/simple"
        ]

    def test_target_exist(self):
        """ test InitSite target path exist
        """

        i = InitSite(self.config_file, self.target_path)
        i.init_site()

        for f in self.files:
            self.assertTrue(os.path.isfile(os.path.join(self.target_path, f)))

        for d in self.dirs:
            self.assertTrue(os.path.isdir(os.path.join(self.target_path, d)))

    def test_target_invalid(self):
        """ test InitSite target path invalid, raise OSError
        """

        self.files = ["_config.yml", "fabfile.py"]
        self.dirs = ["content", "output", "themes"]
        target_error = "/foo/bar/why/not"
        i = InitSite(self.config_file, target_error)
        with self.assertRaises(OSError):
            i.init_site()

    def tearDown(self):
        shutil.rmtree(self.target_path)

if __name__ == "__main__":
    unittest.main()
