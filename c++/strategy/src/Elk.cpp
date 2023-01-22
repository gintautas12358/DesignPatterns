#include "Elk.h"

using namespace std;

void Elk::got_shoted() {
    int rand_num = std::rand() % 100;
    double prob = rand_num / 100.0f;
    _is_living = prob < _survivability;
}

void Elk::modify_survivability(double modifier) {
    _survivability *= modifier;
}

bool Elk::is_alive() {
    return _is_living;
}