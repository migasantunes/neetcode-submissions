class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = defaultdict(list)

        for course, prereq in prerequisites:
            pre[course].append(prereq)
            
        seen = set()
        
        def canTake(c):
            if c in seen:
                return False
            
            if c in pre and pre[c]:
                seen.add(c)
                
                for prereq in pre[c]:
                    if not canTake(prereq):
                        return False
                
                seen.remove(c)
                pre[c] = []            
            
            return True
        
        for course in pre:            
            if not canTake(course):
                return False
        
        return True