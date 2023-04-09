#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <stack>

using namespace std;

struct Plan {
    string lecture;
    int start_time;
    int remain;
};

bool compare(Plan &a, Plan &b) {
    return a.start_time > b.start_time;
}

vector<string> solution(vector<vector<string>> plans) {
    vector<string> answer;
    vector<Plan> jobs;
    stack<Plan> tasks;
    
    for (auto iter = plans.begin(); iter != plans.end(); iter++) {
        Plan plan;
        
        plan.lecture = (*iter)[0];
        plan.start_time = stoi((*iter)[1].substr(0, 2)) * 60 + stoi((*iter)[1].substr(3, 2));
        plan.remain = stoi((*iter)[2]);
        
        jobs.push_back(plan);
    }
    
    sort(jobs.begin(), jobs.end(), compare);
    
    while (true) {
        Plan now = jobs.back();
        jobs.pop_back();
        
        if (jobs.empty()) {
            answer.push_back(now.lecture);
            break;
        }
        else {
            Plan next = jobs.back();
            if (next.start_time - now.start_time == now.remain) {
                answer.push_back(now.lecture);
            }
            else if (next.start_time - now.start_time > now.remain) {
                answer.push_back(now.lecture);
                int remain_time = next.start_time - now.start_time - now.remain;
                while (!tasks.empty() && remain_time) {
                    Plan prev = tasks.top();
                    if (remain_time >= prev.remain) {
                        answer.push_back(prev.lecture);
                        remain_time -= prev.remain;
                        tasks.pop();
                    } else {  
                        tasks.pop();
                        prev.remain -= remain_time;
                        tasks.push(prev);
                        break;
                    }
                }
            }
            else {
                now.remain -= next.start_time - now.start_time;
                tasks.push(now);
            }
        }
    }
    
    while (!tasks.empty()) {
        answer.push_back(tasks.top().lecture);
        tasks.pop();
    }
    
    return answer;
}