#!/usr/bin/env bash

# S screenshot save location
defaults write com.apple.screencapture location ~/Downloads

# Show volume button 
defaults write com.apple.systemuiserver "NSStatusItem Visible com.apple.menuextra.volume" -bool true
