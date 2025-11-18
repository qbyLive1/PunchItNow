#!/bin/bash
# ============================================================
# PunchITNow 9.0 Octopus - macOS Build Script
# ============================================================
# This script creates a .app bundle for macOS
# ============================================================

set -e  # Exit on error

echo ""
echo "============================================================"
echo "  PunchITNow 9.0 Octopus - macOS Build"
echo "============================================================"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if Python3 is available
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}[ERROR]${NC} Python3 not found! Please install Python 3.8 or higher."
    exit 1
fi

echo -e "${GREEN}[INFO]${NC} Python version: $(python3 --version)"

# Check if pip is available
if ! command -v pip3 &> /dev/null; then
    echo -e "${RED}[ERROR]${NC} pip3 not found! Please install pip."
    exit 1
fi

# Create virtual environment (recommended for macOS)
echo -e "${YELLOW}[INFO]${NC} Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
echo -e "${YELLOW}[INFO]${NC} Upgrading pip..."
pip install --upgrade pip

# Install required packages
echo -e "${YELLOW}[INFO]${NC} Installing required packages..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo -e "${RED}[ERROR]${NC} Failed to install required packages"
    exit 1
fi

# Check if PyInstaller is installed
if ! python3 -c "import PyInstaller" &> /dev/null; then
    echo -e "${YELLOW}[INFO]${NC} Installing PyInstaller..."
    pip install pyinstaller
fi

# Build .app bundle
echo ""
echo -e "${YELLOW}[INFO]${NC} Building PunchITNow 9.0 Octopus.app..."
echo ""

pyinstaller --noconfirm \
    --name "PunchITNow 9.0 Octopus" \
    --onefile \
    --windowed \
    --icon="Punch SOFT.icns" \
    --add-data "config:config" \
    --add-data "themes:themes" \
    --add-data "generated_files:generated_files" \
    --add-data "Account generation.csv:." \
    --hidden-import=customtkinter \
    --hidden-import=PIL \
    --hidden-import=PIL._tkinter_finder \
    --hidden-import=openpyxl \
    --hidden-import=requests \
    --hidden-import=pynput \
    --collect-all customtkinter \
    --osx-bundle-identifier "com.punchsoft.punchit.octopus" \
    "New soft 3.0.py"

if [ $? -ne 0 ]; then
    echo ""
    echo -e "${RED}[ERROR]${NC} Build failed!"
    exit 1
fi

# Check if .app was created
if [ -d "dist/PunchITNow 9.0 Octopus.app" ]; then
    echo ""
    echo "============================================================"
    echo -e "  ${GREEN}BUILD SUCCESSFUL!${NC}"
    echo "============================================================"
    echo ""
    echo "  Application: dist/PunchITNow 9.0 Octopus.app"
    echo "  Version: 9.0 Octopus"
    echo "  Platform: macOS"
    echo ""
    echo "============================================================"
    echo ""
    echo -e "${YELLOW}[INFO]${NC} You can now run: open 'dist/PunchITNow 9.0 Octopus.app'"
else
    echo ""
    echo -e "${RED}[ERROR]${NC} .app bundle not found after build!"
    exit 1
fi

# Deactivate virtual environment
deactivate

echo ""
echo -e "${GREEN}[DONE]${NC} Build process completed!"
echo ""
