cmake_minimum_required(VERSION 3.22.1)
project("dictalearn_native")

find_package(oboe REQUIRED CONFIG)

add_library(
    dictalearn_native
    SHARED
    native-lib.cpp
)

target_link_libraries(
    dictalearn_native
    oboe::oboe
    log
)
