#!/bin/bash
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
echo "=== تثبيت OpenCode Smart AI Key Rotator ==="
pip install --user -r "$DIR/requirements.txt"
[ -f "$HOME/litellm_config.yaml" ] || cp "$DIR/config.example.yaml" "$HOME/litellm_config.yaml"
cp "$DIR/gemini_rotator.py" "$DIR/core_router.py" "$DIR/ui_page.py" "$HOME/"

mkdir -p "$HOME/.config/systemd/user"
cat << UNIT > "$HOME/.config/systemd/user/gemini-rotator.service"
[Unit]
Description=OpenCode Multi-Provider AI Key Rotator
After=network.target

[Service]
Type=simple
Environment=PYTHONPATH=$HOME
ExecStart=/usr/bin/python3 $HOME/gemini_rotator.py
Restart=always
RestartSec=3

[Install]
WantedBy=default.target
UNIT

systemctl --user daemon-reload
systemctl --user enable --now gemini-rotator.service
echo "تم التثبيت والتشغيل بنجاح! افتح: http://localhost:4000/ui"
