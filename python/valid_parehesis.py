class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if s=='':
            return True
        if len(s)<2:
            return False
        pair_b={
            "[":"]",
            "(":")",
            "{":"]"
        }
        stk=[]
        for br in s:
            if br in pair_b:
                stk.append(br)
            else:
                if len(s)==0 or pair_b[stk.pop()]!=br:
                    return false
        if len(stk)>0:
            return False
        return True

        