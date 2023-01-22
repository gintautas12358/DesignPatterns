#include "Gun_interface.h"

#include <iostream>

class Rifle : public Guninterface {
    int _magazine_size;
    int _bullet_count;

    public:
        Rifle() : _magazine_size(4), _bullet_count(0) {}
        void load();
        void shoot(TargetInterface* target);
};