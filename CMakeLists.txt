# Generated Cmake Pico project file

cmake_minimum_required(VERSION 3.13)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Initialise pico_sdk from installed location
# (note this can come from environment, CMake cache etc)

# == DO NOT EDIT THE FOLLOWING LINES for the Raspberry Pi Pico VS Code Extension to work ==
if(WIN32)
    set(USERHOME $ENV{USERPROFILE})
else()
    set(USERHOME $ENV{HOME})
endif()
set(sdkVersion 2.1.1)
set(toolchainVersion 14_2_Rel1)
set(picotoolVersion 2.1.1)
set(picoVscode ${USERHOME}/.pico-sdk/cmake/pico-vscode.cmake)
if (EXISTS ${picoVscode})
    include(${picoVscode})
endif()
# ====================================================================================
set(PICO_BOARD pico2_w CACHE STRING "Board type")

# Pull in Raspberry Pi Pico SDK (must be before project)
include(pico_sdk_import.cmake)

project(expo-project-2025 C CXX ASM)

# Initialise the Raspberry Pi Pico SDK
pico_sdk_init()

# Add executable. Default name is the project name, version 0.1
add_executable(expo-project-2025 
        expo-project-2025.c
		dhcpserver/dhcpserver.c
		dnsserver/dnsserver.c
		main.cpp
	)

pico_set_program_name(expo-project-2025 "expo-project-2025")
pico_set_program_version(expo-project-2025 "0.1")
pico_set_float_implementation(expo-project-2025 pico_float_pico)

# Generate PIO header
pico_generate_pio_header(expo-project-2025 ${CMAKE_CURRENT_LIST_DIR}/blink.pio)

# Modify the below lines to enable/disable output over UART/USB
pico_enable_stdio_uart(expo-project-2025 0)
pico_enable_stdio_usb(expo-project-2025 0)
pico_enable_stdio_rtt(expo-project-2025 1)

# Add the standard library to the build
target_link_libraries(expo-project-2025
        pico_stdlib)

# Add the standard include files to the build
target_include_directories(expo-project-2025 PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}
        ${CMAKE_CURRENT_LIST_DIR}/dhcpserver
        ${CMAKE_CURRENT_LIST_DIR}/dnsserver
)

# Add any user requested libraries
target_link_libraries(expo-project-2025 
        hardware_dma
        hardware_pio
        pico_cyw43_arch_lwip_threadsafe_background
        pico_float
        )

pico_add_extra_outputs(expo-project-2025)
