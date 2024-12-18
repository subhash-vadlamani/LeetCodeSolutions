class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
      int n=numCourses;
      vector<int> ans;
      
      unordered_map<int,vector<int>> adj;
      vector<int> indegre(n,0);
      
      for(auto& preq : prerequisites){
        adj[preq[1]].push_back(preq[0]);
        indegre[preq[0]]++;
      }
      
      queue<int> q;
      int cnt=0;
      
      for(int i=0;i<n;i++){
        if(indegre[i]==0)
          q.push(i);
      }
      
      while(!q.empty()){
        int cur=q.front();
        q.pop();
        ans.push_back(cur);
        cnt++;
        
        for(auto& neigh: adj[cur]){
          indegre[neigh]--;
          if(indegre[neigh]==0) q.push(neigh);
        }
      }
      
      if(cnt!=n) return vector<int>();
    	
      return ans;
        
    }
};