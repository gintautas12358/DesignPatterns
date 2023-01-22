#include "Tool_interface.h"
#include <iostream>

class HuntingOdour : public ToolInterface {
    int _uses;
    double _target_modifier;

    public:
        HuntingOdour() : _uses(2), _target_modifier(0.9) {};
        void use(TargetInterface* target);
};