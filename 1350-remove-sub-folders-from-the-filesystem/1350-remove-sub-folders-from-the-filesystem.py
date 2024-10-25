from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()  # Sort lexicographically
        answer = []
        
        for f in folder:
            # Check if `f` is not a subfolder of the last folder added to `answer`
            if not answer or not f.startswith(answer[-1] + '/'):
                answer.append(f)
        
        return answer