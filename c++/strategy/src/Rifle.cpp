#include "Rifle.h"

using namespace std;

void Rifle::load() {
    _bullet_count = _magazine_size;
    cout << ".... magazine loaded." << endl;
}

void Rifle::shoot(TargetInterface* target) {
    if (_bullet_count) {
        _bullet_count--;
        cout << "BAM!" << endl;
        target->got_shoted();
    } else {
        cout << "Out of bullets." << endl;
        load();
    }
}