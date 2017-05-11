# Install script for directory: /home/alex/0_ba/gr-inets/gr-inets/python

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/site-packages/inets" TYPE FILE FILES
    "/home/alex/0_ba/gr-inets/gr-inets/python/__init__.py"
    "/home/alex/0_ba/gr-inets/gr-inets/python/packetizer_python.py"
    "/home/alex/0_ba/gr-inets/gr-inets/python/unmake_packet_python.py"
    "/home/alex/0_ba/gr-inets/gr-inets/python/stop_and_wait_arq.py"
    "/home/alex/0_ba/gr-inets/gr-inets/python/rrrm.py"
    "/home/alex/0_ba/gr-inets/gr-inets/python/per_logger.py"
    )
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/site-packages/inets" TYPE FILE FILES
    "/home/alex/0_ba/gr-inets/gr-inets/build/python/__init__.pyc"
    "/home/alex/0_ba/gr-inets/gr-inets/build/python/packetizer_python.pyc"
    "/home/alex/0_ba/gr-inets/gr-inets/build/python/unmake_packet_python.pyc"
    "/home/alex/0_ba/gr-inets/gr-inets/build/python/stop_and_wait_arq.pyc"
    "/home/alex/0_ba/gr-inets/gr-inets/build/python/rrrm.pyc"
    "/home/alex/0_ba/gr-inets/gr-inets/build/python/per_logger.pyc"
    "/home/alex/0_ba/gr-inets/gr-inets/build/python/__init__.pyo"
    "/home/alex/0_ba/gr-inets/gr-inets/build/python/packetizer_python.pyo"
    "/home/alex/0_ba/gr-inets/gr-inets/build/python/unmake_packet_python.pyo"
    "/home/alex/0_ba/gr-inets/gr-inets/build/python/stop_and_wait_arq.pyo"
    "/home/alex/0_ba/gr-inets/gr-inets/build/python/rrrm.pyo"
    "/home/alex/0_ba/gr-inets/gr-inets/build/python/per_logger.pyo"
    )
endif()

