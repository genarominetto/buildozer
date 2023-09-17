# Automating Android App Build Process using GitHub Actions and Kivy

## Overview

This project focuses on automating the build process of an Android app developed with the Kivy Python framework using GitHub Actions. The primary file for this is `main.yml`, which sets up rules for GitHub Actions to automatically build the Android app whenever there are code changes. 

Other important files include:
- `buildozer.spec`: Contains build configurations
- `main.py`: Holds the basic app code

To use the project, simply modify your Kivy code in `main.py` or update settings in `buildozer.spec`. Once you push changes to GitHub, the build process will be automated by `main.yml`. You can monitor the build under the **Actions** tab on GitHub. Once the build is completed, your Android app will be ready for download.

## How main.yml Works

The YAML configuration file, named `main.yml`, orchestrates the automated build process of the Android application built with Kivy and Python. It is designed to trigger the GitHub Actions workflow on any `push` event that modifies the following files:
- `main.py`
- `.github/workflows/build-android.yml`
- `buildozer.spec`

### Workflow

1. **Initial Setup**: Once initiated, the build job is set to run on the latest version of Ubuntu.
2. **Checkout and Environment Setup**: It checks out the repository and sets up a Python 3.x environment.
3. **Dependency Installation**: Installs all the necessary dependencies including but not limited to `build-essential`, `zlib`, and `JDK 8` by running a series of commands.
4. **Tool Installation**: Sets up Java 8 as the default Java version and installs `Buildozer` and `Cython`, which are key tools for building the Android app.
5. **APK Build and Upload**: Finally, the APK is built using the command `buildozer android debug`. Once generated, it is uploaded as an artifact on GitHub.

You can locate and download this artifact under the **Actions** tab on your GitHub repository, similar to how you monitor the overall build process.
