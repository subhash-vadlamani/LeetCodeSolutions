class Solution {
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        map<string, vector<string>> adj;
        vector<string> res;

        for (const auto& ticket : tickets) {
            const string& src = ticket[0];
            const string& dst = ticket[1];
            adj[src].push_back(dst);
        }

        for (auto& entry : adj) {
            sort(entry.second.begin(), entry.second.end());
        }

        DFS(adj, res, "JFK");
        reverse(res.begin(), res.end());

        if (res.size() != tickets.size() + 1) {
            return vector<string>();
        }

        return res;
    }

private:
    void DFS(map<string, vector<string>>& adj, vector<string>& result, const string& src) {
        if (adj.find(src) != adj.end()) { // if src in adj
            while (!adj[src].empty()) {
                string dest = adj[src].front();
                adj[src].erase(adj[src].begin());
                DFS(adj, result, dest);
            }
        }
        result.push_back(src);
    }
};