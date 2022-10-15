#include<iostream>
#include<stdlib.h>
#include<windows.h>
#include<thread>
using namespace std;

class Time
{
private:
    int hours;
    int minutes;
    int seconds;

public:
    void askTime(int& ohours, int& ominutes, int& clhours)
    {
        cout << "Enter the hour that you want your window open: " << endl;
        cin >> ohours;
        cout << "Enter the minute that you want your window open: " << endl;
        cin >> ominutes;
        cout << "Enter after how many hour that you want your window close: " << endl;
        cin >> clhours;

    }

    void Display(int ohours, int ominutes, int clhours, int hours, int minutes, int seconds)
    {
        if (ohours == hours && ominutes == minutes && seconds == 1)
            cout << "Window is open !!!!!!!!!!!!!!";
        else if ((ohours + clhours == hours && ominutes == minutes && seconds == 1))
            cout << "Window is closed !!!!!!!!!!!!!!";
        else
            return;
    }

    int timer(int ohours, int ominutes, int clhours)
    {
        int hours = 0;
        int minutes = 0;
        int seconds = 0;

        while (true) {
            system("cls");
            cout << hours << " : " << minutes << " : " << seconds << endl;
            seconds++;
            if (seconds == 60) {
                minutes++;
                seconds = 0;
                if (minutes == 60) {
                    hours++;
                    minutes = 0;
                    if (hours == 24) {
                        hours = 0;
                    }
                }
            }
            Display(ohours, ominutes, clhours, hours, minutes, seconds);
            Sleep(1000);
        }
    }
};


int main()
{
    Time T;
    int ohours, ominutes, clhours;
    T.askTime(ohours, ominutes, clhours);
    T.timer(ohours,ominutes,clhours);

    return 0;
}
