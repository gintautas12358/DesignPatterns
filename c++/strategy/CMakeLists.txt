cmake_minimum_required(VERSION 3.16)

project(strategy)

set(SOURCE
        test.cpp
        src/Elk.cpp
        src/Rifle.cpp
        src/Hunting_odour.cpp
        src/Hunter_game.cpp
        )

include_directories("${PROJECT_SOURCE_DIR}/include")

add_executable(${PROJECT_NAME} ${SOURCE})
