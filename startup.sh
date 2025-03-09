#!/bin/bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install -r requirements.txt --no-deps
gunicorn app:app
