# Install script for directory: /home/alex/0_ba/gr-inets/gr-inets/grc

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gnuradio/grc/blocks" TYPE FILE FILES
    "/home/alex/0_ba/gr-inets/gr-inets/grc/inets_frame_sync_cc.xml"
    "/home/alex/0_ba/gr-inets/gr-inets/grc/inets_timing_recovery_cc.xml"
    "/home/alex/0_ba/gr-inets/gr-inets/grc/inets_packetizer.xml"
    "/home/alex/0_ba/gr-inets/gr-inets/grc/inets_packetizer_python.xml"
    "/home/alex/0_ba/gr-inets/gr-inets/grc/inets_unmake_packet_python.xml"
    "/home/alex/0_ba/gr-inets/gr-inets/grc/inets_variable_rotator.xml"
    "/home/alex/0_ba/gr-inets/gr-inets/grc/inets_baseband_derotation.xml"
    "/home/alex/0_ba/gr-inets/gr-inets/grc/inets_stop_and_wait_arq.xml"
    "/home/alex/0_ba/gr-inets/gr-inets/grc/inets_rrrm.xml"
    "/home/alex/0_ba/gr-inets/gr-inets/grc/inets_per_logger.xml"
    "/home/alex/0_ba/gr-inets/gr-inets/grc/inets_rssi.xml"
    )
endif()

