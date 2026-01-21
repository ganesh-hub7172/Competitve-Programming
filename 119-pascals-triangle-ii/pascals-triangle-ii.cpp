#include <vector>
using namespace std;

class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> row;
        row.push_back(1); // First element is always 1

        long long val = 1; // Use long long to avoid overflow
        for (int i = 1; i <= rowIndex; i++) {
            val = val * (rowIndex - i + 1) / i;
            row.push_back((int)val); // Convert back to int
        }

        return row;
    }
};
