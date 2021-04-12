"""Remove excess files from build directory."""
import sys
import glob
import shutil
import os


# QTBIN = os.path.join("PyQt5", "Qt5", "bin")


NAMES = [
    # os.path.join(QTBIN, "concrt140.dll"),
    # os.path.join(QTBIN, "opengl32sw.dll"),

    # "Qt5Designer.dll",
    # "Qt5Location.dll",
    # "Qt5XmlPatterns.dll",
    # "Qt5OpenGL.dll",
    # "Qt5Bluetooth.dll",
    # "Qt5PrintSupport.dll",
    # "Qt5Sensors.dll",
    # "Qt5WebView.dll",
    # "libssl-1_1-x64.dll",
    # "libcrypto-1_1.dll",
    # "qwebgl.dll",
    # "Qt5Quick*.dll",
    # "Qt5Qml*.dll",
    # "Qt5Multimedia*.dll",
    # "Qt5Positioning*.dll",
    # "Qt5Help.dll",
    # "Qt5Nfc.dll",
    # "Qt5RemoteObjects.dll",
    # "Qt5Svg.dll",

    # "d3dcompiler_47.dll",
    # "libGLESv2.dll",
    # "libcrypto-1_1-x64.dll",
    # "libeay32.dll",

    # "python3*.dll",

    # "assetimporters",
    # "geoservices",
    # "*ebengine*",
    # "*qml*",
]


def remove(names, start_path):
    """Find files and directories and remove them."""

    for name in names:
        pattern = os.path.join(start_path, "**", name)

        for found in glob.iglob(pattern, recursive=True):

            if os.path.isdir(found):
                shutil.rmtree(found)

            if os.path.isfile(found):
                os.remove(found)


def main():
    """Entry point."""
    if len(sys.argv) != 2:
        print("syntax: win_post_build <build_path>")
        sys.exit(1)

    build_path = sys.argv[1]
    remove(NAMES, os.path.join(build_path, "lib"))


if __name__ == "__main__":
    main()
