#include "Target_interface.h"
#include <cstdlib>
#include <ctime>
#include <iostream>

class Elk : public TargetInterface {
    double _survivability;
    bool _is_living;

    public:
        Elk() : _survivability(0.7), _is_living(true) {
            std::srand(std::time(0));
        };
        void got_shoted();
        void modify_survivability(double modifier);
        bool is_alive();
};