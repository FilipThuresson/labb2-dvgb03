#!/usr/bin/env python3

import sys
import bst
import logging

log = logging.getLogger(__name__)

class AVL(bst.BST):
    def __init__(self, value=None):
        '''
        Initializes an empty tree if `value` is None, else a root with the
        specified `value` and two empty children.
        '''
        self.set_value(value)
        if not self.is_empty():
            self.cons(AVL(), AVL())

    def add(self, v):
        '''
        Example which shows how to override and call parent methods.  You
        may remove this function and overide something else if you'd like.
        '''
        log.debug("calling bst.BST.add() explicitly from child")

        super().add(v)
        return self.balance()

    def delete(self, v):
        super().delete(v)
        return self.balance()

    def balance_factor(self):
        right = 0 if self.get_rc().height() is None else self.get_rc().height()
        left = 0 if self.get_lc().height() is None else self.get_lc().height()

        return left - right

    def balance(self):
        '''
        AVL-balances around the node rooted at `self`.  In other words, this
        method applies one of the following if necessary: slr, srr, dlr, drr.
        '''

        if self.is_empty():
            return self

            # Check the balance factor
        balance_factor = self.balance_factor()

        if abs(balance_factor) > 1:
            if balance_factor > 0:  # Left heavy
                if self.get_lc() and self.get_lc().balance_factor() >= 0:
                    return self.srr()
                else:
                    return self.drr()
            else:  # Right heavy
                if self.get_rc() and self.get_rc().balance_factor() > 0:
                    return self.dlr()
                else:
                    return self.slr()
        else:
            return self
    def slr(self):
        '''
        Performs a single-left rotate around the node rooted at `self`.
        '''
        node = self.get_rc()
        self.set_rc(node.get_lc())
        node.set_lc(self)

        return node

    def srr(self):
        '''
        Performs a single-right rotate around the node rooted at `self`.
        '''
        node = self.get_lc()
        self.set_lc(node.get_rc())
        node.set_rc(self)
        return node

    def dlr(self):
        '''
        Performs a double-left rotate around the node rooted at `self`.
        '''
        self.set_rc(self.get_rc().srr())
        return self.slr()

    def drr(self):
        '''
        Performs a double-right rotate around the node rooted at `self`.
        '''
        self.set_lc((self.get_lc().slr()))
        return self.srr()

if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
