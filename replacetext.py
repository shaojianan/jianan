#!/usr/bin/env python

class StringConvert():

    def string_convert(self):
        str = input("Enter your url")
        str = str.replace("/Volumes", "\\\\172.16.10.19").replace("/", "\\")
        print "result : ", str

sc = StringConvert()
StringConvert.string_convert(sc)