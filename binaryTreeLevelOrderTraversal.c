/** 
* Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
       vector<vector<int>> levelOrder(TreeNode* root) {
        queue<TreeNode*> graf;
        vector<vector<int>> resposta;

        if (root) {
            graf.push(root);
        }

        while (!graf.empty()) {
            int nivel = graf.size();

            vector<int> nivel_list;
            while (nivel > 0) {
                TreeNode* no = graf.front();
                graf.pop();

                nivel_list.push_back(no->val);

                if (no->left) {
                    graf.push(no->left);
                }

                if (no->right) {
                    graf.push(no->right);
                }
                nivel--;
            }

            resposta.push_back(nivel_list);
        }
        return resposta;
    }
};
