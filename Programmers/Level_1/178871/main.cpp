#include <string>
#include <vector>
#include <map>
#include <iostream>

using namespace std;

vector<string> solution(vector<string> players, vector<string> callings) {
    vector<string> answer;
    map<string, int> record;
    
    for (int i = 0; i < players.size(); i++)
        record.insert({ players[i], i });
    
    for (auto iter = callings.begin(); iter != callings.end(); iter++) {
        string temp;
        auto elem = record.find(*iter);
        
        temp = players[elem->second - 1];
        players[elem->second - 1] = players[elem->second];
        players[elem->second] = temp;
        
        record[*iter]--;
        record[players[elem->second + 1]]++;
    }
    
    return players;
}