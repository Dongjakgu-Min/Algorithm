#include <string>
#include <vector>
#include <map>

using namespace std;

vector<int> solution(vector<string> name, vector<int> yearning, vector<vector<string>> photo) {
    vector<int> answer;
    map<string, int> record;
    vector<string>::iterator iter;
    vector<vector<string>>::iterator vector_iter;
    vector<int>::iterator yearning_itor = yearning.begin();
    
    for (iter = name.begin(); iter != name.end(); iter++) {
        record.insert({ *iter, *yearning_itor });
        yearning_itor++;
    }
    
    for (vector_iter = photo.begin(); vector_iter != photo.end(); vector_iter++) {
        int value = 0;
        for (iter = (*vector_iter).begin(); iter != (*vector_iter).end(); iter++) {
            if (record.find(*iter) != record.end()) {
                value += record.find(*iter)->second;
            }
        }
        answer.push_back(value);
    }
    
    return answer;
}