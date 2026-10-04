class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m = {}
        for i in range(numCourses):
            m[i] = []
        for p in prerequisites:
            m[p[0]].append(p[1])
        
        s = set()
        def dfs(course):
            if len(m[course]) == 0:
                return True
            if course in s:
                return False
            else:
                s.add(course)
            
            for c in m[course]:
                if not dfs(c):
                    dfs(c)
                    return False
            s.remove(course)
            m[course] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            
