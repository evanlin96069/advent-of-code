#!/bin/bash

# Define the range of days and template file
START_DAY=1
END_DAY=25
TEMPLATE="../template.py"

# Loop through the range of days
for day in $(seq $START_DAY $END_DAY); do
    # Create directory for the day
    mkdir -p "day$day"

    # Change to the new directory
    cd "day$day"

    # Copy the template file
    cp "$TEMPLATE" "day$day.py"

    # Create input and sample files
    touch input.txt
    touch sample.txt

    # Move back to the original directory
    cd ..
done

echo "Templates generated for days $START_DAY to $END_DAY."
