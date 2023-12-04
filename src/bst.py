#!/usr/bin/env python3

import bt
import sys
import logging

log = logging.getLogger(__name__)

class BST(bt.BT):
    def __init__(self, value=None):
        '''
        Initializes an empty tree if `value` is None, else a root with the
        specified `value` and two empty children.
        '''
        self.set_value(value)
        if not self.is_empty():
            self.cons(BST(), BST())

    def is_member(self, v):
        '''
        Returns true if the value `v` is a member of the tree.
        '''
        result = False
        if v == self.get_value():
            return True
        if self.get_lc():
            result = result or self.get_lc().is_member(v)
        if self.get_rc():
            result = result or self.get_rc().is_member(v)
        return result

    def size(self):
        '''
        Returns the number of nodes in the tree.
        '''
        if self.is_empty():
            return 0
        return 1 + self.get_lc().size() + self.get_rc().size()

    def height(self):
        '''
        Returns the height of the tree.
        '''
        if self.is_empty():
            return 0

        return 1 + max(self.get_lc().height(), self.get_rc().height())

    def preorder(self):
        '''
        Returns a list of all members in preorder.
        '''
        if self.is_empty():
            return []
        return [self.get_value()] + self.get_lc().preorder() + self.get_rc().preorder()

    def inorder(self):
        '''
        Returns a list of all members in inorder.
        '''
        if self.is_empty():
            return []
        return self.get_lc().inorder() + [self.get_value()] + self.get_rc().inorder()

    def postorder(self):
        '''
        Returns a list of all members in postorder.
        '''
        if self.is_empty():
            return []
        return self.get_lc().postorder() + self.get_rc().postorder() + [self.get_value()]

    def bfs_order_star(self):
        '''
        Returns a list of all members in breadth-first search* order, which
        means that empty nodes are denoted by "stars" (here the value None).

        For example, consider the following tree `t`:
                    10
              5           15
           *     *     *     20

        The output of t.bfs_order_star() should be:
        [ 10, 5, 15, None, None, None, 20 ]
        '''
        result = []
        if not self.is_empty():
            size = (2**self.height()) -1
            q = [self]
            i = 0
            while q and i < size:
                n = q.pop(0)
                if n is not None:
                    result.append(n.get_value())
                    q.append(n.get_lc())
                    q.append(n.get_rc())
                else:
                    result.append(None)
                    q.append(None)
                    q.append(None)
                i += 1
        return result

    def add(self, v):
        '''
        Adds the value `v` and returns the new (updated) tree.  If `v` is
        already a member, the same tree is returned without any modification.
        '''
        if self.is_empty():
            self.__init__(value=v)
            return self
        if v < self.get_value():
            return self.cons(self.get_lc().add(v), self.get_rc())
        if v > self.get_value():
            return self.cons(self.get_lc(), self.get_rc().add(v))
        return self

    def delete(self, v):
        '''
        Removes the value `v` from the tree and returns the new (updated) tree.
        If `v` is a non-member, the same tree is returned without modification.
        '''
        if self.is_empty() or not self.is_member(v):
            return self
        elif self.get_value() == v:
            self.set_value(self.detach())
        elif self.get_value() < v:
            self.get_rc().delete(v)
        else:
            self.get_lc().delete(v)

        return self

    def detach(self):
        if self.get_rc().is_empty() and self.get_lc().is_empty():
            return None

        elif not self.get_lc().is_empty() and not self.get_rc().is_empty():
            if self.get_lc().height() < self.get_rc().height():
                return self.get_rc().get_rc_lm()
            else:
                return self.get_lc().get_lc_rm()

        elif not self.get_rc().is_empty() and self.get_lc().is_empty():
            return self.get_rc().get_rc_lm()
        else:
            return self.get_lc().get_lc_rm()

    def get_rc_lm(self):
        if self.get_lc().is_empty():
            temp = self.get_value()
            if self.get_rc().is_empty():
                self.set_value(None)
            else:
                self.set_value(self.get_rc().get_value())
                self.set_rc(self.get_rc().get_rc())
            return temp
        else:
            return self.get_lc().get_rc_lm()

    def get_lc_rm(self):
        if self.get_rc().is_empty():
            temp = self.get_value()
            if self.get_lc().is_empty():
                self.set_value(None)
            else:
                self.set_value(self.get_lc().get_value())
                self.set_lc(self.get_lc().get_lc())
            return temp
        else:
            return self.get_rc().get_lc_rm()
    

if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
