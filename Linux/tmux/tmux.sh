#!/bin/bash


tmux new-session -s run-watch-fork \; \
  send-keys 'echo First pane!' C-m \; \
   send-keys "echo Activate first pane!" C-m \; \
   split-window -v -p 10 \; \
   send-keys 'echo Second pane!' C-m \; \
   send-keys 'echo Activate second pane!' C-m \; \
   select-pane -U \; \
   split-window -h \; \
   send-keys 'echo Third pane!' C-m \; \
   send-keys 'echo Activate third pane!' C-m \; \
   select-pane -D \; \
   split-window -h \; \
   send-keys 'watch -n 5 "find . -type f | grep -P 'DEBUG_CryptographyVerificationServer\.*' | xargs rm"' C-m \; \
   split-window -h \; \
   send-keys 'watch -n 5 "find . -type f | grep -P 'testSession_[0-9]+.json' | xargs rm"' C-m \; \
   select-pane -U \; \
   split-window -h \; \
   send-keys 'echo Forth pane!' C-m \; \
   send-keys 'echo Activate forth pane!' C-m \; \
   split-window -v \; \
   send-keys 'echo Fifth pane!' C-m \; \
   send-keys 'echo Activate fifth pane!' C-m \; \
