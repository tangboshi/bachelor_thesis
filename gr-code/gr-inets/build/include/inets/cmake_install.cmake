# Install script for directory: /home/alex/0_ba/gr-inets/gr-inets/include/inets

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "0")
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/inets" TYPE FILE FILES
    "/home/alex/0_ba/gr-inets/gr-inets/include/inets/api.h"
    "/home/alex/0_ba/gr-inets/gr-inets/include/inets/frame_sync_cc.h"
    "/home/alex/0_ba/gr-inets/gr-inets/include/inets/timing_recovery_cc.h"
    "/home/alex/0_ba/gr-inets/gr-inets/include/inets/packetizer.h"
    "/home/alex/0_ba/gr-inets/gr-inets/include/inets/variable_rotator.h"
    "/home/alex/0_ba/gr-inets/gr-inets/include/inets/baseband_derotation.h"
    "/home/alex/0_ba/gr-inets/gr-inets/include/inets/rssi.h"
    )
endif()

