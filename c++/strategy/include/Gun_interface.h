#include "Target_interface.h"

#ifndef GUNINTERFACE_H
#define GUNINTERFACE_H

class Guninterface {
    public:
        virtual void load() = 0;
        virtual void shoot(TargetInterface* target) = 0;
};

#endif