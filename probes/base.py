#!/usr/bin/env python3

class Probe:
    def __init__(self):
        self.name = None
        self.description = "Empty probe"
        self.uri = ""
        self.bcp47 = None # language this is for, in bcp47 format; * for all langs
        self.recommended_detector = None
    
    def probe(self, target):
        # attempt to exploit the target, return list of results
        return []