#include <string>
#include <vector>
#include <iostream>
#include <stdlib.h>

using namespace std;

struct Position {
    int x;
    int y;
};

vector<int> solution(vector<string> park, vector<string> routes) {
    vector<int> answer;
    vector<string>::iterator iter;
    
    int size_x = park.front().size();
    int size_y = park.size();
    Position pos;
    
    for (int i = 0; i < size_y; i++) {
        for (int j = 0; j < size_x; j++) {
            if (park[i].at(j) == 'S') {
                pos.x = j;
                pos.y = i;
                break;
            }
        }
    }
    
    for (iter = routes.begin(); iter != routes.end(); iter++) {
        char direction = (*iter).at(0);
        int distance = std::atoi(&(*iter).at(2));
        
        int x = pos.x;
        int y = pos.y;
        
        while (true) {
            distance--;
            switch (direction) {
                case 'E': x++; break;
                case 'W': x--; break;
                case 'N': y--; break;
                case 'S': y++; break;
                default: break;
            }
            if (y >= size_y || x >= size_x || y < 0 || x < 0) break;
            if (park[y][x] == 'X') break;
            
            if (distance == 0) {
                pos.x = x;
                pos.y = y;
                break;
            }
        }
    }
    
    answer.push_back(pos.y);
    answer.push_back(pos.x);
    
    return answer;
}