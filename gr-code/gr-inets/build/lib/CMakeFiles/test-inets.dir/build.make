# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.8

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/alex/0_ba/gr-inets/gr-inets

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/alex/0_ba/gr-inets/gr-inets/build

# Include any dependencies generated for this target.
include lib/CMakeFiles/test-inets.dir/depend.make

# Include the progress variables for this target.
include lib/CMakeFiles/test-inets.dir/progress.make

# Include the compile flags for this target's objects.
include lib/CMakeFiles/test-inets.dir/flags.make

lib/CMakeFiles/test-inets.dir/test_inets.cc.o: lib/CMakeFiles/test-inets.dir/flags.make
lib/CMakeFiles/test-inets.dir/test_inets.cc.o: ../lib/test_inets.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/alex/0_ba/gr-inets/gr-inets/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object lib/CMakeFiles/test-inets.dir/test_inets.cc.o"
	cd /home/alex/0_ba/gr-inets/gr-inets/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/test-inets.dir/test_inets.cc.o -c /home/alex/0_ba/gr-inets/gr-inets/lib/test_inets.cc

lib/CMakeFiles/test-inets.dir/test_inets.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test-inets.dir/test_inets.cc.i"
	cd /home/alex/0_ba/gr-inets/gr-inets/build/lib && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/alex/0_ba/gr-inets/gr-inets/lib/test_inets.cc > CMakeFiles/test-inets.dir/test_inets.cc.i

lib/CMakeFiles/test-inets.dir/test_inets.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test-inets.dir/test_inets.cc.s"
	cd /home/alex/0_ba/gr-inets/gr-inets/build/lib && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/alex/0_ba/gr-inets/gr-inets/lib/test_inets.cc -o CMakeFiles/test-inets.dir/test_inets.cc.s

lib/CMakeFiles/test-inets.dir/test_inets.cc.o.requires:

.PHONY : lib/CMakeFiles/test-inets.dir/test_inets.cc.o.requires

lib/CMakeFiles/test-inets.dir/test_inets.cc.o.provides: lib/CMakeFiles/test-inets.dir/test_inets.cc.o.requires
	$(MAKE) -f lib/CMakeFiles/test-inets.dir/build.make lib/CMakeFiles/test-inets.dir/test_inets.cc.o.provides.build
.PHONY : lib/CMakeFiles/test-inets.dir/test_inets.cc.o.provides

lib/CMakeFiles/test-inets.dir/test_inets.cc.o.provides.build: lib/CMakeFiles/test-inets.dir/test_inets.cc.o


lib/CMakeFiles/test-inets.dir/qa_inets.cc.o: lib/CMakeFiles/test-inets.dir/flags.make
lib/CMakeFiles/test-inets.dir/qa_inets.cc.o: ../lib/qa_inets.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/alex/0_ba/gr-inets/gr-inets/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object lib/CMakeFiles/test-inets.dir/qa_inets.cc.o"
	cd /home/alex/0_ba/gr-inets/gr-inets/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/test-inets.dir/qa_inets.cc.o -c /home/alex/0_ba/gr-inets/gr-inets/lib/qa_inets.cc

lib/CMakeFiles/test-inets.dir/qa_inets.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test-inets.dir/qa_inets.cc.i"
	cd /home/alex/0_ba/gr-inets/gr-inets/build/lib && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/alex/0_ba/gr-inets/gr-inets/lib/qa_inets.cc > CMakeFiles/test-inets.dir/qa_inets.cc.i

lib/CMakeFiles/test-inets.dir/qa_inets.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test-inets.dir/qa_inets.cc.s"
	cd /home/alex/0_ba/gr-inets/gr-inets/build/lib && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/alex/0_ba/gr-inets/gr-inets/lib/qa_inets.cc -o CMakeFiles/test-inets.dir/qa_inets.cc.s

lib/CMakeFiles/test-inets.dir/qa_inets.cc.o.requires:

.PHONY : lib/CMakeFiles/test-inets.dir/qa_inets.cc.o.requires

lib/CMakeFiles/test-inets.dir/qa_inets.cc.o.provides: lib/CMakeFiles/test-inets.dir/qa_inets.cc.o.requires
	$(MAKE) -f lib/CMakeFiles/test-inets.dir/build.make lib/CMakeFiles/test-inets.dir/qa_inets.cc.o.provides.build
.PHONY : lib/CMakeFiles/test-inets.dir/qa_inets.cc.o.provides

lib/CMakeFiles/test-inets.dir/qa_inets.cc.o.provides.build: lib/CMakeFiles/test-inets.dir/qa_inets.cc.o


# Object files for target test-inets
test__inets_OBJECTS = \
"CMakeFiles/test-inets.dir/test_inets.cc.o" \
"CMakeFiles/test-inets.dir/qa_inets.cc.o"

# External object files for target test-inets
test__inets_EXTERNAL_OBJECTS =

lib/test-inets: lib/CMakeFiles/test-inets.dir/test_inets.cc.o
lib/test-inets: lib/CMakeFiles/test-inets.dir/qa_inets.cc.o
lib/test-inets: lib/CMakeFiles/test-inets.dir/build.make
lib/test-inets: /lib/libgnuradio-runtime.so
lib/test-inets: /lib/libgnuradio-pmt.so
lib/test-inets: /usr/lib64/libboost_filesystem.so
lib/test-inets: /usr/lib64/libboost_system.so
lib/test-inets: /usr/lib/libcppunit.so
lib/test-inets: lib/libgnuradio-inets.so
lib/test-inets: /lib/libgnuradio-runtime.so
lib/test-inets: /lib/libgnuradio-pmt.so
lib/test-inets: /usr/lib64/libboost_filesystem.so
lib/test-inets: /usr/lib64/libboost_system.so
lib/test-inets: /lib/libgnuradio-digital.so
lib/test-inets: /usr/lib/libuhd.so
lib/test-inets: lib/CMakeFiles/test-inets.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/alex/0_ba/gr-inets/gr-inets/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable test-inets"
	cd /home/alex/0_ba/gr-inets/gr-inets/build/lib && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test-inets.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
lib/CMakeFiles/test-inets.dir/build: lib/test-inets

.PHONY : lib/CMakeFiles/test-inets.dir/build

lib/CMakeFiles/test-inets.dir/requires: lib/CMakeFiles/test-inets.dir/test_inets.cc.o.requires
lib/CMakeFiles/test-inets.dir/requires: lib/CMakeFiles/test-inets.dir/qa_inets.cc.o.requires

.PHONY : lib/CMakeFiles/test-inets.dir/requires

lib/CMakeFiles/test-inets.dir/clean:
	cd /home/alex/0_ba/gr-inets/gr-inets/build/lib && $(CMAKE_COMMAND) -P CMakeFiles/test-inets.dir/cmake_clean.cmake
.PHONY : lib/CMakeFiles/test-inets.dir/clean

lib/CMakeFiles/test-inets.dir/depend:
	cd /home/alex/0_ba/gr-inets/gr-inets/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/alex/0_ba/gr-inets/gr-inets /home/alex/0_ba/gr-inets/gr-inets/lib /home/alex/0_ba/gr-inets/gr-inets/build /home/alex/0_ba/gr-inets/gr-inets/build/lib /home/alex/0_ba/gr-inets/gr-inets/build/lib/CMakeFiles/test-inets.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : lib/CMakeFiles/test-inets.dir/depend

