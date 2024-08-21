## Bally Astrocade Program Development Tool (BAPD)

**Status:** Alpha version 1.0

**Overview**

The Bally Astrocade Program Development Tool (BAPD) is a Python-based application designed to assist in the development of Astrocade Z80 assembly language programs. It provides a user-friendly interface for managing projects, compiling source code, running compiled programs using MAME, and configuring various settings.

**Key Features**

* **Project Management:** Create, select, and manage Astrocade projects.
* **Compilation:** Compile source code using ZMAC.
* **Execution:** Run compiled programs in MAME in normal or debug mode.
* **Settings Configuration:** Configure settings for ZMAC and MAME.
* **User Interface:** Intuitive interface for interacting with the tool.
* **Non-Invasive:** The program will not change anything on your computer except for creating a BAPD directory under your user profile directory. Everything is contained in the BAPD directory.

## Installation

**Steps:**

1. **Download and Run BAPD:**
   * Download the BAPD executable from this repository. Note that it is not an installer, the .exe file is the program. It does not matter from where the program runs.
   * Run the BAPD executable file. The main program window will open.
   * [Important] Close the BAPD program. This allows the program to create the project directory.
   * The BAPD tool will create a directory named "BAPD" in your user directory (e.g., `C:\Users\<your_username>\BAPD`).

3. **Install MAME:**
   * Download MAME which is included in this repository for convenience. If you download it from the MAME website, you will need the 64 bit version.
   * Extract the downloaded MAME files into the `BAPD\Programs\MAME` directory.

4. **Install PSPad PORTABLE:**
   * [IMPORTANT!] You must get the PORTABLE version for this Alpha build.
   * Download PSPad PORTABLE which is included in this repository for convenience. If you download it from the PSPad website you will need the 64 bit version.
   * Extract the downloaded PSPad files into the `BAPD\Programs\PSPad` directory.

5. **Launch BAPD:**
   * Run the BAPD executable file again. The tool is now ready to use.


**Known Limitations**
* **MAME and PSPad Installation:** MAME and PSPad need to be installed separately.
* **Alpha Release:** Some features may be incomplete or require further development.
