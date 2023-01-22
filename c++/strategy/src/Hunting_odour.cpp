#include "Hunting_odour.h"

using namespace std;

void HuntingOdour::use(TargetInterface* target) {
    if (_uses) {
        _uses--;
        target->modify_survivability(_target_modifier);
    } else
        cout << "Bottle is empty." << endl;
}