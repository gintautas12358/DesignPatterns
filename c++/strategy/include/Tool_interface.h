#include "Target_interface.h"

#ifndef TOOLINTERFACE_H
#define TOOLINTERFACE_H

class ToolInterface {
    public:
        virtual void use(TargetInterface* target) = 0;
};

#endif