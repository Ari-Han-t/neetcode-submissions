class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c=0
        for d in details:
            r=str(d)
            if int(r[11:13:1])>60:
                c+=1
        return c