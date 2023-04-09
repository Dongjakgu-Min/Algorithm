#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

struct Rent {
    int start_time;
    int end_time;
};

bool compare(Rent &a, Rent &b) {
    return a.start_time < b.start_time;
}

int solution(vector<vector<string>> book_time) {
    int answer = 0;
    vector<Rent> schedule;
    vector<int> room;
    
    for (auto iter = book_time.begin(); iter != book_time.end(); iter++) {
        Rent rent;
        rent.start_time = stoi((*iter)[0].substr(0, 2)) * 60 + stoi((*iter)[0].substr(3, 2));
        rent.end_time = stoi((*iter)[1].substr(0, 2)) * 60 + stoi((*iter)[1].substr(3, 2));
        schedule.push_back(rent);
    }
    
    sort(schedule.begin(), schedule.end(), compare);
    
    room.push_back(schedule.front().end_time);
    
    for (auto iter = schedule.begin() + 1; iter != schedule.end(); iter++) {
        auto room_iter = room.begin();
        
        while (room_iter != room.end()) {
            if ((*room_iter) + 10 <= iter->start_time) {
                (*room_iter) = iter->end_time;
                break;
            } 
            room_iter++;
        }
        
        if (room_iter == room.end()) {
            room.push_back(iter->end_time);
        }
    }
    
    return room.size();
}