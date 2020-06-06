# -*- coding: utf-8 -*-
"""
Created on Tue May 26 17:57:47 2020

@author: Christopher Cheng
"""

class Queue (object):
    def __init__ (self):
        self.queue = []
    def get_queue_elements (self):
        return self.queue.copy()
    def add_one (self,item):
        self.queue.append(item)
    def add_many(self,item,n):
        for i in range(n):
            self.queue.append(item)
    def remove_one (self):
        self.queue.pop(0)
    def remove_many (self,n):
        for i in range(n):
            self.queue.pop(0)
    def size(self):
        return len(self.queue)
    def prettyprint(self):
        for thing in self.queue[::-1]:
            print("|_", thing,"_|")
            
pancakes = Queue()
pancakes.add_one("blueberry")
pancakes.add_many("chocolate", 4)
pancakes.add_many("vanilla",2)
pancakes.add_one("blueberry")
print(pancakes.size())
pancakes.remove_one()
print(pancakes.size())
pancakes.remove_many(2)
pancakes.prettyprint()