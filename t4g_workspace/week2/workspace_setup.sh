#!/bin/bash
my_name ="Hajira Baffoe"
echo "hello, I am $my_name"
echo "Current date and time : $(date)"
mkdir -p session_logs
LOG_FILE="session_logs/$(date +%Y-%m-%d).log"
echo "name: $my_name" >>"$LOG_FILE"
echo "Note: Workspace setup completed successfully." >> "$LOG_FILE"
echo "Assignment completed successfully." 